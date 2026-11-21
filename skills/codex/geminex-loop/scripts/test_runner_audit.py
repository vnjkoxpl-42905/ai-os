"""Offline regression tests for the Gemini post-run trajectory audit."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("geminex_runner", Path(__file__).with_name("runner.py"))
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class ReadOnlyAuditTests(unittest.TestCase):
    def test_all_forbidden_categories_in_step_types_and_names(self):
        for tool in runner.FORBIDDEN_REVIEW_TOOLS:
            camel = tool.split('_')[0] + ''.join(x.title() for x in tool.split('_')[1:])
            for value in (tool, camel, tool.replace('_', '-')):
                with self.subTest(tool=tool, spelling=value):
                    with self.assertRaises(runner.RunError):
                        runner.audit_read_only_steps([{'type': 'CORTEX_STEP_TYPE_' + tool.upper()}])
                    with self.assertRaises(runner.RunError):
                        runner.audit_read_only_steps([{'plannerResponse': {'toolCalls': [{'name': value}]}}])

    def test_snake_and_camel_schema_keys_and_nested_function_calls(self):
        for planner in ('plannerResponse', 'planner_response'):
            for calls in ('toolCalls', 'tool_calls', 'functionCalls', 'function_calls'):
                for call in ('toolCall', 'tool_call', 'functionCall', 'function_call'):
                    with self.subTest(planner=planner, calls=calls, call=call):
                        with self.assertRaises(runner.RunError):
                            runner.audit_read_only_steps([{planner: {calls: [{call: {
                                'function': {'name': 'functions.sendMessage'},
                            }}]}}])

    def test_tool_name_identifiers_and_step_payloads(self):
        for key in ('toolName', 'tool_name', 'type'):
            with self.subTest(key=key), self.assertRaises(runner.RunError):
                runner.audit_read_only_steps([{'toolInvocation': {key: 'schedule'}}])
        for key in ('sendMessage', 'ask_question', 'runCommand', 'manageTask', 'callMcpTool'):
            with self.subTest(payload=key), self.assertRaises(runner.RunError):
                runner.audit_read_only_steps([{'type': 'CORTEX_STEP_TYPE_TOOL_CALL', key: {}}])

    def test_old_mutating_enum_aliases(self):
        for value in ('WRITE', 'REPLACE_CONTENT', 'MULTI_REPLACE_CONTENT', 'EDIT', 'CREATE', 'DELETE', 'SUBAGENT'):
            with self.subTest(value=value), self.assertRaises(runner.RunError):
                runner.audit_read_only_steps([{'type': 'CORTEX_STEP_TYPE_' + value}])

    def test_read_only_records_and_metadata_are_not_invocations(self):
        forbidden = [{'name': name} for name in runner.FORBIDDEN_REVIEW_TOOLS]
        runner.audit_read_only_steps([
            {'type': 'CORTEX_STEP_TYPE_USER_INPUT', 'userInput': {'text': 'run_command schedule ask_question'}},
            {'type': 'CORTEX_STEP_TYPE_ERROR_MESSAGE'},
            {'type': 'CORTEX_STEP_TYPE_VIEW_FILE', 'viewFile': {'name': 'schedule', 'type': 'write_file'}},
            {'type': 'CORTEX_STEP_TYPE_PLANNER_RESPONSE',
             'metadata': {'tools': forbidden, 'toolCalls': forbidden, 'schedule': {}},
             'plannerResponse': {'response': 'Never call send_message or write_file.',
                                 'toolConfig': {'toolCalls': forbidden},
                                 'toolCalls': [{'name': 'read_file',
                                                'arguments': {'toolCalls': forbidden},
                                                'argumentsJson': '{"name":"send_message"}',
                                                'result': {'toolCall': {'name': 'schedule'}}}]}}
        ])

    def test_multiple_steps_reject_later_violation(self):
        with self.assertRaises(runner.RunError):
            runner.audit_read_only_steps([{'type': 'CORTEX_STEP_TYPE_VIEW_FILE'},
                                          {'planner_response': {'tool_calls': [{'name': 'ask_question'}]}}])


class ExecuteTurnTests(unittest.TestCase):
    def execute(self, prior, added, read_only):
        def rpc(_server, method, _payload, **_kwargs):
            if method == 'GetCascadeTrajectory':
                return {'trajectory': {'steps': next(trajectories)}}
            if method == 'GetCascadeTrajectoryGeneratorMetadata':
                return {'generatorMetadata': []}
            return {}

        trajectories = iter([prior, prior + added])
        with tempfile.TemporaryDirectory() as folder, patch.object(runner, 'ls_rpc', side_effect=rpc):
            try:
                result = runner.execute_gemini_turn(
                    {'base_url': 'http://localhost'}, Path(folder), Path(folder), 'review evidence',
                    'route', None, None, '00000000-0000-4000-8000-000000000001', 1, read_only)
            except runner.RunError:
                self.assertFalse(Path(folder, 'reply.txt').exists())
                self.assertTrue(Path(folder, 'stdout.txt').exists())
                raise
            self.assertTrue(Path(folder, 'reply.txt').exists())
            return result

    def test_forbidden_current_call_rejected_before_reply_acceptance(self):
        for mode in ('send_message', 'schedule', 'ask_question', 'call_mcp_tool'):
            with self.subTest(tool=mode), self.assertRaises(runner.RunError):
                self.execute([], [{'type': 'CORTEX_STEP_TYPE_PLANNER_RESPONSE',
                                   'plannerResponse': {'response': 'done', 'toolCalls': [{'name': mode}]}}], True)

    def test_previous_turn_calls_do_not_poison_new_safe_turn(self):
        result = self.execute([{'type': 'CORTEX_STEP_TYPE_RUN_COMMAND'}],
                              [{'plannerResponse': {'response': 'done', 'toolCalls': [{'name': 'read_file'}]}}], True)
        self.assertEqual(result['response'], 'done')

    def test_build_bypasses_read_only_post_run_rejection(self):
        result = self.execute([], [{'type': 'CORTEX_STEP_TYPE_WRITE_FILE',
                                   'plannerResponse': {'response': 'built'}}], False)
        self.assertEqual(result['response'], 'built')


if __name__ == '__main__':
    unittest.main()
