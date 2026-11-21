"""Boundary and stale-evidence checks for compiled-knowledge retrieval."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'query-brain.py'
SPEC = importlib.util.spec_from_file_location('query_brain', SCRIPT)
brain = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(brain)


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('wiki/index.md', '# Index\n[[wiki/voice|Voice]]\n[[wiki/booking|Bookings]]')
        self.write('wiki/voice.md', '---\naliases: [apology emails]\n---\n# Voice\n## Apology emails\nKeep the draft plain. [Bookings](booking.md)\n')
        self.write('wiki/booking.md', '# Booking credits\n## Just taken\nCheck the live balance.\n')
        self.write('raw/secret.md', '# Apology emails\nDo not retrieve raw.')
        self.index = brain.build(self.root)

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8')

    def test_alias_finds_evidence_and_safe_pointer(self):
        result = brain.search(self.root, self.index, 'apology emails', follow=True)
        self.assertEqual(result['results'][0]['path'], 'wiki/voice.md')
        self.assertIn('wiki/booking.md', result['results'][0]['pointers'])

    def test_no_match_stays_an_honest_miss(self):
        self.assertEqual(brain.search(self.root, self.index, 'quasarx')['status'],
                         'not-in-compiled-index')

    def test_catalog_change_requires_rebuild(self):
        self.write('wiki/index.md', '# Index\nChanged')
        self.assertEqual(brain.search(self.root, self.index, 'voice')['status'], 'stale-index')

    def test_changed_evidence_is_not_returned_as_current(self):
        self.write('wiki/voice.md', '# Replacement')
        result = brain.search(self.root, self.index, 'apology emails')
        self.assertEqual(result['status'], 'stale-index')
        self.assertEqual(result['results'], [])

    def test_raw_and_outside_paths_are_excluded(self):
        self.assertIsNone(brain.safe_path(self.root, 'raw/secret.md'))
        self.assertIsNone(brain.safe_path(self.root, '../elsewhere.md'))
        self.assertIsNone(brain.safe_path(self.root, '.env'))

    def test_raw_link_in_catalog_is_not_indexed(self):
        self.write('wiki/index.md', '# Index\n[Raw](../raw/secret.md)')
        self.assertEqual([r['path'] for r in brain.build(self.root)['pages']], ['wiki/index.md'])

    def test_equal_candidates_are_explicit(self):
        self.write('wiki/another.md', '# Voice\n')
        self.write('wiki/index.md', '# Index\n[[wiki/another]]\n[[wiki/voice]]')
        data = brain.build(self.root)
        for row in data['pages']:
            row.update(title='Voice', aliases='', headings=[])
        self.assertTrue(brain.search(self.root, data, 'voice')['ambiguous_top_match'])

    def test_synonym_only_match_is_a_candidate(self):
        self.write('wiki/recall.md', '# Recall\nCheck the remembered meaning.')
        self.write('wiki/index.md', '# Index\n[[wiki/recall]]')
        result = brain.search(self.root, brain.build(self.root), 'retention')
        self.assertEqual(result['results'][0]['path'], 'wiki/recall.md')
        self.assertIn('recall', result['results'][0]['matched_expansions'])

    def test_unranked_page_change_invalidates_negative_result(self):
        self.write('wiki/booking.md', '# Retention\nNow relevant.')
        result = brain.search(self.root, self.index, 'retention')
        self.assertEqual(result['status'], 'stale-index')

    def test_new_configured_catalog_requires_rebuild(self):
        self.write('design/README.md', '# New design catalog\n')
        result = brain.search(self.root, self.index, 'design')
        self.assertEqual(result['status'], 'stale-index')
        self.assertIn('design/README.md', result['changed_catalogs'])


if __name__ == '__main__':
    unittest.main()
