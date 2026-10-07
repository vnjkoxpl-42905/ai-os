# Claude conversation 80a0bc11-2647-43df-b4ff-a43eeb3f415c-agent-a2a7b1c06b3cb6d9a

## user

In the LSAT U repo at C:\Users\Joshu\dev\ai-os\projects\lsatu, I need to understand two flows and how to connect them.

Context: I created a `homework_sets` row (title "PT156.S2 (LR)", question_qids = ["PT156-S2-Q1"..."PT156-S2-Q25"]) and assigned it via `assignWork()` (kind: 'homework_set') to a student. The resulting classroom item routes to `/classroom/:assignmentId` (see src/lib/assignWork.ts, the homework_set case's `route` field: `/classroom/${assignmentId}`). When the student opens it and clicks "Start", it shows a plain page with title, description, "25 questions | about 50 minutes | assigned" and a "Start" button — but clicking Start does NOT launch a real timed LR section like the Testing Centre does. I need it to actually launch the section as a normal timed LR test, the same experience as when a student self-serves a section from Testing Centre (src/pages/TestingCentre.tsx + src/components/drill/SectionSelector.tsx + src/lib/questionLoader.ts, which loads /data/PT156-S2-LR.json question bank data keyed by qid like "PT156-S2-Q1").

Please find and report back (under 350 words, concrete file paths and line numbers):

1. What component/page renders at `/classroom/:assignmentId` for a `homework_assignments` row, and where its "Start" button handler is — what does it currently do when clicked (does it navigate anywhere, or is it a dead/stub button)?
2. How does Testing Centre / SectionSelector actually launch a timed section run for a given PT+section (what route or component does it push to, and what params/props does that runner need — e.g. does it need a list of qids, or does it derive the question list itself from pt+section numbers)?
3. Is there an existing runner component (e.g. a "SectionRunner" or similar used by both Testing Centre and Drill) that takes a qid list directly, or does it require deriving PT/section numbers from qids?
4. What is the minimal fix to make the homework "Start" button (or the classroom item's route) launch that same timed-section runner instead of the current stub, given the homework_assignments row already stores `question_qids`? Point to the exact file(s) and function(s) that would need to change, and describe the change in a sentence or two per file — do not write the code yet, just report where and what.

Be concrete. If the homework detail page truly has no wiring to any runner at all, say so plainly.

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && ls", "description": "List repo root"}

## user

Tool result:
ACTIVITIES-CONTEXT.md
ACTIVITIES-DESIGN.md
AGENTS.md
CLASSROOM-DESIGN.md
CLASSROOM-ROUTING-AUDIT.md
CLAUDE.md
COMPREHENSIVEAUDIT.md
CONTEXT-MAP.md
DESIGN.md
Explanations
GEMINI.md
MIGRATION_PLAN_lovable_to_supabase.md
Missing question features
NOTES-RECAPS-AUDIT.md
NOTES-RECAPS-PLAN.md
NOTES-RECAPS-PROGRESS.md
ONBOARDING-SPEC.md
PLAN-REVIEW-LOG.md
PLAN-copy-link.md
PLAN.md
PRODUCT.md
PROTOTYPE_TO_LSATU_PLACEMENT_MAP.md
QUIZ-DESIGN-STANDARD.md
README.md
brainstorms
bun.lock
bun.lockb
classroom-mockup.html
components.json
content
data
deno.lock
design-references
dist
docs
drizzle
drizzle.config.ts
e2e
eslint.config.js
index.html
node_modules
package-lock.json
package.json
plans
playwright-fixture.ts
playwright.config.ts
postcss.config.js
public
qa_audit.py
references
reflection-notes.md
repro.tsx
scripts
session-ingest-auth-gate.png
skills
skills-lock.json
src
structured-flashcards-route-2.png
structured-flashcards-route.png
student-notes
supabase
ta-claude-code-prompt.md
ta-enhancement-roadmap.md
tailwind.config.ts
teacher-desktop-before.png
tsconfig.app.json
tsconfig.json
tsconfig.node.json
vite.config.ts
vite.config.ts.timestamp-1780946164610-c779775623b6.mjs
vitest.config.ts

## assistant

Tool call: Grep
{"pattern": "classroom/:assignmentId|classroom/\\$\\{assignmentId\\}", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu", "output_mode": "files_with_matches"}

## user

Tool result:
Found 3 files
projects\lsatu\src\lib\assignWork.ts
projects\lsatu\docs\main-conclusion-bootcamp\chat-export\full-session.jsonl
projects\lsatu\CLASSROOM-ROUTING-AUDIT.md

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && grep -n \"homework\" -r src/App.tsx src/routes* 2>/dev/null | head -50", "description": "Search for homework routing in App.tsx"}

## user

Tool result:
src/App.tsx:309:            <Route path="/admin/homework" element={
src/App.tsx:311:                <AdminErrorBoundary routeLabel="/admin/homework">
src/App.tsx:318:            <Route path="/admin/homework/new" element={
src/App.tsx:320:                <AdminErrorBoundary routeLabel="/admin/homework/new">
src/App.tsx:329:            <Route path="/admin/homework/:setId" element={
src/App.tsx:331:                <AdminErrorBoundary routeLabel="/admin/homework/:setId">
src/App.tsx:693:                      <Route path="library/homework/:setId" element={

## assistant

Tool call: Grep
{"pattern": "classroom", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\App.tsx", "output_mode": "content", "-n": true}

## user

Tool result:
42:import ClassroomAccountView from "./components/classroom/AccountView";
44:import AdmissionsPage from "./pages/classroom/AdmissionsPage";
45:import ClassroomLayout from "./components/classroom/shell/ClassroomLayout";
52:} from "./components/classroom/ClassroomRouteViews";
56:} from "./components/classroom/FlaggedViews";
60:} from "@/components/classroom/JournalViews";
141:const OVERLAY_FREE_PREFIXES = ["/book/", "/classroom", "/drill", "/rc"];
276:                the classroom's orientation card, which the student opens and
278:            <Route path="/onboarding" element={<Navigate to="/classroom" replace />} />
281:            <Route path="/foyer" element={<Navigate to="/classroom" replace />} />
426:                  <Route path="/" element={<Navigate to="/classroom" replace />} />
503:                    <Route path="/classroom" element={
504:                      <ProtectedRoute flag="has_classroom_access" allowSignedIn><Outlet /></ProtectedRoute>
517:                          assigned work are what has_classroom_access buys. */}
519:                        <ProtectedRoute flag="has_classroom_access"><ClassroomRecapsView /></ProtectedRoute>
525:                        <ProtectedRoute flag="has_classroom_access" allowSignedIn>
530:                        <ProtectedRoute flag="has_classroom_access"><ClassroomItemView /></ProtectedRoute>
533:                        <ProtectedRoute flag="has_classroom_access"><ClassroomTAAssignmentView /></ProtectedRoute>
536:                        <ProtectedRoute flag="has_classroom_access"><ClassroomAssignmentView /></ProtectedRoute>
540:                    {/* The Testing Centre sits inside the classroom frame on
541:                        purpose: choosing a section is still classroom time, and
571:                    {/* Messages is reached from the classroom rail's Support
622:                        Opening it from the classroom rail is entering a room,
623:                        not leaving for another app: the classroom rail stays
770:                      /mainhub was the old *home*, so it goes to the classroom,
772:                  <Route path="/mainhub" element={<Navigate to="/classroom" replace />} />
776:                  <Route path="/practice" element={<Navigate to="/classroom/drill" replace />} />
778:                  {/* Old standalone pages now live inside the classroom
780:                  <Route path="/profile" element={<Navigate to="/classroom/account" replace />} />
781:                  <Route path="/settings/layout" element={<Navigate to="/classroom/account?section=layout" replace />} />

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\App.tsx", "offset": 500, "limit": 45}

## user

Tool result:
500	                      has_flagged_access and nothing about who can reach what
501	                      has changed. */}
502	                  <Route element={<ClassroomLayout />}>
503	                    <Route path="/classroom" element={
504	                      <ProtectedRoute flag="has_classroom_access" allowSignedIn><Outlet /></ProtectedRoute>
505	                    }>
506	                      <Route index element={<Classroom />} />
507	                      <Route path="drill" element={
508	                        <ProtectedRoute flag="has_drill_access">
509	                          <AcademyMainhub />
510	                        </ProtectedRoute>
511	                      } />
512	                      <Route path="uploads" element={<ClassroomUploadsView />} />
513	                      <Route path="account" element={<ClassroomAccountView />} />
514	                      {/* The outlet above lets any signed-in user through so a
515	                          fresh signup can reach the intake and their account.
516	                          Coursework does not ride on that: notes, recaps and
517	                          assigned work are what has_classroom_access buys. */}
518	                      <Route path="recaps" element={
519	                        <ProtectedRoute flag="has_classroom_access"><ClassroomRecapsView /></ProtectedRoute>
520	                      } />
521	                      {/* Admissions is reference, not a paid feature: a student
522	                          deciding whether to work with Joshua should be able to
523	                          see what the schools they want actually took. */}
524	                      <Route path="admissions" element={
525	                        <ProtectedRoute flag="has_classroom_access" allowSignedIn>
526	                          <AdmissionsPage />
527	                        </ProtectedRoute>
528	                      } />
529	                      <Route path="item/:itemId" element={
530	                        <ProtectedRoute flag="has_classroom_access"><ClassroomItemView /></ProtectedRoute>
531	                      } />
532	                      <Route path="ta/:assignmentId" element={
533	                        <ProtectedRoute flag="has_classroom_access"><ClassroomTAAssignmentView /></ProtectedRoute>
534	                      } />
535	                      <Route path=":assignmentId" element={
536	                        <ProtectedRoute flag="has_classroom_access"><ClassroomAssignmentView /></ProtectedRoute>
537	                      } />
538	                    </Route>
539	
540	                    {/* The Testing Centre sits inside the classroom frame on
541	                        purpose: choosing a section is still classroom time, and
542	                        the rail has to stay reachable right up to the moment the
543	                        clock starts. The runners themselves are full-screen
544	                        takeovers registered above, outside this shell. */}

## assistant

Tool call: Grep
{"pattern": "ClassroomAssignmentView", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src", "output_mode": "files_with_matches"}

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\assignWork.ts"}

## user

Tool result:
1	import { supabase } from '@/integrations/supabase/client';
2	import { BOOTCAMPS } from '@/lib/bootcamps';
3	import { createClassroomItem } from '@/lib/classroomItems';
4	import type { ClassroomItemType } from '@/hooks/useClassroomItems';
5	import { notifyStudentOfClassroomItem, type NotifyResult } from '@/lib/classroomNotify';
6	import { parseLocalDay } from '@/lib/localDate';
7	import { coerceStudentLevel, type StudentLevel } from '@/lib/studentLevel';
8	
9	/**
10	 * The one thing a teacher can hand a student. Every assign surface in the
11	 * workspace narrows to this union, so there is exactly one place that knows
12	 * how work reaches a student.
13	 */
14	export type AssignableItem =
15	  | { kind: 'homework_set'; setId: string }
16	  | { kind: 'guided_drill'; drillId: string }
17	  | { kind: 'activity'; activityId: string }
18	  | { kind: 'bootcamp'; topicId: string };
19	
20	export interface StudentResult {
21	  studentId: string;
22	  /**
23	   * The assignment row. Absent for bootcamps, which have no row of their own.
24	   * On a bundle this is the first item's row; see `assignmentIds` for all of them.
25	   */
26	  assignmentId?: string;
27	  classroomItemId?: string;
28	  route?: string;
29	  /** Every assignment row written for this student, in bundle order. */
30	  assignmentIds?: string[];
31	  /** Every classroom item created for this student, in bundle order. */
32	  classroomItemIds?: string[];
33	  /**
34	   * Per-channel notify outcome. A false channel means the work landed and the
35	   * student can see it, but one message did not go out.
36	   */
37	  notify?: NotifyResult;
38	  /** Set only on `failed`: why this student got nothing. */
39	  error?: string;
40	}
41	
42	export interface AssignWorkResult {
43	  ok: StudentResult[];
44	  failed: StudentResult[];
45	}
46	
47	/** What one kind of item needs, resolved once before the per-student loop. */
48	interface AssignPlan {
49	  type: ClassroomItemType;
50	  title: string;
51	  description?: string;
52	  /** Wording for the notification ("New guided drill", etc). */
53	  assignmentType?: string;
54	  sourceTable: string;
55	  /** Insert the assignment row. Returns null for kinds that have no row. */
56	  insertRow: (studentId: string) => Promise<string | null>;
57	  sourceId: (assignmentId: string | null) => string | undefined;
58	  route: (assignmentId: string | null) => string;
59	  unlockAt: string | null;
60	  dueAt: string | null;
61	  metadata: Record<string, unknown>;
62	}
63	
64	function message(error: unknown, fallback: string) {
65	  return error instanceof Error ? error.message : fallback;
66	}
67	
68	/** Per-student proficiency, resolved once for the whole assign. */
69	export type StudentLevelMap = ReadonlyMap<string, StudentLevel | null>;
70	
71	/**
72	 * Postgres 42703 (undefined_column), which PostgREST also surfaces in the
73	 * message. Means the migration has not been applied to this database yet.
74	 */
75	function isMissingColumnError(error: unknown): boolean {
76	  const e = error as { code?: string; message?: string } | null;
77	  if (!e) return false;
78	  if (e.code === '42703') return true;
79	  return /proficiency_level/.test(e.message ?? '') && /does not exist|column/i.test(e.message ?? '');
80	}
81	
82	/**
83	 * Every student's band in one query.
84	 *
85	 * Seeded with null for each requested id, so a student with no profile row is a
86	 * defined "no level" rather than an undefined lookup. A student Joshua has not
87	 * levelled gets null and therefore the drill's own range -- the behaviour that
88	 * predates levels. Inventing a default here would be the system overruling him.
89	 */
90	async function fetchStudentLevels(studentIds: string[]): Promise<StudentLevelMap> {
91	  const levels = new Map<string, StudentLevel | null>(
92	    studentIds.map((id) => [id, null]),
93	  );
94	  if (studentIds.length === 0) return levels;
95	
96	  // proficiency_level is newer than the auto-generated Supabase types, which
97	  // are not hand-editable, so the select is cast at the call site -- the same
98	  // pattern savedSets.ts and questionExposure.ts use for new columns.
99	  const { data, error } = await (supabase.from('profiles') as never as {
100	    select: (cols: string) => {
101	      in: (
102	        col: string,
103	        vals: string[],
104	      ) => Promise<{ data: Array<Record<string, unknown>> | null; error: unknown }>;
105	    };
106	  })
107	    .select('class_id, proficiency_level')
108	    .in('class_id', studentIds);
109	
110	  // The code and the migration do not land atomically. If the app is live
111	  // before the column exists, treat it as "nobody has a level yet" and assign
112	  // exactly as we did before levels existed, rather than breaking every guided
113	  // drill assign until the migration catches up. Any other error is real and
114	  // fails the assign cleanly, because silently unlevelling work Joshua asked to
115	  // be levelled would be worse than not assigning it.
116	  if (error) {
117	    if (isMissingColumnError(error)) {
118	      console.warn('[assignWork] profiles.proficiency_level is not deployed yet; assigning unlevelled');
119	      return levels;
120	    }
121	    throw error;
122	  }
123	
124	  for (const row of data ?? []) {
125	    const id = row.class_id as string;
126	    if (!levels.has(id)) continue;
127	    levels.set(id, coerceStudentLevel(row.proficiency_level, null));
128	  }
129	  return levels;
130	}
131	
132	async function planFor(
133	  item: AssignableItem,
134	  teacherId: string,
135	  scheduledForLocalDate: string | undefined,
136	  levels: StudentLevelMap,
137	  levelOverrides: Record<string, StudentLevel | null> | undefined,
138	  questionCountOverride: number | null | undefined,
139	  frozenQidsByStudent: Record<string, string[]> | undefined,
140	): Promise<AssignPlan> {
141	  /**
142	   * `studentId in overrides` rather than `??`, so an explicit null ("assign
143	   * this one unlevelled") is honoured instead of falling through to the profile.
144	   */
145	  const levelFor = (studentId: string): StudentLevel | null =>
146	    levelOverrides && studentId in levelOverrides
147	      ? levelOverrides[studentId]
148	      : (levels.get(studentId) ?? null);
149	
150	  // A scheduled date is a calendar day the teacher picked, so it has to be read
151	  // in their timezone. Parsed as UTC it would unlock the evening before.
152	  const scheduledDay = scheduledForLocalDate ? parseLocalDay(scheduledForLocalDate) : null;
153	  if (scheduledForLocalDate && !scheduledDay) {
154	    throw new Error(`Not a calendar date: ${scheduledForLocalDate}`);
155	  }
156	  const unlockAt = scheduledDay ? scheduledDay.toISOString() : null;
157	
158	  switch (item.kind) {
159	    case 'homework_set': {
160	      const { data: set, error } = await supabase
161	        .from('homework_sets')
162	        .select('id, title, description, question_qids')
163	        .eq('id', item.setId)
164	        .single();
165	      if (error) throw error;
166	
167	      return {
168	        type: 'homework',
169	        title: set.title,
170	        description: set.description ?? undefined,
171	        assignmentType: 'homework',
172	        sourceTable: 'homework_assignments',
173	        insertRow: async (studentId) => {
174	          const { data, error: insertError } = await supabase
175	            .from('homework_assignments')
176	            .insert({
177	              set_id: set.id,
178	              student_id: studentId,
179	              // The student owns the row, not the set's author. Pointing this
180	              // at the teacher hid assigned homework from the student.
181	              class_id: studentId,
182	              assigned_by: teacherId,
183	              set_title: set.title,
184	              set_description: set.description,
185	              question_qids: set.question_qids ?? [],
186	              status: 'assigned',
187	            })
188	            .select('id')
189	            .single();
190	          if (insertError) throw insertError;
191	          return data.id as string;
192	        },
193	        sourceId: (assignmentId) => assignmentId ?? undefined,
194	        route: (assignmentId) => (assignmentId ? `/classroom/${assignmentId}` : '/classroom'),
195	        unlockAt,
196	        dueAt: null,
197	        metadata: { set_id: set.id },
198	      };
199	    }
200	
201	    case 'guided_drill': {
202	      const { data: drill, error } = await supabase
203	        .from('guided_drills')
204	        .select('id, title, question_count')
205	        .eq('id', item.drillId)
206	        .single();
207	      if (error) throw error;
208	
209	      return {
210	        type: 'drill',
211	        title: drill.title,
212	        description: `New guided drill: ${drill.title}`,
213	        assignmentType: 'guided drill',
214	        sourceTable: 'guided_drill_assignments',
215	        insertRow: async (studentId) => {
216	          // Normally the level is recorded, not resolved: the question draw
217	          // happens when the student opens the drill, so a re-attempt gets a
218	          // fresh set. That is the whole point of the pool model.
219	          //
220	          // Freezing is correct in exactly one case — an offline artifact was
221	          // generated from a specific list and emailed. Then the set has
222	          // already left the building, and a drill that re-draws would serve
223	          // different questions from the file in the student's inbox. Pinning
224	          // here is what makes the two provably the same.
225	          //
226	          // The cost is real and deliberate: a pinned assignment stops
227	          // re-drawing, and resolveLeveledDrillQids returns a pin in full,
228	          // unfiltered by band, so a later level edit on this row is inert.
229	          const frozen = frozenQidsByStudent?.[studentId];
230	          const { data, error: insertError } = await supabase
231	            .from('guided_drill_assignments')
232	            .insert({
233	              guided_drill_id: drill.id,
234	              student_id: studentId,
235	              class_id: studentId,
236	              assigned_by: teacherId,
237	              scheduled_for: scheduledForLocalDate ?? null,
238	              unlock_at: unlockAt,
239	              status: 'assigned',
240	              level: levelFor(studentId),
241	              question_count: questionCountOverride ?? null,
242	              // Spread rather than `question_qids: frozen ?? null`, so the
243	              // default path sends a payload with no such key at all. That is
244	              // what makes "unchanged when not freezing" checkable in a spec
245	              // rather than merely asserted here.
246	              ...(frozen && frozen.length > 0 ? { question_qids: frozen } : {}),
247	            } as never)
248	            .select('id')
249	            .single();
250	          if (insertError) throw insertError;
251	          return data.id as string;
252	        },
253	        sourceId: (assignmentId) => assignmentId ?? undefined,
254	        route: (assignmentId) =>
255	          assignmentId
256	            ? `/guided/${assignmentId}?returnTo=${encodeURIComponent('/classroom')}`
257	            : '/classroom',
258	        unlockAt,
259	        dueAt: null,
260	        metadata: {
261	          guided_drill_id: drill.id,
262	          // The only durable record of WHY this one row is pinned. Six weeks
263	          // later, "why did this drill not re-draw?" has an answer.
264	          ...(frozenQidsByStudent ? { frozen_reason: 'artifact_attached' } : {}),
265	        },
266	      };
267	    }
268	
269	    case 'activity': {
270	      const { data: activity, error } = await supabase
271	        .from('activities')
272	        .select('*')
273	        .eq('id', item.activityId)
274	        .single();
275	      if (error) throw error;
276	
277	      return {
278	        type: 'activity',
279	        title: activity.title,
280	        description: activity.subtitle ?? undefined,
281	        assignmentType: 'activity',
282	        sourceTable: 'activity_assignments',
283	        insertRow: async (studentId) => {
284	          // Content is snapshotted at assign time so editing the activity
285	          // later cannot change work a student has already started.
286	          const { data, error: insertError } = await supabase
287	            .from('activity_assignments')
288	            .insert({
289	              activity_id: activity.id,
290	              student_id: studentId,
291	              class_id: studentId,
292	              assigned_by: teacherId,
293	              title: activity.title,
294	              subtitle: activity.subtitle,
295	              instructions: activity.instructions as never,
296	              item_format: activity.item_format,
297	              items: activity.items as never,
298	              // Snapshotted for the same reason `items` is. The clock is what
299	              // her time is scored against, so a later edit to the Activity
300	              // must not be able to rescore a run she has already finished.
301	              mode: activity.mode,
302	              time_goal_minutes: activity.time_goal_minutes as never,
303	              source_section: activity.source_section,
304	              status: 'assigned',
305	            })
306	            .select('id')
307	            .single();
308	          if (insertError) throw insertError;
309	          return data.id as string;
310	        },
311	        sourceId: (assignmentId) => assignmentId ?? undefined,
312	        route: (assignmentId) => (assignmentId ? `/activities/${assignmentId}` : '/activities'),
313	        unlockAt,
314	        dueAt: null,
315	        metadata: { activity_id: activity.id },
316	      };
317	    }
318	
319	    case 'bootcamp': {
320	      const bootcamp = BOOTCAMPS.find((b) => b.id === item.topicId);
321	      if (!bootcamp) throw new Error(`Unknown bootcamp: ${item.topicId}`);
322	
323	      return {
324	        type: 'bootcamp_module',
325	        title: bootcamp.title,
326	        description: bootcamp.description,
327	        assignmentType: 'bootcamp',
328	        // A bootcamp has no per-student row: the classroom item IS the
329	        // assignment, and source_id is the bootcamp's own route.
330	        sourceTable: 'bootcamps',
331	        insertRow: async () => null,
332	        sourceId: () => bootcamp.route,
333	        route: () => bootcamp.route,
334	        unlockAt,
335	        dueAt: null,
336	        metadata: { bootcamp_id: bootcamp.id },
337	      };
338	    }
339	  }
340	}
341	
342	/**
343	 * Assign one piece of work to one or more students.
344	 *
345	 * Per student, in sequence: insert the assignment row, create the classroom
346	 * item that makes it visible, then notify. Students are isolated from each
347	 * other, so one failure never costs the rest their assignment and never
348	 * re-inserts a row that already landed.
349	 *
350	 * If the classroom item or the notify call throws, the rows already written
351	 * for that student are deleted again: an assignment the student cannot see is
352	 * worse than no assignment, because it silently blocks a re-assign. A notify
353	 * call that returns with a channel `false` is NOT a failure — the work is
354	 * visible in the Classroom and only a message went missing, so it is reported
355	 * on the ok result rather than rolled back.
356	 */
357	export async function assignWork(input: {
358	  teacherId: string;
359	  studentIds: string[];
360	  item: AssignableItem;
361	  /** A local calendar day, YYYY-MM-DD. Unlocks the work that morning. */
362	  scheduledForLocalDate?: string;
363	  /**
364	   * Teacher-authored overrides for what the student sees. The assign builder
365	   * lets Joshua retitle a set or set a due date for one student without
366	   * editing the set itself.
367	   */
368	  overrides?: {
369	    title?: string;
370	    description?: string;
371	    dueAt?: string | null;
372	    metadata?: Record<string, unknown>;
373	  };
374	  /**
375	   * Per-student band, overriding their profile level. An explicit null assigns
376	   * that student unlevelled. Guided drills only.
377	   */
378	  levelOverrides?: Record<string, StudentLevel | null>;
379	  /** Shorten the drill for everyone in this assign. Guided drills only. */
380	  questionCountOverride?: number | null;
381	  /** See assignWorkBundle. Guided drills only. */
382	  frozenQidsByStudent?: Record<string, string[]>;
383	  /**
384	   * Send the student a notification. Default true. Set false only when the
385	   * caller sends its own message covering this work.
386	   */
387	  notify?: boolean;
388	}): Promise<AssignWorkResult> {
389	  return runAssign({ ...input, items: [input.item] });
390	}
391	
392	/**
393	 * Assign several pieces of work — of mixed kinds — as ONE event (spec D4).
394	 *
395	 * A drill and a homework set for the same topic ship together: the student gets
396	 * a classroom card for each (they are separate work), but a single notification,
397	 * because two pings for one handoff reads as two assignments. Per student the
398	 * bundle is all-or-nothing: if the third item fails, the first two are rolled
399	 * back, so the teacher never has to reason about a half-delivered bundle.
400	 *
401	 * Per-item overrides are deliberately not offered here — retitling one item
402	 * inside a bundle belongs to the single-item path.
403	 */
404	export async function assignWorkBundle(input: {
405	  teacherId: string;
406	  studentIds: string[];
407	  items: AssignableItem[];
408	  scheduledForLocalDate?: string;
409	  /** Per-student band. Applies to every guided drill in the bundle. */
410	  levelOverrides?: Record<string, StudentLevel | null>;
411	  questionCountOverride?: number | null;
412	  /**
413	   * Pin an exact question list on the guided-drill row instead of drawing at
414	   * open time. Keyed by studentId, because two students at different bands
415	   * freeze different sets from the same drill.
416	   *
417	   * Set this ONLY when an offline artifact is produced from the same list.
418	   * A pinned assignment stops re-drawing on re-attempt, and a later level
419	   * change on that row has no effect. Guided drills only.
420	   */
421	  frozenQidsByStudent?: Record<string, string[]>;
422	  /** See assignWork. Default true. */
423	  notify?: boolean;
424	}): Promise<AssignWorkResult> {
425	  return runAssign(input);
426	}
427	
428	/** What one student ended up with, so a failure can be undone precisely. */
429	interface Written {
430	  assignmentId: string | null;
431	  classroomItemId: string | null;
432	  table: string;
433	  kind: AssignableItem['kind'];
434	}
435	
436	async function runAssign(input: {
437	  teacherId: string;
438	  studentIds: string[];
439	  items: AssignableItem[];
440	  scheduledForLocalDate?: string;
441	  overrides?: {
442	    title?: string;
443	    description?: string;
444	    dueAt?: string | null;
445	    metadata?: Record<string, unknown>;
446	  };
447	  levelOverrides?: Record<string, StudentLevel | null>;
448	  questionCountOverride?: number | null;
449	  frozenQidsByStudent?: Record<string, string[]>;
450	  notify?: boolean;
451	}): Promise<AssignWorkResult> {
452	  const {
453	    teacherId,
454	    studentIds,
455	    items,
456	    scheduledForLocalDate,
457	    overrides,
458	    levelOverrides,
459	    questionCountOverride,
460	    frozenQidsByStudent,
461	    notify: shouldNotify = true,
462	  } = input;
463	
464	  const ok: StudentResult[] = [];
465	  const failed: StudentResult[] = [];
466	
467	  if (studentIds.length === 0 || items.length === 0) return { ok, failed };
468	
469	  /*
470	   * Freezing is validated before any write, and it throws rather than
471	   * degrading. A silent no-op here is the exact failure this feature exists to
472	   * prevent: an artifact would be emailed carrying questions the assignment
473	   * row does not hold, and nothing downstream could tell.
474	   */
475	  if (frozenQidsByStudent) {
476	    if (!items.some((item) => item.kind === 'guided_drill')) {
477	      throw new Error('frozenQidsByStudent was supplied but no guided drill is being assigned');
478	    }
479	    for (const [studentId, qids] of Object.entries(frozenQidsByStudent)) {
480	      if (!studentIds.includes(studentId)) {
481	        throw new Error(`frozenQidsByStudent names ${studentId}, who is not in this assign`);
482	      }
483	      if (!Array.isArray(qids) || qids.length === 0) {
484	        throw new Error(`frozenQidsByStudent[${studentId}] is empty; omit the student instead`);
485	      }
486	    }
487	  }
488	
489	  // Every item is resolved before anyone is written to, so an unreadable item
490	  // fails the whole assign cleanly instead of half-delivering the bundle. An
491	  // unreadable student level belongs in the same block for the same reason: the
492	  // catch below reports every student as failed and nothing has been written.
493	  let plans: AssignPlan[];
494	  try {
495	    // Only guided drills carry a level, so nothing else pays for the lookup.
496	    const needsLevels = items.some((item) => item.kind === 'guided_drill');
497	    const levels: StudentLevelMap = needsLevels
498	      ? await fetchStudentLevels(studentIds)
499	      : new Map();
500	
501	    plans = await Promise.all(
502	      items.map(async (item, index) => {
503	        const base = await planFor(
504	          item,
505	          teacherId,
506	          scheduledForLocalDate,
507	          levels,
508	          levelOverrides,
509	          questionCountOverride,
510	          frozenQidsByStudent,
511	        );
512	        // Overrides only ever accompany a single item (see assignWork).
513	        if (index > 0 || !overrides) return base;
514	        return {
515	          ...base,
516	          title: overrides.title?.trim() || base.title,
517	          description: overrides.description?.trim() || base.description,
518	          dueAt: overrides.dueAt !== undefined ? overrides.dueAt : base.dueAt,
519	          metadata: { ...base.metadata, ...(overrides.metadata ?? {}) },
520	        };
521	      }),
522	    );
523	  } catch (error) {
524	    // Nothing was written, so every student failed for the same reason.
525	    const reason = message(error, 'Could not load the item to assign');
526	    return { ok, failed: studentIds.map((studentId) => ({ studentId, error: reason })) };
527	  }
528	
529	  for (const studentId of studentIds) {
530	    const written: Written[] = [];
531	
532	    try {
533	      const routes: string[] = [];
534	
535	      for (let i = 0; i < plans.length; i++) {
536	        const plan = plans[i];
537	        const record: Written = {
538	          assignmentId: null,
539	          classroomItemId: null,
540	          table: plan.sourceTable,
541	          kind: items[i].kind,
542	        };
543	        // Recorded before each write so a throw mid-item still rolls back what
544	        // the previous items wrote.
545	        written.push(record);
546	
547	        record.assignmentId = await plan.insertRow(studentId);
548	        const route = plan.route(record.assignmentId);
549	        routes.push(route);
550	
551	        const classroomItem = await createClassroomItem({
552	          studentId,
553	          createdBy: teacherId,
554	          type: plan.type,
555	          title: plan.title,
556	          description: plan.description,
557	          sourceTable: plan.sourceTable,
558	          sourceId: plan.sourceId(record.assignmentId),
559	          unlockAt: plan.unlockAt,
560	          dueAt: plan.dueAt,
561	          visibleToStudent: true,
562	          status: 'assigned',
563	          metadata: { ...plan.metadata, assigned_route: route },
564	        });
565	        record.classroomItemId = classroomItem.id;
566	      }
567	
568	      // A caller that owns its own messaging opts out. The weekly-plan builder
569	      // does: it sends one summary for the whole week, and seven bell entries
570	      // for one plan is the exact UX it already avoids.
571	      const summary = notificationFor(plans, routes);
572	      const notify = shouldNotify
573	        ? await notifyStudentOfClassroomItem({
574	            adminUserId: teacherId,
575	            studentId,
576	            title: summary.title,
577	            description: summary.description,
578	            route: summary.route,
579	            assignmentType: summary.assignmentType,
580	          })
581	        : undefined;
582	
583	      ok.push({
584	        studentId,
585	        assignmentId: written[0]?.assignmentId ?? undefined,
586	        classroomItemId: written[0]?.classroomItemId ?? undefined,
587	        route: routes[0],
588	        assignmentIds: written.map((w) => w.assignmentId).filter((id): id is string => !!id),
589	        classroomItemIds: written
590	          .map((w) => w.classroomItemId)
591	          .filter((id): id is string => !!id),
592	        notify,
593	      });
594	    } catch (error) {
595	      console.error('[assignWork] student failed', {
596	        studentId,
597	        kinds: items.map((i) => i.kind),
598	        written,
599	        error,
600	      });
601	      // Newest first, so the half-written item goes before the ones that landed.
602	      for (const record of [...written].reverse()) {
603	        await rollback(record);
604	      }
605	      failed.push({ studentId, error: message(error, 'Assign failed') });
606	    }
607	  }
608	
609	  return { ok, failed };
610	}
611	
612	/**
613	 * One handoff, one message. A single item keeps its own wording; a bundle is
614	 * announced as a list pointing at the Classroom, since no one route covers it.
615	 */
616	function notificationFor(
617	  plans: AssignPlan[],
618	  routes: string[],
619	): { title: string; description?: string; route: string; assignmentType?: string } {
620	  if (plans.length === 1) {
621	    return {
622	      title: plans[0].title,
623	      description: plans[0].description,
624	      route: routes[0],
625	      assignmentType: plans[0].assignmentType,
626	    };
627	  }
628	  return {
629	    title: `${plans.length} new pieces of work`,
630	    description: plans.map((p) => `• ${p.title}`).join('\n'),
631	    route: '/classroom',
632	    assignmentType: 'assignment',
633	  };
634	}
635	
636	/**
637	 * One sentence for the teacher, in the order they care about: who missed out,
638	 * then which messages did not go, then plain success. Shared so every assign
639	 * surface reports the same outcome the same way.
640	 */
641	export function describeAssignResult(
642	  result: AssignWorkResult,
643	  title: string,
644	): { level: 'success' | 'warning' | 'error'; message: string } {
645	  const { ok, failed } = result;
646	  const students = (n: number) => `${n} student${n === 1 ? '' : 's'}`;
647	
648	  if (ok.length === 0) {
649	    return {
650	      level: 'error',
651	      message: failed[0]?.error
652	        ? `Could not assign "${title}": ${failed[0].error}`
653	        : `Could not assign "${title}"`,
654	    };
655	  }
656	
657	  if (failed.length > 0) {
658	    return {
659	      level: 'warning',
660	      message: `Assigned "${title}" to ${students(ok.length)}. ${students(failed.length)} failed: ${failed[0].error ?? 'unknown error'}`,
661	    };
662	  }
663	
664	  const quiet = ok.filter((r) => r.notify && !(r.notify.inbox_ok && r.notify.bell_ok && r.notify.email_ok));
665	  if (quiet.length > 0) {
666	    return {
667	      level: 'warning',
668	      message: `Assigned "${title}" to ${students(ok.length)}, but ${students(quiet.length)} were not fully notified.`,
669	    };
670	  }
671	
672	  return { level: 'success', message: `Assigned "${title}" to ${students(ok.length)}` };
673	}
674	
675	/**
676	 * Undo a half-written assign. Best effort: if the cleanup itself fails there is
677	 * nothing further to try, so it is logged loudly and swallowed rather than
678	 * masking the original error that sent us here.
679	 */
680	async function rollback(input: {
681	  assignmentId: string | null;
682	  classroomItemId: string | null;
683	  table: string;
684	  kind: AssignableItem['kind'];
685	}) {
686	  const { assignmentId, classroomItemId, table, kind } = input;
687	
688	  if (classroomItemId) {
689	    const { error } = await supabase.from('classroom_items').delete().eq('id', classroomItemId);
690	    if (error) console.error('[assignWork] rollback left a classroom item', { classroomItemId, error });
691	  }
692	
693	  // Bootcamps write no assignment row, so there is nothing else to undo.
694	  if (!assignmentId || kind === 'bootcamp') return;
695	
696	  const { error } = await supabase
697	    .from(table as 'homework_assignments' | 'guided_drill_assignments' | 'activity_assignments')
698	    .delete()
699	    .eq('id', assignmentId);
700	  if (error) console.error('[assignWork] rollback left an assignment row', { table, assignmentId, error });
701	}
702	

## user

Tool result:
Found 2 files
projects\lsatu\src\components\classroom\ClassroomRouteViews.tsx
projects\lsatu\src\App.tsx

## assistant

Now let's look at ClassroomAssignmentView (in ClassroomRouteViews.tsx) and its Start button.

## assistant

Tool call: Grep
{"pattern": "ClassroomAssignmentView|homework_assignments|Start", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\classroom\\ClassroomRouteViews.tsx", "output_mode": "content", "-n": true}

## user

Tool result:
469:export function ClassroomAssignmentView() {
546:              : setQuery.set?.start_button_label || "Start"}

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\classroom\\ClassroomRouteViews.tsx", "offset": 1, "limit": 60}

## user

Tool result:
1	import * as React from "react";
2	import { useNavigate, useParams } from "react-router-dom";
3	import { toast } from "sonner";
4	import { useClassroomItems } from "@/hooks/useClassroomItems";
5	import {
6	  markTAAssignmentCompleted,
7	  markTAAssignmentViewed,
8	  useStudentAssignment,
9	  useStudentTAAssignment,
10	} from "@/hooks/useStudentAssignments";
11	import StructuredTAAssignmentWorkspace from "@/components/classroom/StructuredTAAssignmentWorkspace";
12	import { hasStructuredWorkspace } from "@/components/classroom/structured-assignment-model";
13	import { useStudentExternalUploads } from "@/hooks/useExternalWorkUploads";
14	import { useHomeworkSet } from "@/hooks/useHomeworkSets";
15	import { useQueryClient } from "@tanstack/react-query";
16	import { resolveItemRoute } from "@/lib/classroomItems";
17	import { markNoteRead } from "@/lib/markNoteRead";
18	import {
19	  groupNotes,
20	  NOTE_TYPES,
21	  sanitizeClassroomHtml,
22	} from "@/components/classroom/classroomData";
23	import {
24	  StageIndexHint,
25	  StageIndexList,
26	  shortDate,
27	} from "@/components/classroom/StageIndexList";
28	
29	function formatClassroomDate(value: string | Date) {
30	  return new Intl.DateTimeFormat("en-CA", {
31	    day: "numeric",
32	    month: "long",
33	    year: "numeric",
34	  }).format(typeof value === "string" ? new Date(value) : value);
35	}
36	
37	/**
38	 * Row and heading labels for note types. The raw enum leaked into the UI, so a
39	 * student read "note" and "smartboard recap".
40	 *
41	 * `smartboard_recap` is a dead type as far as students are concerned: Joshua
42	 * confirmed 2026-09-09 that boards are not attached to accounts, so no student
43	 * ever sees this label. It stays because the teacher side can still write the
44	 * type and an unmapped value would fall through to the raw enum. Do not spend
45	 * effort wording it.
46	 */
47	const NOTE_KIND_LABELS: Record<string, string> = {
48	  note: "Note",
49	  session_recap: "Session recap",
50	  smartboard_recap: "Board from your session",
51	  announcement: "Announcement",
52	};
53	
54	function noteKind(type: string) {
55	  return NOTE_KIND_LABELS[type] ?? type.replace(/_/g, " ");
56	}
57	
58	/**
59	 * First ~55 words of a note, for the landing preview.
60	 *

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\classroom\\ClassroomRouteViews.tsx", "offset": 460, "limit": 180}

## user

Tool result:
460	              </span>
461	            </div>
462	          ))}
463	        </section>
464	      ) : null}
465	    </>
466	  );
467	}
468	
469	export function ClassroomAssignmentView() {
470	  const { assignmentId } = useParams<{ assignmentId: string }>();
471	  const navigate = useNavigate();
472	  const assignmentQuery = useStudentAssignment(assignmentId);
473	  const setQuery = useHomeworkSet(assignmentQuery.assignment?.set_id ?? undefined);
474	  const assignment = assignmentQuery.assignment;
475	
476	  const start = () => {
477	    if (!assignment) return;
478	    const params = new URLSearchParams({
479	      mode: "type-drill",
480	      qids: assignment.question_qids.join(","),
481	      assignmentId: assignment.id,
482	    });
483	    if (setQuery.set?.id && setQuery.set.is_guided_set) {
484	      params.set("guidedSetId", setQuery.set.id);
485	    }
486	    navigate(`/drill?${params.toString()}`);
487	  };
488	
489	  if (assignmentQuery.loading && !assignment) return <DetailLoading />;
490	  if (assignmentQuery.error) {
491	    return (
492	      <DetailError
493	        message="Could not load this assignment."
494	        retry={() => void assignmentQuery.refresh()}
495	      />
496	    );
497	  }
498	  if (!assignment) {
499	    return (
500	      <>
501	        <DetailHeading
502	          date={new Date().toISOString()}
503	          kind="Assignment"
504	          title="Assignment not found"
505	        />
506	      </>
507	    );
508	  }
509	
510	  const estimatedMinutes =
511	    setQuery.set?.estimated_minutes ??
512	    Math.max(1, Math.ceil(assignment.question_qids.length * 2));
513	
514	  return (
515	    <>
516	      <DetailHeading
517	        date={assignment.created_at}
518	        kind="Assignment"
519	        title={assignment.set_title}
520	      />
521	      {assignment.set_description ? (
522	        <div className="classroom-callout">{assignment.set_description}</div>
523	      ) : null}
524	      <div className="classroom-note-meta">
525	        {assignment.question_qids.length} question
526	        {assignment.question_qids.length === 1 ? "" : "s"} | about{" "}
527	        {estimatedMinutes} minutes | {assignment.status.replace(/_/g, " ")}
528	      </div>
529	      {setQuery.error ? (
530	        <DetailError
531	          message="Some assignment details could not be loaded."
532	          retry={() => void setQuery.refresh()}
533	        />
534	      ) : null}
535	      <div className="classroom-detail-actions">
536	        <button
537	          type="button"
538	          className="classroom-button classroom-button-primary"
539	          disabled={setQuery.loading}
540	          onClick={start}
541	        >
542	          {assignment.status === "completed"
543	            ? "Review"
544	            : assignment.status === "in_progress"
545	              ? "Continue"
546	              : setQuery.set?.start_button_label || "Start"}
547	        </button>
548	      </div>
549	    </>
550	  );
551	}
552	
553	export function ClassroomTAAssignmentView() {
554	  const { assignmentId } = useParams<{ assignmentId: string }>();
555	  const query = useStudentTAAssignment(assignmentId);
556	  const assignment = query.assignment;
557	  const structured = assignment ? hasStructuredWorkspace(assignment) : false;
558	  const [completing, setCompleting] = React.useState(false);
559	  const [downloading, setDownloading] = React.useState(false);
560	  const viewedRef = React.useRef<string | null>(null);
561	
562	  React.useEffect(() => {
563	    if (!assignment || assignment.status !== "assigned") return;
564	    if (viewedRef.current === assignment.id) return;
565	    viewedRef.current = assignment.id;
566	    void markTAAssignmentViewed(assignment.id).then((result) => {
567	      if (result.ok) void query.refresh();
568	    });
569	  }, [assignment, query]);
570	
571	  const safeHtml = React.useMemo(
572	    () => sanitizeClassroomHtml(assignment?.content_html ?? ""),
573	    [assignment?.content_html],
574	  );
575	
576	  const download = async () => {
577	    if (!assignment) return;
578	    setDownloading(true);
579	    try {
580	      const { downloadAssignmentPdf } = await import("@/lib/taPdf");
581	      await downloadAssignmentPdf({
582	        title: assignment.title,
583	        contentHtml: safeHtml,
584	      });
585	    } catch (error) {
586	      toast.error(error instanceof Error ? error.message : "PDF download failed");
587	    } finally {
588	      setDownloading(false);
589	    }
590	  };
591	
592	  const complete = async () => {
593	    if (!assignment) return;
594	    setCompleting(true);
595	    const result = await markTAAssignmentCompleted(assignment.id);
596	    if (result.ok) {
597	      toast.success("Marked complete");
598	      await query.refresh();
599	    } else {
600	      toast.error(result.error ?? "Could not mark this complete");
601	    }
602	    setCompleting(false);
603	  };
604	
605	  if (query.loading && !assignment) return <DetailLoading />;
606	  if (query.error) {
607	    return (
608	      <DetailError
609	        message="Could not load this assignment."
610	        retry={() => void query.refresh()}
611	      />
612	    );
613	  }
614	  if (!assignment) {
615	    return (
616	      <DetailHeading
617	        date={new Date().toISOString()}
618	        kind="Assignment"
619	        title="Assignment not found"
620	      />
621	    );
622	  }
623	
624	  return (
625	    <>
626	      <DetailHeading
627	        date={assignment.assigned_at}
628	        kind="Assignment"
629	        title={assignment.title}
630	      />
631	      <div className="classroom-note-meta">
632	        {assignment.status.replace(/_/g, " ")}
633	      </div>
634	      {safeHtml ? (
635	        <article
636	          className="classroom-prose"
637	          dangerouslySetInnerHTML={{ __html: safeHtml }}
638	        />
639	      ) : null}

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && grep -n \"\\\"/drill\\\"\\|'/drill'\\|path=\\\"drill\" src/App.tsx", "description": "Find /drill route registration"}

## assistant

Tool call: Grep
{"pattern": "type-drill", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src", "output_mode": "files_with_matches"}

## user

Tool result:
141:const OVERLAY_FREE_PREFIXES = ["/book/", "/classroom", "/drill", "/rc"];
430:                  <Route path="/drill" element={
507:                      <Route path="drill" element={

## user

Tool result:
Found 40 files
projects\lsatu\src\components\classroom\ClassroomRouteViews.tsx
projects\lsatu\src\pages\AcademyMainhub.tsx
projects\lsatu\src\components\mainhub\PracticeInsightStage.tsx
projects\lsatu\src\pages\AcademyMainhub.section.test.tsx
projects\lsatu\src\components\questionfinder\QuestionFinder.tsx
projects\lsatu\src\components\mainhub\insightSlides.ts
projects\lsatu\src\types\drill.ts
projects\lsatu\src\pages\Drill.tsx
projects\lsatu\src\pages\ClassroomAssignmentDetail.tsx
projects\lsatu\src\pages\Analytics.tsx
projects\lsatu\src\lib\questionPoolService.ts
projects\lsatu\src\lib\questionPoolService.test.ts
projects\lsatu\src\lib\mainhubAnalytics.test.ts
projects\lsatu\src\lib\guidedDrillSession.ts
projects\lsatu\src\lib\drillRunSpec.ts
projects\lsatu\src\lib\drillResumeSession.ts
projects\lsatu\src\lib\drillResumeSession.test.ts
projects\lsatu\src\lib\drillLaunchResolve.ts
projects\lsatu\src\lib\drillLaunchResolve.resume.test.ts
projects\lsatu\src\lib\drillLaunch.ts
projects\lsatu\src\lib\drillLaunch.test.ts
projects\lsatu\src\features\rc\pages\RcRedirect.tsx
projects\lsatu\src\features\rc\pages\RcRedirect.test.tsx
projects\lsatu\src\features\rc\pages\RcHub.tsx
projects\lsatu\src\features\rc\components\RcHubSurface.test.tsx
projects\lsatu\src\features\rc\CONTEXT.md
projects\lsatu\src\components\questionfinder\questionFinderSearch.ts
projects\lsatu\src\components\questionfinder\questionFinderSearch.test.ts
projects\lsatu\src\components\questionfinder\QuestionJump.tsx
projects\lsatu\src\components\questionfinder\QuestionFinder.test.tsx
projects\lsatu\src\components\mainhub\AnalyticsStage.tsx
projects\lsatu\src\components\drill\SectionReviewWalk.tsx
projects\lsatu\src\components\drill\ModeSelector.tsx
projects\lsatu\src\components\drill\LRSectionResults.tsx
projects\lsatu\src\components\drill\DrillLaunchGate.tsx
projects\lsatu\src\components\drill\DrillLaunchGate.test.tsx
projects\lsatu\src\components\classroom\FlaggedViews.tsx
projects\lsatu\src\components\analytics\FlaggedQuestionsList.tsx
projects\lsatu\src\bootcamps\fallacy-flaw-v2\components\GuidedDrills.tsx
projects\lsatu\src\bootcamps\fallacy-flaw-v2\components\FlawDrillLauncher.tsx

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\pages\\Drill.tsx"}

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\pages\\ClassroomAssignmentDetail.tsx"}

## user

Tool result:
1	import * as React from "react";
2	import { useNavigate, useParams } from "react-router-dom";
3	import { useAuth } from "@/contexts/AuthContext";
4	import { Button } from "@/components/ui/button";
5	import { Skeleton } from "@/components/ui/skeleton";
6	import { ArrowLeft, Play, Eye, Clock } from "lucide-react";
7	import { ThemeToggle } from "@/components/ThemeToggle";
8	import { LogoutButton } from "@/components/LogoutButton";
9	import {
10	  useStudentAssignment,
11	  type AssignmentStatus,
12	} from "@/hooks/useStudentAssignments";
13	import { useHomeworkSet } from "@/hooks/useHomeworkSets";
14	import { GuidedDrillLaunchFrame } from "@/components/drill/GuidedDrillLaunchFrame";
15	import {
16	  buildGuidedDrillLaunchHtml,
17	  splitInstructionColumns,
18	} from "@/lib/guidedDrillLaunch";
19	
20	function StatusBadge({ status }: { status: AssignmentStatus }) {
21	  const map: Record<AssignmentStatus, { label: string; cls: string }> = {
22	    assigned: {
23	      label: "Assigned",
24	      cls: "bg-secondary text-foreground/80 ring-border",
25	    },
26	    in_progress: {
27	      label: "In progress",
28	      cls: "bg-amber-500/10 text-amber-400 ring-amber-500/20",
29	    },
30	    completed: {
31	      label: "Completed",
32	      cls: "bg-emerald-500/10 text-emerald-400 ring-emerald-500/20",
33	    },
34	  };
35	  const cfg = map[status];
36	  return (
37	    <span
38	      className={`inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-medium ring-1 ${cfg.cls}`}
39	    >
40	      {cfg.label}
41	    </span>
42	  );
43	}
44	
45	export default function ClassroomAssignmentDetail() {
46	  const navigate = useNavigate();
47	  const { assignmentId } = useParams<{ assignmentId: string }>();
48	  const { user } = useAuth();
49	  const { assignment, loading } = useStudentAssignment(assignmentId);
50	  const { set: parentSet, loading: parentLoading } = useHomeworkSet(
51	    assignment?.set_id ?? undefined,
52	  );
53	  const [showCard, setShowCard] = React.useState(false);
54	
55	  React.useEffect(() => {
56	    if (!user) navigate("/auth");
57	  }, [user, navigate]);
58	
59	  const isGuided = parentSet?.is_guided_set === true;
60	
61	  const navigateToDrill = React.useCallback(() => {
62	    if (!assignment) return;
63	    const qidsParam = assignment.question_qids.join(",");
64	    const params = new URLSearchParams({
65	      mode: "type-drill",
66	      qids: qidsParam,
67	      assignmentId: assignment.id,
68	    });
69	    if (parentSet?.id && isGuided) {
70	      params.set("guidedSetId", parentSet.id);
71	    }
72	    navigate(`/drill?${params.toString()}`);
73	  }, [assignment, parentSet, isGuided, navigate]);
74	
75	  const handleStart = () => {
76	    if (!assignment) return;
77	    if (isGuided) {
78	      setShowCard(true);
79	      return;
80	    }
81	    navigateToDrill();
82	  };
83	
84	  const estMinutes = assignment
85	    ? parentSet?.estimated_minutes ??
86	      Math.max(1, Math.ceil(assignment.question_qids.length * 2))
87	    : 0;
88	
89	  // Render the full-page premium launch screen before transitioning to the
90	  // drill — identical format to every other guided drill.
91	  if (showCard && assignment && parentSet && isGuided) {
92	    const { left, right } = splitInstructionColumns(parentSet.instructions_markdown);
93	    const html = buildGuidedDrillLaunchHtml({
94	      title: parentSet.title,
95	      estimatedMinutes: parentSet.estimated_minutes,
96	      questionCount: assignment.question_qids.length,
97	      leftMd: left,
98	      rightMd: right,
99	    });
100	    return (
101	      <GuidedDrillLaunchFrame
102	        html={html}
103	        title={parentSet.title}
104	        onStart={navigateToDrill}
105	        onReturn={() => setShowCard(false)}
106	      />
107	    );
108	  }
109	
110	  return (
111	    <div className="min-h-screen bg-background">
112	      <header className="sticky top-0 z-10 border-b border-border bg-background/80 backdrop-blur-xl">
113	        <div className="px-4 lg:px-8 py-4 flex items-center justify-between max-w-4xl mx-auto">
114	          <Button
115	            variant="ghost"
116	            size="sm"
117	            onClick={() => navigate("/classroom")}
118	            className="gap-2 text-muted-foreground hover:text-foreground hover:bg-accent -ml-2"
119	          >
120	            <ArrowLeft className="h-3.5 w-3.5" />
121	            Back to Classroom
122	          </Button>
123	          <LogoutButton />
124	          <ThemeToggle />
125	        </div>
126	      </header>
127	
128	      <main className="max-w-4xl mx-auto px-4 lg:px-8 py-10">
129	        {loading && (
130	          <div className="space-y-3">
131	            <Skeleton className="h-8 w-64" />
132	            <Skeleton className="h-4 w-96" />
133	            <Skeleton className="h-32 w-full" />
134	          </div>
135	        )}
136	
137	        {!loading && !assignment && (
138	          <div className="text-center py-20 text-muted-foreground">
139	            Assignment not found.
140	          </div>
141	        )}
142	
143	        {assignment && (
144	          <div className="space-y-6">
145	            <div className="flex items-start justify-between gap-4">
146	              <div className="space-y-2 min-w-0 flex-1">
147	                <h1 className="text-2xl font-semibold text-foreground">
148	                  {assignment.set_title}
149	                </h1>
150	                <StatusBadge status={assignment.status} />
151	              </div>
152	              {assignment.status === "completed" && assignment.score !== null && (
153	                <div className="text-right shrink-0">
154	                  <div className="text-3xl font-light text-emerald-400 tabular-nums">
155	                    {Math.round(assignment.score)}%
156	                  </div>
157	                  <div className="text-[10px] uppercase tracking-[0.2em] text-muted-foreground">
158	                    Score
159	                  </div>
160	                </div>
161	              )}
162	            </div>
163	
164	            {assignment.set_description && (
165	              <div className="rounded-xl bg-card border border-border px-5 py-4">
166	                <p className="text-sm text-muted-foreground leading-relaxed whitespace-pre-wrap">
167	                  {assignment.set_description}
168	                </p>
169	              </div>
170	            )}
171	
172	            <div className="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
173	              <span>
174	                {assignment.question_qids.length} question
175	                {assignment.question_qids.length === 1 ? "" : "s"}
176	              </span>
177	              <span className="flex items-center gap-1.5">
178	                <Clock className="h-3.5 w-3.5" />≈ {estMinutes} min
179	              </span>
180	            </div>
181	
182	            <div>
183	              {assignment.status === "assigned" && (
184	                <Button
185	                  size="lg"
186	                  onClick={handleStart}
187	                  disabled={parentLoading}
188	                  className="gap-2"
189	                >
190	                  <Play className="h-4 w-4" /> {parentSet?.start_button_label || "Start"}
191	                </Button>
192	              )}
193	              {assignment.status === "in_progress" && (
194	                <Button
195	                  size="lg"
196	                  onClick={handleStart}
197	                  disabled={parentLoading}
198	                  className="gap-2"
199	                >
200	                  <Play className="h-4 w-4" /> Continue
201	                </Button>
202	              )}
203	              {assignment.status === "completed" && (
204	                <Button size="lg" variant="outline" onClick={handleStart} className="gap-2">
205	                  <Eye className="h-4 w-4" /> Review
206	                </Button>
207	              )}
208	            </div>
209	          </div>
210	        )}
211	      </main>
212	    </div>
213	  );
214	}
215	

## user

Tool result:
1	import * as React from "react";
2	import { useNavigate, useSearchParams } from 'react-router-dom';
3	import { useAuth } from '@/contexts/AuthContext';
4	import { useUserPermissions } from '@/hooks/useUserPermissions';
5	import { AdminQuestionNotes } from '@/components/drill/AdminQuestionNotes';
6	import { useUserSettings } from '@/contexts/UserSettingsContext';
7	import { Button } from '@/components/ui/button';
8	import { Card } from '@/components/ui/card';
9	import { Badge } from '@/components/ui/badge';
10	import { Progress } from '@/components/ui/progress';
11	import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
12	import { Label } from '@/components/ui/label';
13	import OfficialDrillFrame from '@/components/drill/official/OfficialDrillFrame';
14	import type {
15	  DrawerTab,
16	  DrillDetailsMeta,
17	  DrillSimilarContext,
18	} from '@/components/drill/official/DrillNotesPanel';
19	import type { DrillExplanationContext } from '@/components/drill/official/DrillExplanationTab';
20	import {
21	  type InlineChoiceNotes,
22	} from '@/components/drill/official/InlineChoiceExplanation';
23	import { useLrExplanation, type LrStyleKey } from '@/hooks/useLrExplanation';
24	import SectionReviewWalk from '@/components/drill/SectionReviewWalk';
25	import HelpSheet from '@/components/help/HelpSheet';
26	import OfficialSessionStrip from '@/components/drill/official/OfficialSessionStrip';
27	import OfficialDrillToolbar from '@/components/drill/official/OfficialDrillToolbar';
28	import OfficialQuestionPane from '@/components/drill/official/OfficialQuestionPane';
29	import OfficialAnswerNavigator from '@/components/drill/official/OfficialAnswerNavigator';
30	import OfficialSmartDrillBar from '@/components/drill/official/OfficialSmartDrillBar';
31	import AnswerOvals from '@/components/drill/official/AnswerOvals';
32	import { TutorChatModal } from '@/components/drill/TutorChatModal';
33	import { resolveTutorLaunch, resolveTutorMode, type TutorMode } from '@/components/drill/tutorBehavior';
34	import { ReviewModal } from '@/components/drill/ReviewModal';
35	import { VoiceCoachChip } from '@/components/drill/VoiceCoachChip';
36	import { VoiceCoachModal } from '@/components/drill/VoiceCoachModal';
37	import { DrillTopBar } from '@/components/drill/DrillTopBar';
38	import { GuidedDrillIntroModal } from '@/components/drill/GuidedDrillIntroModal';
39	import { useHomeworkSet } from '@/hooks/useHomeworkSets';
40	import { HighlightedText } from '@/components/drill/HighlightedText';
41	import { BlindReviewSelection } from '@/components/drill/BlindReviewSelection';
42	import { BlindReviewFlow, type BlindReviewResult as LegacyBlindReviewResult } from '@/components/drill/BlindReviewFlow';
43	import { SectionComplete } from '@/components/drill/SectionComplete';
44	import { ScorePrediction } from '@/components/drill/ScorePrediction';
45	import { ScoreReport } from '@/components/drill/ScoreReport';
46	import { LRSectionResults } from '@/components/drill/LRSectionResults';
47	import { EnhancedBlindReview } from '@/components/drill/EnhancedBlindReview';
48	import { PracticeSetResults } from '@/components/drill/PracticeSetResults';
49	import { TimerProvider, useTimerContextSafe } from '@/contexts/TimerContext';
50	import { useQuestionBank } from '@/contexts/QuestionBankContext';
51	import { useClassId } from '@/hooks/useClassId';
52	import { ErrorBoundary } from '@/components/common/ErrorBoundary';
53	import { questionBank } from '@/lib/questionLoader';
54	import {
55	  buildSectionStats,
56	  logSectionWrongAnswers,
57	  emailSectionReport,
58	  persistSectionResults,
59	  wajQidsForSection,
60	} from '@/lib/sectionHistorySave';
61	import {
62	  clearCloseoutProgress,
63	  closeoutKey,
64	  outstandingWajQids,
65	  recordCloseoutProgress,
66	} from '@/lib/practiceTestCloseout';
67	import { isSittingReturn } from '@/lib/practiceTestRunner';
68	import { useAdaptiveEngine } from '@/contexts/AdaptiveEngineContext';
69	import { normalizeText } from '@/lib/utils';
70	import { captureTextSelection, replaceOverlappingHighlights, type Highlight, type HighlightColor } from '@/lib/highlightUtils';
71	import { Switch } from '@/components/ui/switch';
72	import { setActiveDrillQid } from '@/lib/drillNotepadBus';
73	import { officialLeadCrumbLabel } from '@/lib/officialBreadcrumbs';
74	import { upsertLastActivity, type DrillSnapshot, type SectionSnapshot } from '@/lib/lastActivity';
75	import { getRecentExposureSet, recordExposures } from '@/lib/questionExposure';
76	import { ArrowLeft, CheckCircle, X, XCircle, ChevronLeft, ChevronRight, Pause, Play } from 'lucide-react';
77	import { cn } from '@/lib/utils';
78	import { supabase } from '@/integrations/supabase/client';
79	import { completeLinkedTodo } from '@/lib/todoActions';
80	import type { Json } from '@/integrations/supabase/types';
81	import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip';
82	import {
83	  AlertDialog,
84	  AlertDialogAction,
85	  AlertDialogCancel,
86	  AlertDialogContent,
87	  AlertDialogDescription,
88	  AlertDialogFooter,
89	  AlertDialogHeader,
90	  AlertDialogTitle,
91	} from '@/components/ui/alert-dialog';
92	import type { LRQuestion } from '@/lib/questionLoader';
93	import type {
94	  BlindReviewResult as DrillBlindReviewResult,
95	  DrillMode,
96	  DrillSession,
97	  FullSectionConfig,
98	  TimerConfig,
99	  TypeDrillConfig,
100	} from '@/types/drill';
101	import { QuestionPoolService, servesFixedQueue, type QuestionUsage } from '@/lib/questionPoolService';
102	import { QuestionPoolChip } from '@/components/drill/QuestionPoolChip';
103	import { QuestionPoolExhausted } from '@/components/drill/QuestionPoolExhausted';
104	import { toast } from 'sonner';
105	import { QuestionTimer } from '@/lib/questionTimer';
106	import { record } from '@rrweb/record';
107	import type { eventWithTime } from '@rrweb/types';
108	import { timerConfigForRunSpec } from '@/lib/drillRunSpec';
109	import { useDrillRunSpec } from '@/components/drill/DrillRunSpecContext';
110	import { closeOutAssignedSection } from '@/lib/closeOutAssignedSection';
111	import { getDrillDisplayNumber } from '@/pages/drillDisplayNumber';
112	import { getPracticePool } from '@/bootcamps/main-conclusion/data/practiceDrillPools';
113	import { recordPracticeDrillCompletion } from '@/bootcamps/main-conclusion/lib/recordPracticeCompletion';
114	import {
115	  loadPracticeSession,
116	  savePracticeSessionSnapshot,
117	  completePracticeSession,
118	  type PracticeSessionSnapshot,
119	} from '@/bootcamps/main-conclusion/lib/practiceSessionStore';
120	import { recordFlawPerformance } from '@/bootcamps/fallacy-flaw-v2/lib/recordFlawPerformance';
121	import { appendGuidedResumeParams } from '@/lib/guidedDrillNavigation';
122	import { DrillSplit } from '@/components/drill/DrillSplit';
123	import {
124	  guidedSessionKeyForRunner,
125	  guidedResumeIndex,
126	  loadGuidedDrillSession,
127	  saveGuidedDrillSnapshot,
128	  completeGuidedDrillSession,
129	  isResumableGuidedSession,
130	} from '@/lib/guidedDrillSession';
131	import {
132	  drillResumeKey,
133	  loadDrillResumeSession,
134	  saveDrillResumeSnapshot,
135	  completeDrillResumeSession,
136	  isResumableDrillSession,
137	} from '@/lib/drillResumeSession';
138	
139	
140	/**
141	 * The clock a full section was started under, in milliseconds. Unlimited has
142	 * no budget, which is not the same as a budget of zero.
143	 */
144	function sectionBudgetMs(timer?: TimerConfig): number | undefined {
145	  if (!timer) return undefined;
146	  switch (timer.mode) {
147	    case '35':
148	      return 35 * 60 * 1000;
149	    case '52.5':
150	      return 52.5 * 60 * 1000;
151	    case '70':
152	      return 70 * 60 * 1000;
153	    case 'custom':
154	      return timer.customMinutes ? timer.customMinutes * 60 * 1000 : undefined;
155	    default:
156	      return undefined;
157	  }
158	}
159	
160	function DrillContent() {
161	  const adaptiveEngine = useAdaptiveEngine();
162	  const navigate = useNavigate();
163	  const [searchParams] = useSearchParams();
164	  const { user } = useAuth();
165	  // Depend on the id, never the user object: Supabase hands out a fresh object
166	  // on every token refresh, and effects keyed on the object re-run for no reason.
167	  const userId = user?.id;
168	  // Teaching notes under the question are an admin surface. The panel stays
169	  // open across questions once opened, so a teaching pass is one click, not ten.
170	  const { is_admin: isAdmin } = useUserPermissions();
171	  const [teachingNotesOpen, setTeachingNotesOpen] = React.useState(false);
172	  const { settings } = useUserSettings();
173	  const permissions = useUserPermissions();
174	  const { isLoading: qbLoading } = useQuestionBank();
175	
176	  // Everything about the run itself comes from the Drill Run Spec, which the
177	  // gate in front of this page built from the launch in the address bar. The
178	  // runner does not parse the query string for it: one grammar, one reader.
179	  const state = useDrillRunSpec();
180	  const assignmentId = state.assignmentId ?? null;
181	  const guidedAssignmentId = state.guidedAssignmentId ?? null;
182	  const guidedDrillId = state.guidedDrillId ?? null;
183	  const guidedSetId = state.guidedSetId;
184	  const { set: guidedSet } = useHomeworkSet(guidedSetId);
185	  const [guidedInfoOpen, setGuidedInfoOpen] = React.useState(false);
186	
187	  const practicingLabel = state.practicingLabel;
188	
189	  // Context params for header/breadcrumbs (survive refresh)
190	  const origin = searchParams.get('origin');
191	  const returnTo = searchParams.get('returnTo');
192	  const drillReturnTo = state.returnTo ?? (returnTo && returnTo.startsWith('/') && !returnTo.startsWith('//') ? returnTo : undefined);
193	  // Which run and leg this section belongs to, when it belongs to one. Comes
194	  // from the launch rather than from returnTo: that string is a routing hint
195	  // and nothing load-bearing may depend on it. A refreshed leg used to lose
196	  // these and then had nothing to write its close-out against, so the section
197	  // could never be marked finished and the practice test stayed open forever.
198	  const ptRun = state.ptRun;
199	  // Routing and score-UI suppression only. Never a clock or integrity decision.
200	  const inSitting = isSittingReturn(drillReturnTo);
201	  /**
202	   * Answer and Explanation are not rendered at all for this run.
203	   *
204	   * Two runs are sealed. A practice-test sitting, because a sitting reveals
205	   * nothing until it is scored and the old per-question gate quietly broke
206	   * that: attempt a question inside a sitting and the reveal unlocked. And a
207	   * run launched `?sealed=1`, which is how an assigned section is handed over.
208	   *
209	   * The full-section gate further down is a different and weaker thing. It
210	   * withholds the reveal until the question is attempted and then allows it.
211	   * That is right for a section a student chose to sit; it is wrong for one
212	   * assigned as a measurement, where the answer to question 3 must not be
213	   * available while question 4 is still open.
214	   */
215	  const revealSealed = inSitting || !!state.sealed;
216	  const contextLabel = searchParams.get('label');
217	  const contextFocus = searchParams.get('focus');
218	  // Kept as a string: `?initialIndex=0` is a real request to open on the first
219	  // question, and a number would read as absent.
220	  const initialIndexParam = state.initialIndex != null ? String(state.initialIndex) : null;
221	  const isMcPractice = state.practiceSource === 'intro-to-lr-practice-drills';
222	  // Maps the finished MC practice set back to its module-progress completion id
223	  // so the Intro to LR path cannot report "core path cleared" before the final
224	  // practice sets are actually done.
225	  const mcPracticePool = React.useMemo(
226	    () => (isMcPractice ? getPracticePool(state.practiceSlug ?? '') : undefined),
227	    [isMcPractice, state.practiceSlug],
228	  );
229	  // Once the set is finished, snapshot writes must stop: a late write would
230	  // flip the stored row back to in_progress and re-offer "Resume" on a set the
231	  // student already completed.
232	  const mcPracticeFinalizedRef = React.useRef(false);
233	  // Guided drills keep the same kind of durable resume row, keyed by assignment.
234	  // Null for every other drill surface, which is what leaves library, flagged,
235	  // and Smart Drill runs untouched.
236	  const guidedSessionKey = React.useMemo(
237	    () => guidedSessionKeyForRunner({ guidedAssignmentId, guidedDrillId, returnTo }),
238	    [guidedAssignmentId, guidedDrillId, returnTo],
239	  );
240	  const guidedLegacySessionKey = React.useMemo(
241	    () =>
242	      guidedDrillId && !guidedAssignmentId
243	        ? guidedSessionKeyForRunner({ returnTo })
244	        : null,
245	    [guidedDrillId, guidedAssignmentId, returnTo],
246	  );
247	  // Same reason as mcPracticeFinalizedRef: once the drill is finished, a late
248	  // snapshot write would flip the row back to in_progress and offer a resume on
249	  // a drill the student already completed.
250	  const guidedFinalizedRef = React.useRef(false);
251	  const genericResumeIdentity = state.resumeIdentity;
252	  // Every remaining drill surface — Smart Drill, custom type drills, full
253	  // sections — gets the same durable resume row, so closing the browser or
254	  // signing out mid-drill is never a loss. Null while the guided/practice-set
255	  // surfaces own the run, so the three can never write over each other.
256	  const genericResumeKey = React.useMemo(() => {
257	    if (isMcPractice || guidedSessionKey) return null;
258	    if (!state?.mode) return null;
259	    const mode = state.mode === 'practice-set' ? 'type-drill' : state.mode;
260	    return drillResumeKey({ mode, config: state.config, identity: genericResumeIdentity });
261	  }, [isMcPractice, guidedSessionKey, state, genericResumeIdentity]);
262	  // Rows written before a bootcamp day had its own identity were named by the
263	  // picked question list. Read that key only when the day-keyed row is absent;
264	  // every new snapshot and completion still writes the day-keyed row.
265	  const genericLegacyResumeKey = React.useMemo(() => {
266	    if (!genericResumeIdentity || !state?.mode) return null;
267	    const mode = state.mode === 'practice-set' ? 'type-drill' : state.mode;
268	    return drillResumeKey({ mode, config: state.config });
269	  }, [genericResumeIdentity, state]);
270	  const genericFinalizedRef = React.useRef(false);
271	
272	  const bootcampPracticeReturnTo =
273	    returnTo && returnTo.startsWith('/') && !returnTo.startsWith('//')
274	      ? returnTo
275	      : '/bootcamp/intro-to-lr/practice-drills';
276	
277	  React.useEffect(() => {
278	    if (!user) navigate('/auth');
279	  }, [user, navigate]);
280	
281	  // ── Force dark mode: drilling pages always use the dark reading surface ──
282	  React.useEffect(() => {
283	    const root = document.documentElement;
284	    const wasLight = root.classList.contains('light');
285	    root.classList.remove('light');
286	    return () => {
287	      if (wasLight) root.classList.add('light');
288	    };
289	  }, []);
290	
291	  // ── rrweb: start recording on mount, stop on unmount ──
292	  React.useEffect(() => {
293	    const stop = record({
294	      emit: (event) => { eventsRef.current.push(event); },
295	      sampling: { mousemove: 50, scroll: 150, input: 'last' },
296	      recordCanvas: false,
297	      collectFonts: false,
298	    });
299	    stopRecordingRef.current = stop ?? null;
300	    return () => {
301	      stopRecordingRef.current?.();
302	      stopRecordingRef.current = null;
303	      eventsRef.current = [];
304	    };
305	  }, []);
306	
307	  const [session, setSession] = React.useState<DrillSession | null>(null);
308	  const [currentQuestion, setCurrentQuestion] = React.useState<LRQuestion | null>(null);
309	  const [selectedAnswer, setSelectedAnswer] = React.useState<string>('');
310	  const [showSolution, setShowSolution] = React.useState(false);
311	  const [tutorChatOpen, setTutorChatOpen] = React.useState(false);
312	  // The authored LSAT Lab explanation. Distinct from the AI tutor: this shows
313	  // transcribed source content, the tutor generates. Authored wins when it
314	  // exists; the tutor is the fallback for questions that have none. It renders
315	  // in two places — the drawer's Explanation tab (question-level) and inline
316	  // under each choice — so the chosen style is owned here and shared, because
317	  // the drawer itself is mounted twice by the frame.
318	  const [activeStyle, setActiveStyle] = React.useState<LrStyleKey | null>(null);
319	  // Questions the student revealed before attempting. Not scored: the answer is
320	  // already on screen, so committing it would be meaningless.
321	  const [unscoredQids, setUnscoredQids] = React.useState<Set<string>>(new Set());
322	  // Confirm shown when Answer is pressed before an attempt.
323	  const [revealConfirmOpen, setRevealConfirmOpen] = React.useState(false);
324	  // Which pill opened the unscored-reveal confirm, so "Show me" finishes the
325	  // job that was actually asked for: Answer reveals in place, Explanation
326	  // reveals and brings the drawer with it.
327	  const [pendingRevealIntent, setPendingRevealIntent] =
328	    React.useState<'answer' | 'explanation'>('answer');
329	  // Help sheet, opened from the header strip beside Pause. The global
330	  // FloatingHelpButton is suppressed on /drill so no bubble floats over the
331	  // question card.
332	  const [helpOpen, setHelpOpen] = React.useState(false);
333	  // Section mode's opt-in reveal, shown on the section navigator. Off by
334	  // default and deliberately not persisted: a real section shows nothing, and
335	  // that stays the default every time.
336	  const [sectionRevealEnabled, setSectionRevealEnabled] = React.useState(false);
337	  const [tutorQuestionSnapshot, setTutorQuestionSnapshot] = React.useState<LRQuestion | null>(null);
338	  const [tutorUserAnswerSnapshot, setTutorUserAnswerSnapshot] = React.useState<string>('');
339	  const [tutorChatMode, setTutorChatMode] = React.useState<TutorMode>('pre-answer');
340	  // Which tab the unified tutor panel opens on (undefined → derived from mode).
341	  const [tutorInitialTab, setTutorInitialTab] = React.useState<'coach' | 'breakdown' | 'notes' | undefined>(undefined);
342	  const [wajModalOpen, setWajModalOpen] = React.useState(false);
343	  const [voiceCoachOpen, setVoiceCoachOpen] = React.useState(false);
344	  // The "Explain your reasoning" voice chip is shown whenever a solution is
345	  // revealed (answer committed) and no overlay is already open. Derived, not
346	  // stored, so it appears on every reveal path automatically.
347	  const [questionStartTime, setQuestionStartTime] = React.useState(performance.now());
348	  /**
349	   * Where this question's answer trail had got to when the student opened it.
350	   * The per-question clock restarts on every visit, so a question revisited
351	   * after two minutes would otherwise stamp its second answer earlier than its
352	   * first. Carrying the furthest point forward keeps the trail monotonic and
353	   * makes the results timeline read as one run.
354	   */
355	  const trailBaseMs = React.useRef(0);
356	  /**
357	   * The question currently open, and what its answer trail looked like when it
358	   * was opened. Closing the visit compares the two: a visit that ends with the
359	   * trail the same length it started is a second pass that changed nothing,
360	   * which is a finding in its own right and invisible from the trail alone.
361	   */
362	  const openVisit = React.useRef<{ qid: string; trailLength: number } | null>(null);
363	  /**
364	   * Latest eliminations, readable from the visit closer without making it
365	   * depend on state that changes on every cross-off.
366	   */
367	  const eliminatedRef = React.useRef<Map<string, Set<string>>>(new Map());
368	  const [hasTimer, setHasTimer] = React.useState(false);
369	  const [answerLocked, setAnswerLocked] = React.useState(false);
370	  const [eliminatedByQid, setEliminatedByQid] = React.useState<Map<string, Set<string>>>(new Map());
371	  // Kept current for the visit closer, which must not re-subscribe on every
372	  // cross-off just to read the latest set.
373	  eliminatedRef.current = eliminatedByQid;
374	  // Derived: eliminations for the displayed question only (read-only proxy).
375	  // Adaptive Smart Drill can render a currentQuestion outside the queued index.
376	  // Shaped so we can later promote into session.attempts.get(qid).eliminated.
377	  const eliminatedAnswers = React.useMemo<Set<string>>(() => {
378	    const qid = currentQuestion?.qid;
379	    return qid ? eliminatedByQid.get(qid) ?? new Set<string>() : new Set<string>();
380	  }, [eliminatedByQid, currentQuestion?.qid]);
381	  const [highlightMode, setHighlightMode] = React.useState<'none' | 'yellow' | 'pink' | 'orange' | 'underline' | 'erase'>('none');
382	  const [highlights, setHighlights] = React.useState<Map<string, Highlight[]>>(new Map());
383	  const [highlightHistory, setHighlightHistory] = React.useState<Map<string, Highlight[]>[]>([]);
384	  const [isFlagged, setIsFlagged] = React.useState(false);
385	  const [showExitDialog, setShowExitDialog] = React.useState(false);
386	  /**
387	   * Complete Section asks first. A section ends once, and a student who meant
388	   * to press Next should not lose the rest of it to a mis-click — least of all
389	   * silently, with questions still blank and time still on the clock.
390	   */
391	  const [submitConfirmOpen, setSubmitConfirmOpen] = React.useState(false);
392	  /**
393	   * What happens when a section's clock runs out.
394	   *
395	   * Nothing used to: the countdown sat at 0:00 and the student kept going, so
396	   * the score said "sat under 35 minutes" about a section that took an hour.
397	   * Now the buzzer stops the room and asks. Finishing there is the honest
398	   * score; carrying on turns the clock around and counts up, and the results
399	   * screen says which questions were answered on which side of it.
400	   */
401	  const [overtimeState, setOvertimeState] = React.useState<'none' | 'prompt' | 'running'>('none');
402	  const [exitDestination, setExitDestination] = React.useState<string>('/');
403	  const [tutorMode, setTutorMode] = React.useState(true);
404	  const [brMarked, setBrMarked] = React.useState<Set<string>>(new Set());
405	  const [showBRSelection, setShowBRSelection] = React.useState(false);
406	  const [showBRFlow, setShowBRFlow] = React.useState(false);
407	  const [brSelectedQids, setBrSelectedQids] = React.useState<string[]>([]);
408	  const [brResults, setBrResults] = React.useState<DrillBlindReviewResult[]>([]);
409	  const [isRetryAfterWrong, setIsRetryAfterWrong] = React.useState(false);
410	  const [correctExplanation, setCorrectExplanation] = React.useState<string>('');
411	  const [showReviewButton, setShowReviewButton] = React.useState(false);
412	  const [isEndingBootcampPracticeDrill, setIsEndingBootcampPracticeDrill] = React.useState(false);
413	  
414	  // New post-section flow states
415	  const [postSectionScreen, setPostSectionScreen] = React.useState<'predict' | 'complete' | 'review' | 'review-walk' | 'score-report' | null>(null);
416	  /**
417	   * What the student guessed before seeing anything. Held for this sitting only
418	   * and shown beside the real score; nothing persists it, so nothing claims it
419	   * as history.
420	   */
421	  const [predictedScore, setPredictedScore] = React.useState<number | null>(null);
422	  /**
423	   * Which questions blind review walks. Null means the whole section, which is
424	   * what a section's blind review always is. Practice sets set it explicitly,
425	   * because "Review wrong" there is a shortlist by name and should stay one.
426	   */
427	  const [brPassQids, setBrPassQids] = React.useState<string[] | null>(null);
428	  const [longPressTimer, setLongPressTimer] = React.useState<ReturnType<typeof setTimeout> | null>(null);
429	  
430	  // Question pool state
431	  const [poolStatus, setPoolStatus] = React.useState<string>('');
432	  const [totalPoolSize, setTotalPoolSize] = React.useState(0);
433	  const [availablePoolSize, setAvailablePoolSize] = React.useState(0);
434	  const [poolExhausted, setPoolExhausted] = React.useState(false);
435	  const [bootError, setBootError] = React.useState<string | null>(null);
436	  const [adaptiveHydrationStatus, setAdaptiveHydrationStatus] = React.useState<'idle' | 'loading' | 'ready' | 'failed'>('idle');
437	  const { classId, loading: classIdLoading } = useClassId();
438	  const [advanceToken, setAdvanceToken] = React.useState(0);
439	  // Smart Drill: questions skipped (advanced without answering). Excluded from
440	  // the adaptive selector so a skipped question is not immediately re-served.
441	  const [skippedQids, setSkippedQids] = React.useState<Set<string>>(new Set());
442	  // Smart Drill: auto-reveal the correct answer after submitting. Persisted.
443	  const [autoReveal, setAutoReveal] = React.useState<boolean>(() => {
444	    try {
445	      return localStorage.getItem('lsatu.smartdrill.autoReveal') !== 'false';
446	    } catch {
447	      return true;
448	    }
449	  });
450	  const handleAutoRevealChange = React.useCallback((next: boolean) => {
451	    setAutoReveal(next);
452	    try {
453	      localStorage.setItem('lsatu.smartdrill.autoReveal', String(next));
454	    } catch {
455	      /* ignore quota/availability errors */
456	    }
457	  }, []);
458	
459	  const currentViewId = React.useRef<string | null>(null);
460	
461	  // rrweb session replay capture (one row per question in session_replays)
462	  const eventsRef = React.useRef<eventWithTime[]>([]);
463	  const stopRecordingRef = React.useRef<(() => void) | null>(null);
464	  const lastRecordedQidRef = React.useRef<string | null>(null);
465	  const adaptiveCommitInFlightRef = React.useRef<Set<string>>(new Set());
466	
467	  // Homework assignment: dedupe the status='in_progress' write per mount.
468	  const assignmentStartedRef = React.useRef(false);
469	
470	  // Practice-set mode state
471	  const [isPracticeSetMode, setIsPracticeSetMode] = React.useState(false);
472	  const questionTimer = React.useRef(new QuestionTimer());
473	  const [hideTimer, setHideTimer] = React.useState(false);
474	  const [showAnswerRevealed, setShowAnswerRevealed] = React.useState<Map<string, boolean>>(new Map());
475	  // Official-layout-only local UI state (Find Text + Aa font scale).
476	  const [officialSearchTerm, setOfficialSearchTerm] = React.useState('');
477	  const [officialFontScale, setOfficialFontScale] = React.useState(1);
478	  // Smart Drill docked notes panel open state.
479	  const [notesOpen, setNotesOpen] = React.useState(false);
480	  // Active tab inside the docked drill drawer (Notes | Details).
481	  const [drawerTab, setDrawerTab] = React.useState<DrawerTab>('details');
482	  
483	  const timer = useTimerContextSafe();
484	  /**
485	   * Time already spent on a resumed run, waiting for the clock to start. Read
486	   * off the stored row while the session loads and folded in once the timer is
487	   * running, because the provider's duration is fixed at mount and cannot know
488	   * about a resume that had not been read yet.
489	   */
490	  const pendingResumeElapsedMs = React.useRef<number | null>(null);
491	
492	  // BR only for Full Section and Type Drill modes
493	  const sessionMode = session?.mode;
494	  // Blind review is a review affordance, and a sitting reveals nothing between
495	  // sections, so its selection and flow screens must not appear mid-sitting.
496	  const brEnabled =
497	    (sessionMode === 'full-section' || sessionMode === 'type-drill') && !inSitting;
498	
499	  // class_id resolved via useClassId() hook above (F1.10).
500	
501	  // Guards the session initializer against re-entry. The effect below builds the
502	  // run once per drill launch; anything that re-fires it afterwards (a Supabase
503	  // TOKEN_REFRESHED handing React a new `user` object, a settings write) used to
504	  // re-hydrate from the stored resume row and silently jump the student forward
505	  // to their furthest-answered question. Mid-lesson that reads as the page
506	  // skipping on its own. The key is the identity of the run, not of the user.
507	  const sessionInitKeyRef = React.useRef<string | null>(null);
508	
509	  // Initialize session with question pool filtering
510	  React.useEffect(() => {
511	    if (!state?.mode) {
512	      navigate('/classroom');
513	      return;
514	    }
515	
516	    const initializeSession = async () => {
517	      // Wait until the class_id fetch has completed before attempting to build
518	      // the session.  Without this guard the effect fires twice: once on mount
519	      // (classId === '') and again when classId resolves, wiping any in-progress
520	      // answers and causing a premature "could not resolve your class" toast.
521	      if (classIdLoading) return;
522	      if (qbLoading) return;
523	
524	      // One initialization per (launch state, user, resume target). Once the
525	      // run is live, a repeat firing is a no-op rather than a reset.
526	      const initKey = JSON.stringify([
527	        state.mode,
528	        userId ?? null,
529	        classId,
530	        guidedSessionKey ?? null,
531	        genericResumeKey ?? null,
532	        mcPracticePool?.slug ?? null,
533	        initialIndexParam ?? null,
534	      ]);
535	      if (sessionInitKeyRef.current === initKey) return;
536	      sessionInitKeyRef.current = initKey;
537	
538	      const mode = state.mode === 'practice-set' ? 'type-drill' : state.mode;
539	      let questionQueue: string[] = [];
540	      let rawQuestions: LRQuestion[] = [];
541	
542	      if (mode === 'adaptive') {
543	        rawQuestions = questionBank.getAllQuestions();
544	      } else if (mode === 'full-section' && state.config) {
545	        const config = state.config as FullSectionConfig;
546	        rawQuestions = questionBank.getSection(config.pt, config.section);
547	        setHasTimer(config.timer.mode !== 'unlimited');
548	      } else if (mode === 'natural-drill' && state.config) {
549	        const config = state.config as TypeDrillConfig;
550	        rawQuestions = config.selectedQids
551	          ?.map(qid => questionBank.getQuestion(qid))
552	          .filter((q): q is LRQuestion => !!q) ?? [];
553	      } else if (mode === 'type-drill' && state.config) {
554	        const config = state.config as TypeDrillConfig;
555	        
556	        // Detect practice-set mode (Build-a-Set)
557	        if (config.selectedQids && config.selectedQids.length > 0) {
558	          setIsPracticeSetMode(true);
559	          setHasTimer(true); // Guided drills use their configured countdown; other fixed queues use stopwatch.
560	          rawQuestions = config.selectedQids
561	            .map(qid => questionBank.getQuestion(qid))
562	            .filter(Boolean) as LRQuestion[];
563	        } else {
564	          // Otherwise, filter by criteria
565	          rawQuestions = questionBank.getQuestionsByFilter({
566	            qtypes: config.qtypes.length > 0 ? config.qtypes : undefined,
567	            difficulties: config.difficulties.length > 0 ? config.difficulties : undefined,
568	            pts: config.pts.length > 0 ? config.pts : undefined,
569	            sections: config.sections && config.sections.length > 0 ? config.sections : undefined,
570	            qfeatures: config.qfeatures && config.qfeatures.length > 0 ? config.qfeatures : undefined,
571	            reasoningTypes:
572	              config.reasoningTypes && config.reasoningTypes.length > 0
573	                ? config.reasoningTypes
574	                : undefined,
575	            searchQuery: config.searchQuery,
576	            questionNumber: config.questionNumber,
577	          });
578	        }
579	      }
580	
581	      // Apply question pool filtering only if classId is available
582	      let available = rawQuestions;
583	      let exhausted = false;
584	      
585	      // A section is served whole or not at all. Pool dedupe used to run for
586	      // every mode, so a full section silently lost any question the student
587	      // had already met in a drill — PT103.S1 handed over 25 of its 26 with
588	      // nothing on screen to say one was missing.
589	      const fixedQueue = servesFixedQueue(
590	        mode,
591	        state.config as { selectedQids?: string[] } | null,
592	      );
593	
594	      if (classId && !fixedQueue) {
595	        // Dedupe read can fail (RLS/transport). Don't block the drill: fall back
596	        // to an empty usage map (repeats possible) but tell the student why.
597	        let usage: Map<string, QuestionUsage> = new Map();
598	        try {
599	          usage = await QuestionPoolService.getQuestionUsage(classId, mode);
600	        } catch (err) {
601	          console.error('Failed to load question history for dedupe:', err);
602	          toast.error("Couldn't check your question history; some questions may repeat.");
603	        }
604	        const typeDrillConfig = mode === 'type-drill' ? (state.config as TypeDrillConfig) : null;
605	        const poolSettings = {
606	          allowRepeats: typeDrillConfig?.unseen_only ? false : settings.allowRepeats,
607	          preferUnseen: typeDrillConfig?.unseen_only ? true : settings.preferUnseen,
608	          recycleAfterDays: settings.recycleAfterDays
609	        };
610	
611	        const filtered = QuestionPoolService.filterQuestionPool(
612	          rawQuestions,
613	          usage,
614	          poolSettings
615	        );
616	        
617	        available = filtered.available;
618	        exhausted = filtered.exhausted;
619	
620	        setTotalPoolSize(rawQuestions.length);
621	        setAvailablePoolSize(available.length);
622	        setPoolExhausted(exhausted);
623	        setPoolStatus(QuestionPoolService.getPoolStatus(rawQuestions.length, available.length, poolSettings));
624	
625	        if (exhausted) {
626	          // Don't initialize session if pool is exhausted — surface the
627	          // reason so the render layer can show a real message instead of
628	          // the misleading "Session Complete / Loading…" card.
629	          setBootError(
630	            "You've already practiced every available question for this drill type. Adjust your drill settings or come back after recycle."
631	          );
632	          return;
633	        }
634	      }
635	
636	      if (rawQuestions.length === 0) {
637	        setBootError(
638	          "The question bank hasn't loaded any questions for this drill. Try refreshing or contact support if this persists."
639	        );
640	        return;
641	      }
642	
643	      // For type-drill, apply balanced selection from available pool (only if not pre-selected)
644	      let finalQuestions = available;
645	      if (mode === 'type-drill' && state.config) {
646	        const config = state.config as TypeDrillConfig;
647	        
648	        // Skip pool filtering if questions were pre-selected
649	        if (config.selectedQids && config.selectedQids.length > 0) {
650	          finalQuestions = available; // Use them directly
651	        } else {
652	          // Balanced mix: group by type × level, round-robin select
653	          const groups = new Map<string, LRQuestion[]>();
654	          
655	          for (const q of available) {
656	            const key = `${q.qtype}-${q.difficulty}`;
657	            if (!groups.has(key)) groups.set(key, []);
658	            groups.get(key)!.push(q);
659	          }
660	          
661	          // Shuffle each group
662	          for (const [, questions] of groups) {
663	            for (let i = questions.length - 1; i > 0; i--) {
664	              const j = Math.floor(Math.random() * (i + 1));
665	              [questions[i], questions[j]] = [questions[j], questions[i]];
666	            }
667	          }
668	          
669	          // Round-robin select
670	          const selected: LRQuestion[] = [];
671	          const groupArrays = Array.from(groups.values());
672	          
673	          while (selected.length < config.count && groupArrays.some(g => g.length > 0)) {
674	            for (const group of groupArrays) {
675	              if (group.length > 0 && selected.length < config.count) {
676	                selected.push(group.shift()!);
677	              }
678	            }
679	          }
680	          
681	          // Final shuffle for variety
682	          for (let i = selected.length - 1; i > 0; i--) {
683	            const j = Math.floor(Math.random() * (i + 1));
684	            [selected[i], selected[j]] = [selected[j], selected[i]];
685	          }
686	          
687	          finalQuestions = selected;
688	        }
689	      }
690	
691	      questionQueue = finalQuestions.map(q => q.qid);
692	
693	      const requestedInitialIndex = initialIndexParam ? Number.parseInt(initialIndexParam, 10) : 0;
694	      let initialIndex = Number.isFinite(requestedInitialIndex)
695	        ? Math.min(Math.max(requestedInitialIndex, 0), Math.max(questionQueue.length - 1, 0))
696	        : 0;
697	      let restoredAttempts: DrillSession['attempts'] = new Map();
698	      // Set only when a stored section had already run out of time.
699	      let restoredRegulationMark: DrillSession['regulationMark'] | undefined;
700	
701	      // Intro to LR practice sets resume from durable storage, not from the URL.
702	      // A student who closed the tab, signed out, or moved to another device
703	      // comes back to the question they stopped on with every prior answer
704	      // still marked answered in the navigator.
705	      if (isMcPractice && mcPracticePool && user) {
706	        const stored = await loadPracticeSession(user.id, mcPracticePool.slug);
707	        const sameSet =
708	          !!stored &&
709	          stored.status === 'in_progress' &&
710	          stored.question_queue.length === questionQueue.length &&
711	          stored.question_queue.every((qid) => questionQueue.includes(qid));
712	
713	        if (stored && sameSet) {
714	          questionQueue = stored.question_queue;
715	          initialIndex = Math.min(
716	            Math.max(stored.current_index, 0),
717	            Math.max(questionQueue.length - 1, 0),
718	          );
719	          for (const attempt of stored.attempts) {
720	            restoredAttempts.set(attempt.qid, {
721	              selectedAnswer: attempt.selected_answer,
722	              correct: attempt.correct,
723	              timeMs: attempt.time_ms,
724	              timestamp: Date.now(),
725	              confidence: undefined,
726	              reviewDone: false,
727	              // The record, not just the answer. A resumed run used to come
728	              // back flattened: no changes of mind, no marks for review.
729	              switchCount: attempt.switch_count,
730	              brMarked: attempt.flagged,
731	              answerTrail: attempt.answer_trail?.map((e) => ({
732	                answer: e.answer,
733	                atMs: e.at_ms,
734	              })),
735	            });
736	          }
737	        } else if (stored && !sameSet && stored.status === 'in_progress') {
738	          // The frozen pool changed under a saved run. Starting clean is the
739	          // only honest option; say so rather than silently dropping answers.
740	          console.warn('[drill:mc-practice] stored resume set no longer matches pool, starting fresh', {
741	            slug: mcPracticePool.slug,
742	          });
743	        }
744	      }
745	
746	      // Guided drills resume the same way, and for the same reason: leaving a
747	      // drill and coming back must return the student to the question they
748	      // stopped on with their earlier answers intact, not to a fresh shuffle.
749	      if (guidedSessionKey && user) {
750	        const stored = await loadGuidedDrillSession(
751	          user.id,
752	          guidedSessionKey,
753	          guidedLegacySessionKey,
754	        );
755	        if (isResumableGuidedSession(stored, questionQueue)) {
756	          questionQueue = stored.question_queue;
757	          initialIndex = guidedResumeIndex(
758	            questionQueue,
759	            stored.current_index,
760	            stored.attempts.map((a) => a.qid),
761	          );
762	          for (const attempt of stored.attempts) {
763	            restoredAttempts.set(attempt.qid, {
764	              selectedAnswer: attempt.selected_answer,
765	              correct: attempt.correct,
766	              timeMs: attempt.time_ms,
767	              timestamp: Date.now(),
768	              confidence: undefined,
769	              reviewDone: false,
770	              // The record, not just the answer. A resumed run used to come
771	              // back flattened: no changes of mind, no marks for review.
772	              switchCount: attempt.switch_count,
773	              brMarked: attempt.flagged,
774	              answerTrail: attempt.answer_trail?.map((e) => ({
775	                answer: e.answer,
776	                atMs: e.at_ms,
777	              })),
778	            });
779	          }
780	        } else if (stored?.status === 'in_progress') {
781	          console.warn('[drill:guided] stored resume set no longer matches this drill, starting fresh', {
782	            key: guidedSessionKey,
783	          });
784	        }
785	      }
786	
787	      // Smart Drill, custom type drills and full sections. These are drawn
788	      // fresh on every launch, so the stored queue IS the run: adopt it whole
789	      // rather than comparing it to a new shuffle, or the student loses the
790	      // questions they already answered. An explicit ?initialIndex wins, since
791	      // that is someone deliberately jumping to a question.
792	      if (genericResumeKey && user && !initialIndexParam) {
793	        const stored = await loadDrillResumeSession(
794	          user.id,
795	          genericResumeKey,
796	          genericLegacyResumeKey,
797	        );
798	        if (isResumableDrillSession(stored)) {
799	          // Come back on the clock they left. A timed section that resumed
800	          // with a fresh 35:00 was handing back time already spent, which
801	          // makes the score it produces meaningless.
802	          if (stored?.elapsed_ms) pendingResumeElapsedMs.current = stored.elapsed_ms;
803	          if (stored?.regulation_answered_qids) {
804	            restoredRegulationMark = { answeredQids: stored.regulation_answered_qids };
805	          }
806	          questionQueue = stored.question_queue;
807	          initialIndex = guidedResumeIndex(
808	            questionQueue,
809	            stored.current_index,
810	            stored.attempts.map((a) => a.qid),
811	          );
812	          for (const attempt of stored.attempts) {
813	            restoredAttempts.set(attempt.qid, {
814	              selectedAnswer: attempt.selected_answer,
815	              correct: attempt.correct,
816	              timeMs: attempt.time_ms,
817	              timestamp: Date.now(),
818	              confidence: undefined,
819	              reviewDone: false,
820	              // The record, not just the answer. A resumed run used to come
821	              // back flattened: no changes of mind, no marks for review.
822	              switchCount: attempt.switch_count,
823	              brMarked: attempt.flagged,
824	              answerTrail: attempt.answer_trail?.map((e) => ({
825	                answer: e.answer,
826	                atMs: e.at_ms,
827	              })),
828	            });
829	          }
830	        }
831	      }
832	
833	
834	      setSession({
835	        mode,
836	        regulationMark: restoredRegulationMark,
837	        fullSectionConfig: mode === 'full-section' ? (state.config as FullSectionConfig) : undefined,
838	        typeDrillConfig: (mode === 'type-drill' || mode === 'natural-drill') ? (state.config as TypeDrillConfig) : undefined,
839	        questionQueue,
840	        currentIndex: initialIndex,
841	        attempts: restoredAttempts,
842	      });
843	    };
844	
845	    initializeSession();
846	  }, [state, navigate, classId, classIdLoading, qbLoading, settings.allowRepeats, settings.preferUnseen, settings.recycleAfterDays, initialIndexParam, isMcPractice, mcPracticePool, guidedSessionKey, guidedLegacySessionKey, genericResumeKey, genericLegacyResumeKey, userId]);
847	
848	  // Shapes the student's current place into a resume snapshot. Shared by the two
849	  // surfaces that persist one — Intro to LR practice sets and guided drills — and
850	  // written on every answer and every question move, so leaving mid-drill is
851	  // never a loss. The persistence layer writes locally at once and debounces the
852	  // cloud upsert, so this stays cheap enough to run on each session change.
853	  /**
854	   * How much of the section clock has been spent, right now.
855	   *
856	   * A countdown reports what is left, so the spend is the budget minus that; a
857	   * stopwatch already reports the spend. Null when there is no clock at all,
858	   * which is the difference between "no time used" and "no time to use".
859	   */
860	  const sectionElapsedMs = React.useCallback((): number | undefined => {
861	    if (!timer) return undefined;
862	    if (timer.mode === 'stopwatch') return Math.max(0, Math.round(timer.ms));
863	    const total = sectionBudgetMs(session?.fullSectionConfig?.timer);
864	    if (!total) return undefined;
865	    return Math.max(0, Math.round(total - timer.ms));
866	  }, [timer, session?.fullSectionConfig?.timer]);
867	
868	  const drillResumeSnapshot = React.useCallback(
869	    (source: DrillSession | null): PracticeSessionSnapshot | null => {
870	      if (!source) return null;
871	      return {
872	        questionQueue: source.questionQueue,
873	        currentIndex: source.currentIndex,
874	        attempts: Array.from(source.attempts.entries())
875	          .filter(([, attempt]) => !!attempt.selectedAnswer)
876	          .map(([qid, attempt]) => ({
877	            qid,
878	            selected_answer: attempt.selectedAnswer,
879	            correct: !!attempt.correct,
880	            time_ms: Number.isFinite(attempt.timeMs) ? Math.max(0, Math.round(attempt.timeMs)) : 0,
881	            switch_count: attempt.switchCount ?? 0,
882	            flagged: !!attempt.brMarked,
883	            answer_trail: attempt.answerTrail?.map((e) => ({
884	              answer: e.answer,
885	              at_ms: Math.max(0, Math.round(e.atMs)),
886	            })),
887	          })),
888	        // Stored as time SPENT, so it reads the same whether the surface
889	        // counts down or up.
890	        elapsedMs: sectionElapsedMs(),
891	        regulationAnsweredQids: source.regulationMark?.answeredQids,
892	      };
893	    },
894	    [sectionElapsedMs],
895	  );
896	
897	  /**
898	   * The clock keeps running between answers, and a student can sit on one
899	   * question for five minutes. Snapshots written only on answer changes would
900	   * hand those five minutes back on resume, so a timed section also saves on a
901	   * slow heartbeat. Held in a ref because the snapshot function changes on
902	   * every tick and would otherwise restart the interval each time.
903	   */
904	  const snapshotRef = React.useRef(drillResumeSnapshot);
905	  snapshotRef.current = drillResumeSnapshot;
906	  React.useEffect(() => {
907	    if (!genericResumeKey || !user || !session || !timer) return;
908	    if (genericFinalizedRef.current) return;
909	    if (session.mode !== 'full-section') return;
910	    const id = window.setInterval(() => {
911	      const snapshot = snapshotRef.current(session);
912	      if (!snapshot || snapshot.attempts.length === 0) return;
913	      void saveDrillResumeSnapshot(user.id, genericResumeKey, snapshot).catch((err) => {
914	        console.error('[drill:resume:heartbeat] resume write failed', { err });
915	      });
916	    }, 20_000);
917	    return () => window.clearInterval(id);
918	  }, [genericResumeKey, user, session, timer]);
919	
920	  React.useEffect(() => {
921	    if (!isMcPractice || !mcPracticePool || !user || !session) return;
922	    if (mcPracticeFinalizedRef.current) return;
923	    if (session.questionQueue.length === 0) return;
924	    const snapshot = drillResumeSnapshot(session);
925	    if (!snapshot) return;
926	    void savePracticeSessionSnapshot(user.id, mcPracticePool, snapshot).catch((err) => {
927	      // Non-fatal: the drill still works, they just lose the resume point.
928	      console.error('[drill:mc-practice:snapshot] resume write failed', {
929	        userId: user.id,
930	        slug: mcPracticePool.slug,
931	        err,
932	      });
933	    });
934	  }, [session, isMcPractice, mcPracticePool, user, drillResumeSnapshot]);
935	
936	  // Same snapshot on every answer and every question move for guided drills, so
937	  // the student's place survives a tab close, a sign-out, or another device —
938	  // none of which a URL param can carry.
939	  React.useEffect(() => {
940	    if (!guidedSessionKey || !user || !session) return;
941	    if (guidedFinalizedRef.current) return;
942	    if (session.questionQueue.length === 0) return;
943	    const snapshot = drillResumeSnapshot(session);
944	    if (!snapshot) return;
945	    void saveGuidedDrillSnapshot(user.id, guidedSessionKey, snapshot).catch((err) => {
946	      // Non-fatal: the drill still works, they just lose the resume point.
947	      console.error('[drill:guided:snapshot] resume write failed', {
948	        userId: user.id,
949	        key: guidedSessionKey,
950	        err,
951	      });
952	    });
953	  }, [session, guidedSessionKey, user, drillResumeSnapshot]);
954	
955	  // And the same again for every other drill surface. Only runs with at least
956	  // one answered question are written: an untouched shuffle is not progress,
957	  // and storing it would freeze a stale question order in place.
958	  React.useEffect(() => {
959	    if (!genericResumeKey || !user || !session) return;
960	    if (genericFinalizedRef.current) return;
961	    if (session.questionQueue.length === 0) return;
962	    const snapshot = drillResumeSnapshot(session);
963	    if (!snapshot || snapshot.attempts.length === 0) return;
964	    void saveDrillResumeSnapshot(user.id, genericResumeKey, snapshot).catch((err) => {
965	      // Non-fatal: the drill still works, they just lose the resume point.
966	      console.error('[drill:resume:snapshot] resume write failed', {
967	        userId: user.id,
968	        key: genericResumeKey,
969	        err,
970	      });
971	    });
972	  }, [session, genericResumeKey, user, drillResumeSnapshot]);
973	
974	
975	
976	  // Hydrate adaptive engine from DB before Smart Drill selects its first
977	  // question. If hydration fails, the selector may proceed with current-session
978	  // state only; it must not cold-start merely because the DB read is still in
979	  // flight.
980	  React.useEffect(() => {
981	    if (sessionMode !== 'adaptive') {
982	      setAdaptiveHydrationStatus('idle');
983	      return;
984	    }
985	
986	    if (classIdLoading) {
987	      setAdaptiveHydrationStatus('loading');
988	      return;
989	    }
990	
991	    if (!classId) {
992	      console.warn('[Drill] adaptive hydration skipped: classId unavailable');
993	      setAdaptiveHydrationStatus('failed');
994	      return;
995	    }
996	
997	    let cancelled = false;
998	    const currentHydrationStatus = adaptiveEngine.getHydrationStatus();
999	    setAdaptiveHydrationStatus(currentHydrationStatus === 'idle' ? 'loading' : currentHydrationStatus);
1000	    adaptiveEngine.ensureHydratedFromDB(classId).then(() => {
1001	      if (!cancelled) setAdaptiveHydrationStatus(adaptiveEngine.getHydrationStatus());
1002	    });
1003	
1004	    return () => {
1005	      cancelled = true;
1006	    };
1007	  }, [adaptiveEngine, classId, classIdLoading, sessionMode]);
1008	
1009	  // Homework: mark assignment as in_progress on first question render.
1010	  React.useEffect(() => {
1011	    if (!assignmentId || !session || !currentQuestion || !user || assignmentStartedRef.current) return;
1012	    assignmentStartedRef.current = true;
1013	    (async () => {
1014	      try {
1015	        // eslint-disable-next-line @typescript-eslint/no-explicit-any
1016	        const { error } = await supabase
1017	          .from('homework_assignments')
1018	          .update({ status: 'in_progress', started_at: new Date().toISOString() })
1019	          .eq('id', assignmentId)
1020	          .eq('student_id', user.id)
1021	          .eq('status', 'assigned');
1022	        if (error) throw error;
1023	      } catch (err) {
1024	        console.error('[drill:assignment:start] update failed', {
1025	          userId: user.id,
1026	          assignmentId,
1027	          err,
1028	        });
1029	        // No user-facing toast — drill works regardless. Completion failure is the one we surface.
1030	      }
1031	    })();
1032	  }, [assignmentId, session?.mode, currentQuestion?.qid, user?.id]);
1033	
1034	  // Track question views whenever currentQuestion changes
1035	  React.useEffect(() => {
1036	    if (!currentQuestion || !classId || !session) return;
1037	    // Flush previous question's rrweb events before switching context
1038	    const prevQid = lastRecordedQidRef.current;
1039	    if (prevQid && prevQid !== currentQuestion.qid) {
1040	      flushReplay(prevQid, session.mode);
1041	    }
1042	    lastRecordedQidRef.current = currentQuestion.qid;
1043	    currentViewId.current = null;
1044	    QuestionPoolService.trackQuestionView(currentQuestion.qid, classId, session.mode).then(id => {
1045	      currentViewId.current = id;
1046	    });
1047	  }, [currentQuestion?.qid, classId, session?.mode]);
1048	
1049	  // Publish active qid for the floating drill notepad (per-question notes).
1050	  React.useEffect(() => {
1051	    setActiveDrillQid(currentQuestion?.qid ?? null);
1052	    return () => setActiveDrillQid(null);
1053	  }, [currentQuestion?.qid]);
1054	
1055	  // Persist "last activity" so the classroom Resume CTA can reopen at exact
1056	  // index. Fires whenever the user lands on a new question OR completes one
1057	  // (attempts.size grows). The service throws on DB failure; we surface as a
1058	  // toast (one-shot per failure) rather than silently swallowing.
1059	  const lastActivityAttemptsRef = React.useRef<number>(-1);
1060	  const lastActivityIndexRef = React.useRef<number>(-1);
1061	  React.useEffect(() => {
1062	    if (!user?.id || !session || !currentQuestion) return;
1063	    const attemptCount = session.attempts.size;
1064	    // Skip the very first render of a fresh session (currentIndex 0, no
1065	    // attempts) — that's not "resumable progress" yet.
1066	    if (attemptCount === 0 && session.currentIndex === 0) return;
1067	    if (lastActivityAttemptsRef.current === attemptCount && session.currentIndex === lastActivityIndexRef.current) {
1068	      return;
1069	    }
1070	    lastActivityAttemptsRef.current = attemptCount;
1071	    lastActivityIndexRef.current = session.currentIndex;
1072	
1073	    const isSection = session.mode === 'full-section';
1074	    const prettyMode = isSection
1075	      ? 'Section'
1076	      : session.mode === 'type-drill'
1077	      ? 'Custom Drill'
1078	      : session.mode === 'natural-drill'
1079	      ? 'Smart Drill'
1080	      : 'Drill';
1081	    const snapshot: DrillSnapshot | SectionSnapshot = isSection
1082	      ? {
1083	          kind: 'section',
1084	          pt: currentQuestion.pt,
1085	          section_number: currentQuestion.section,
1086	          qids: session.questionQueue,
1087	          current_qid: currentQuestion.qid,
1088	          current_index: session.currentIndex,
1089	          label: `PT ${currentQuestion.pt} Section ${currentQuestion.section} Q${currentQuestion.qnum}`,
1090	        }
1091	      : {
1092	          kind: 'drill',
1093	          mode: session.mode,
1094	          qids: session.questionQueue,
1095	          current_index: session.currentIndex,
1096	          current_qid: currentQuestion.qid,
1097	          assignment_id: assignmentId ?? undefined,
1098	          label: `${prettyMode} — PT ${currentQuestion.pt} Q${currentQuestion.qnum}`,
1099	        };
1100	    (async () => {
1101	      try {
1102	        await upsertLastActivity(user.id, snapshot);
1103	      } catch (e) {
1104	        console.error('[Drill] upsertLastActivity failed', e);
1105	        toast.error("Couldn't save your place. Resume may be out of date.");
1106	      }
1107	    })();
1108	  }, [user?.id, session?.mode, session?.currentIndex, session?.attempts.size, currentQuestion?.qid, currentQuestion?.pt, currentQuestion?.section, currentQuestion?.qnum, assignmentId]);
1109	
1110	  // Adaptive mode: select next question only when advanceToken changes.
1111	  // SELECTOR LAYER ONLY — no rendering changes. Pre-filters the question
1112	  // pool against the user's most-recent-500 exposures (Wave 3A), then writes
1113	  // the picked qid back to question_exposures so subsequent picks see it.
1114	  React.useEffect(() => {
1115	    if (!session || session.mode !== 'adaptive') return;
1116	    if (adaptiveHydrationStatus === 'idle' || adaptiveHydrationStatus === 'loading') return;
1117	
1118	    let cancelled = false;
1119	    (async () => {
1120	      let excludedQids = new Set<string>();
1121	      if (user?.id) {
1122	        try {
1123	          excludedQids = await getRecentExposureSet(user.id, 500);
1124	        } catch (e) {
1125	          console.error('[Drill] getRecentExposureSet failed; falling back to no exclusion', e);
1126	        }
1127	      }
1128	      if (cancelled) return;
1129	
1130	      const allQuestions = questionBank.getAllQuestions();
1131	      const sessionAttemptRecords = Array.from(session.attempts.entries()).flatMap(([qid, attempt]) => {
1132	        const q = questionBank.getQuestion(qid);
1133	        if (!q) return [];
1134	        return {
1135	          qid,
1136	          correct: attempt.correct,
1137	          time_ms: attempt.timeMs,
1138	          qtype: q.qtype,
1139	          difficulty: q.difficulty,
1140	          timestamp: new Date(attempt.timestamp),
1141	          reasoningType: q.reasoningType ?? [],
1142	          questionFeatures: q.questionFeatures ?? [],
1143	        };
1144	      });
1145	
1146	      const historicalAttempts = adaptiveEngine.getRecentAttempts();
1147	      const combinedAttempts = [...historicalAttempts, ...sessionAttemptRecords];
1148	      const profile = adaptiveEngine.buildStudentProfile(combinedAttempts);
1149	      const selection = adaptiveEngine.selectSmartDrillQuestion(allQuestions, profile, {
1150	        attempts: combinedAttempts,
1151	        currentSessionUsedQids: new Set([...session.attempts.keys(), ...skippedQids]),
1152	        recentExposureQids: excludedQids,
1153	      });
1154	      const nextQuestion = selection?.question ?? null;
1155	
1156	      if (cancelled) return;
1157	
1158	      if (!nextQuestion) {
1159	        setSession(null);
1160	        setBootError(
1161	          "No new Smart Drill questions are available without repeating recent work. Try a focused drill or come back after more questions are added."
1162	        );
1163	        return;
1164	      }
1165	
1166	      setCurrentQuestion(nextQuestion);
1167	      resetPerQuestionState();
1168	
1169	      // Fire-and-forget exposure write. Service silently skips if the table
1170	      // isn't deployed yet; real errors log + continue (no toast on adaptive
1171	      // pick — would interrupt the student's flow).
1172	      if (user?.id && nextQuestion?.qid) {
1173	        recordExposures(user.id, [nextQuestion.qid]).catch((e) =>
1174	          console.error('[Drill] recordExposures failed', e),
1175	        );
1176	      }
1177	    })();
1178	
1179	    return () => {
1180	      cancelled = true;
1181	    };
1182	  }, [advanceToken, adaptiveHydrationStatus]);
1183	
1184	  // Non-adaptive mode: load question based on session.currentIndex
1185	  React.useEffect(() => {
1186	    if (!session || session.mode === 'adaptive') return;
1187	
1188	    if (session.currentIndex < session.questionQueue.length) {
1189	      const qid = session.questionQueue[session.currentIndex];
1190	      const question = questionBank.getQuestion(qid);
1191	      setCurrentQuestion(question || null);
1192	    } else {
1193	      setCurrentQuestion(null);
1194	    }
1195	
1196	    resetPerQuestionState();
1197	
1198	    // Close the visit we are leaving, then open the one we are entering. Done
1199	    // for every mode: a revisit means the same thing in a drill as in a
1200	    // section, and the record costs one map write.
1201	    if (session) {
1202	      const nextQid = session.questionQueue[session.currentIndex];
1203	      closeOpenVisit();
1204	      if (nextQid) {
1205	        openVisit.current = {
1206	          qid: nextQid,
1207	          trailLength: session.attempts.get(nextQid)?.answerTrail?.length ?? 0,
1208	        };
1209	      }
1210	    }
1211	
1212	    // Restore saved answer + revealed solution for any non-adaptive mode.
1213	    // (Adaptive is narrowed out by prior control flow in this effect.)
1214	    if (session) {
1215	      const qid = session.questionQueue[session.currentIndex];
1216	      // A revisit picks the answer trail up where it left off rather than
1217	      // restarting it at zero.
1218	      const priorTrail = qid ? session.attempts.get(qid)?.answerTrail : undefined;
1219	      trailBaseMs.current = priorTrail?.length ? priorTrail[priorTrail.length - 1].atMs : 0;
1220	      if (qid) {
1221	        const savedAttempt = session.attempts.get(qid);
1222	        if (savedAttempt?.selectedAnswer) {
1223	          setSelectedAnswer(savedAttempt.selectedAnswer);
1224	        }
1225	        if (showAnswerRevealed.get(qid)) {
1226	          setShowSolution(true);
1227	        }
1228	      }
1229	    }
1230	
1231	    // Check if current question is flagged
1232	    checkIfFlagged();
1233	  }, [session?.currentIndex, session?.mode]);
1234	
1235	  // Also trigger initial adaptive selection when session first initializes
1236	  React.useEffect(() => {
1237	    if (
1238	      sessionMode === 'adaptive' &&
1239	      !currentQuestion &&
1240	      (adaptiveHydrationStatus === 'ready' || adaptiveHydrationStatus === 'failed')
1241	    ) {
1242	      setAdvanceToken(t => t + 1);
1243	    }
1244	  }, [sessionMode, currentQuestion, adaptiveHydrationStatus]);
1245	
1246	  /**
1247	   * Bank the visit that is ending.
1248	   *
1249	   * Counts the visit, marks the question as one the student actually opened,
1250	   * and — when the trail is no longer than it was on entry — counts it as a
1251	   * pass that changed nothing. A first visit that produced no answer is not
1252	   * one of those: there was no answer to leave alone.
1253	   */
1254	  const closeOpenVisit = React.useCallback(() => {
1255	    const visit = openVisit.current;
1256	    openVisit.current = null;
1257	    if (!visit) return;
1258	    setSession((prev) => {
1259	      if (!prev) return prev;
1260	      const attempts = new Map(prev.attempts);
1261	      const attempt = attempts.get(visit.qid);
1262	      const trailLength = attempt?.answerTrail?.length ?? 0;
1263	      const changedNothing = trailLength > 0 && trailLength === visit.trailLength;
1264	      if (attempt) {
1265	        const crossedOff = [...(eliminatedRef.current.get(visit.qid) ?? [])];
1266	        attempts.set(visit.qid, {
1267	          ...attempt,
1268	          visitCount: (attempt.visitCount ?? 0) + 1,
1269	          noChangeRevisits: (attempt.noChangeRevisits ?? 0) + (changedNothing ? 1 : 0),
1270	          // Kept rather than discarded with the question: three crossed off and
1271	          // a choice between the last two is the state the webinar says must
1272	          // always be flagged.
1273	          eliminations: crossedOff.length > 0 ? crossedOff : attempt.eliminations,
1274	        });
1275	      }
1276	      const visited = new Set(prev.visitedQids ?? []);
1277	      visited.add(visit.qid);
1278	      return { ...prev, attempts, visitedQids: [...visited] };
1279	    });
1280	  }, []);
1281	
1282	  const resetPerQuestionState = () => {
1283	    setSelectedAnswer('');
1284	    setShowSolution(false);
1285	    setTutorChatOpen(false);
1286	    setTutorQuestionSnapshot(null);
1287	    setTutorUserAnswerSnapshot('');
1288	    setTutorChatMode('pre-answer');
1289	    setVoiceCoachOpen(false);
1290	    setAnswerLocked(false);
1291	    setQuestionStartTime(performance.now());
1292	    setHighlightHistory([]);
1293	    setIsRetryAfterWrong(false);
1294	    setCorrectExplanation('');
1295	    setShowReviewButton(false);
1296	
1297	    // Reset visual timer for Smart Drill and Smart Builder only
1298	    if (session?.mode === 'adaptive' || session?.mode === 'natural-drill') {
1299	      timer?.reset();
1300	      timer?.start();
1301	    }
1302	  };
1303	
1304	  const checkIfFlagged = async () => {
1305	    if (!currentQuestion || !user) {
1306	      setIsFlagged(false);
1307	      return;
1308	    }
1309	    
1310	    try {
1311	      const { data, error } = await supabase
1312	        .from('flagged_questions')
1313	        .select('id')
1314	        .eq('qid', currentQuestion.qid)
1315	        .eq('user_id', user.id)
1316	        .maybeSingle();
1317	      
1318	      if (error && error.code !== 'PGRST116') {
1319	        console.error('Error checking flag status:', error);
1320	      }
1321	      
1322	      setIsFlagged(!!data);
1323	    } catch (err) {
1324	      console.error('Error checking flag:', err);
1325	      setIsFlagged(false);
1326	    }
1327	  };
1328	
1329	  const handleAnswerSelect = (answer: string) => {
1330	    if (!isPracticeSetMode && !isRetryAfterWrong && answerLocked) return;
1331	    if (!tutorMode && showSolution) return;
1332	    
1333	    if (selectedAnswer === answer) {
1334	      setSelectedAnswer('');
1335	      if ((session?.mode === 'full-section' || isPracticeSetMode) && currentQuestion) {
1336	        const newAttempts = new Map(session.attempts);
1337	        newAttempts.delete(currentQuestion.qid);
1338	        setSession({ ...session, attempts: newAttempts });
1339	        
1340	        if (isPracticeSetMode) {
1341	          questionTimer.current.recordAnswer(currentQuestion.qid, '');
1342	        }
1343	      }
1344	    } else {
1345	      setSelectedAnswer(answer);
1346	      if ((session?.mode === 'full-section' || isPracticeSetMode) && currentQuestion) {
1347	        const newAttempts = new Map(session.attempts);
1348	        const existingAttempt = newAttempts.get(currentQuestion.qid);
1349	        // When this choice was made, measured from the start of the question.
1350	        const atMs = Math.max(
1351	          0,
1352	          trailBaseMs.current + Math.floor(performance.now() - questionStartTime),
1353	        );
1354	        const answerTrail = [...(existingAttempt?.answerTrail ?? []), { answer, atMs }];
1355	
1356	        newAttempts.set(currentQuestion.qid, {
1357	          selectedAnswer: answer,
1358	          correct: answer === currentQuestion.correctAnswer,
1359	          timeMs: isPracticeSetMode
1360	            ? questionTimer.current.getTotalTime(currentQuestion.qid)
1361	            : Math.floor(performance.now() - questionStartTime),
1362	          timestamp: Date.now(),
1363	          confidence: existingAttempt?.confidence || null,
1364	          reviewDone: false,
1365	          answerRevealed: existingAttempt?.answerRevealed || false,
1366	          answerTrail,
1367	          // Every entry after the first is a change of mind. Derived here so
1368	          // the count and the trail can never disagree.
1369	          switchCount: Math.max(0, answerTrail.length - 1),
1370	        });
1371	        setSession({ ...session, attempts: newAttempts });
1372	        
1373	        if (isPracticeSetMode) {
1374	          questionTimer.current.recordAnswer(currentQuestion.qid, answer);
1375	        }
1376	      }
1377	    }
1378	  };
1379	
1380	  const handleEliminateAnswer = (key: string) => {
1381	    if (!currentQuestion) return;
1382	    const qid = currentQuestion.qid;
1383	    setEliminatedByQid(prev => {
1384	      const next = new Map(prev);
1385	      const current = new Set(prev.get(qid) ?? []);
1386	      if (current.has(key)) {
1387	        current.delete(key);
1388	      } else {
1389	        current.add(key);
1390	        if (selectedAnswer === key) {
1391	          setSelectedAnswer('');
1392	          if ((session?.mode === 'full-section' || isPracticeSetMode) && session) {
1393	            const newAttempts = new Map(session.attempts);
1394	            newAttempts.delete(qid);
1395	            setSession({ ...session, attempts: newAttempts });
1396	          }
1397	        }
1398	      }
1399	      next.set(qid, current);
1400	      return next;
1401	    });
1402	  };
1403	
1404	  const handleLongPressStart = (key: string) => {
1405	    const timer = setTimeout(() => {
1406	      handleEliminateAnswer(key);
1407	    }, 500);
1408	    setLongPressTimer(timer);
1409	  };

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && grep -n \"FullSectionConfig\\|TypeDrillConfig\\|interface.*Config\\|mode:\" src/types/drill.ts | head -60", "description": "Inspect drill types"}

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillLaunchResolve.ts"}

## user

Tool result:
1	/**
2	 * Turning a Drill Launch's *name* into the questions it stands for.
3	 *
4	 * A launch names a run rather than containing it, so the kinds named by a row
5	 * have to read that row before the runner can start. This is the read.
6	 *
7	 * A row that is gone is a dead link, and a dead link says so. It does not fall
8	 * back to a generic drill: a student quietly drilling something nobody assigned
9	 * is worse than a student telling you a link is broken. See
10	 * `docs/adr/0016-a-drill-link-names-a-run-it-does-not-contain-one.md`.
11	 */
12	
13	import { DrillLaunchError, launchNeedsResolution, type DrillLaunch } from '@/lib/drillLaunch';
14	import { listSavedSets } from '@/lib/savedSets';
15	import { supabase } from '@/integrations/supabase/client';
16	import { getPracticePool } from '@/bootcamps/main-conclusion/data/practiceDrillPools';
17	import {
18	  pickHomeworkForDay,
19	  pickPracticeForDay,
20	} from '@/bootcamps/principle-flaw/lib/dayQuestions';
21	import {
22	  drillResumeKey,
23	  isResumableDrillSession,
24	  loadDrillResumeSession,
25	} from '@/lib/drillResumeSession';
26	import { getRecentExposureSet } from '@/lib/questionExposure';
27	import {
28	  getAssignment,
29	  getGuidedDrill,
30	  resolveGuidedDrillQidsForLevel,
31	  type GuidedDrill,
32	  type GuidedDrillAssignment,
33	} from '@/lib/guidedDrills';
34	import {
35	  getLocalGuidedDrillBySlug,
36	  isEmptyBankFilter,
37	} from '@/lib/guidedDrillsLocal';
38	import {
39	  guidedSessionKey,
40	  loadGuidedDrillSession,
41	} from '@/lib/guidedDrillSession';
42	
43	/** Raised when the link is well-formed but the thing it names is gone. */
44	export class DeadDrillLinkError extends DrillLaunchError {
45	  constructor(message: string) {
46	    super(message);
47	    this.name = 'DeadDrillLinkError';
48	  }
49	}
50	
51	export async function resolveDrillLaunch(
52	  launch: DrillLaunch,
53	  userId: string | undefined,
54	): Promise<string[] | undefined> {
55	  if (!launchNeedsResolution(launch)) return undefined;
56	
57	  switch (launch.kind) {
58	    case 'saved-set': {
59	      if (!userId) {
60	        throw new DeadDrillLinkError('You need to be signed in to open a saved set.');
61	      }
62	      // Saved sets belong to the student who saved them, so a link to someone
63	      // else's set finds nothing here — which is the intended answer, not a
64	      // failure to look hard enough.
65	      const sets = await listSavedSets(userId);
66	      const set = sets.find((s) => s.id === launch.setId);
67	      if (!set) {
68	        throw new DeadDrillLinkError('That saved set no longer exists.');
69	      }
70	      if (set.question_ids.length === 0) {
71	        throw new DeadDrillLinkError('That saved set has no questions in it.');
72	      }
73	      return set.question_ids;
74	    }
75	
76	    case 'assignment': {
77	      // `homework_assignments`, which is where the classroom assignment surfaces
78	      // read theirs from (`useStudentAssignment`). NOT `guided_drill_assignments`:
79	      // those are a different table with different ids, and looking an id up in
80	      // the wrong one makes a live assignment read as a dead link.
81	      const { data, error } = await supabase
82	        .from('homework_assignments')
83	        .select('id, question_qids')
84	        .eq('id', launch.assignmentId)
85	        .maybeSingle();
86	      if (error) throw error;
87	      const qids = (data as { question_qids?: string[] } | null)?.question_qids ?? [];
88	      if (!data) {
89	        throw new DeadDrillLinkError('That assignment no longer exists.');
90	      }
91	      if (qids.length === 0) {
92	        throw new DeadDrillLinkError('That assignment has no questions on it.');
93	      }
94	      return qids;
95	    }
96	
97	    case 'practice-set': {
98	      // The pool is static source data with a fixed list, so re-resolving the
99	      // slug gives back the same questions every time. Its Run Record is keyed
100	      // by the slug too, so both safety conditions hold.
101	      const pool = getPracticePool(launch.slug);
102	      if (!pool) {
103	        throw new DeadDrillLinkError('That practice set no longer exists.');
104	      }
105	      return [...pool.qids];
106	    }
107	
108	    case 'bootcamp-day': {
109	      const resumeKey = drillResumeKey({
110	        mode: 'type-drill',
111	        identity: launch,
112	      });
113	      let hasIdentityRecord = false;
114	      if (userId) {
115	        const stored = await loadDrillResumeSession(userId, resumeKey);
116	        hasIdentityRecord = !!stored;
117	        if (isResumableDrillSession(stored)) return stored.question_queue;
118	      }
119	
120	      // The day picker includes the student's recently-seen cooldown, so a
121	      // fresh resolution can legitimately produce a different list. The
122	      // identity-keyed Run Record above wins whenever one exists; only a new
123	      // run reaches this draw. The gate waits for the question bank first.
124	      const excludedQids = userId ? await getRecentExposureSet(userId, 500) : new Set<string>();
125	      const qids =
126	        launch.part === 'homework'
127	          ? pickHomeworkForDay(launch.day, undefined, excludedQids)
128	          : pickPracticeForDay(launch.day, undefined, excludedQids);
129	      if (userId && !hasIdentityRecord && qids.length > 0) {
130	        const legacyKey = drillResumeKey({
131	          mode: 'type-drill',
132	          config: { selectedQids: qids },
133	        });
134	        const legacy = await loadDrillResumeSession(userId, legacyKey);
135	        if (isResumableDrillSession(legacy)) return legacy.question_queue;
136	      }
137	      if (qids.length === 0) {
138	        throw new DeadDrillLinkError(
139	          `Day ${launch.day} has no ${launch.part} questions to give yet.`,
140	        );
141	      }
142	      return qids;
143	    }
144	
145	    case 'guided-drill': {
146	      let assignment: (GuidedDrillAssignment & { guided_drill?: GuidedDrill }) | null = null;
147	      let drill: GuidedDrill | null = null;
148	
149	      if (launch.assignmentId) {
150	        assignment = (await getAssignment(launch.assignmentId)) as typeof assignment;
151	        drill = assignment?.guided_drill ?? null;
152	      } else if (launch.drillId) {
153	        drill = await getGuidedDrill(launch.drillId);
154	        if (!drill) drill = getLocalGuidedDrillBySlug(launch.drillId);
155	      }
156	
157	      if (!drill) {
158	        throw new DeadDrillLinkError('That guided drill no longer exists.');
159	      }
160	
161	      const local = getLocalGuidedDrillBySlug(drill.slug);
162	      if (local && isEmptyBankFilter(drill.bank_filter)) {
163	        drill = {
164	          ...drill,
165	          bank_filter: local.bank_filter,
166	          question_count: drill.question_count ?? local.question_count,
167	        };
168	      }
169	
170	      if (userId) {
171	        const currentKey = guidedSessionKey({
172	          assignmentId: launch.assignmentId,
173	          drillId: launch.assignmentId ? undefined : launch.drillId,
174	        });
175	        const legacyKey = launch.assignmentId
176	          ? null
177	          : guidedSessionKey({ slug: drill.slug });
178	        const stored = await loadGuidedDrillSession(userId, currentKey, legacyKey);
179	        if (
180	          stored?.status === 'in_progress' &&
181	          stored.question_queue.length > 0 &&
182	          stored.attempts.length > 0
183	        ) {
184	          return stored.question_queue;
185	        }
186	      }
187	
188	      const resolution = resolveGuidedDrillQidsForLevel({ drill, assignment });
189	      if (resolution.warning === 'empty' || resolution.qids.length === 0) {
190	        throw new DeadDrillLinkError('That guided drill has no questions to give yet.');
191	      }
192	      return resolution.qids;
193	    }
194	
195	    default:
196	      throw new DrillLaunchError(
197	        `${launch.kind} links are not accepted yet — open it from the classroom instead.`,
198	      );
199	  }
200	}
201	

## user

Tool result:
9:export interface TimerConfig {
10:  mode: TimerMode;
17:export interface FullSectionConfig {
23:export interface TypeDrillConfig {
38:  mode: DrillMode;
39:  fullSectionConfig?: FullSectionConfig;
40:  typeDrillConfig?: TypeDrillConfig;

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\types\\drill.ts", "offset": 1, "limit": 45}

## user

Tool result:
1	// Drill mode types and interfaces
2	
3	export type DrillMode = 'adaptive' | 'full-section' | 'type-drill' | 'natural-drill' | 'practice-set';
4	
5	export type { Highlight, HighlightColor } from '@/lib/highlightUtils';
6	
7	export type TimerMode = '35' | '52.5' | '70' | 'custom' | 'unlimited';
8	
9	export interface TimerConfig {
10	  mode: TimerMode;
11	  customMinutes?: number;
12	  isPaused: boolean;
13	  elapsedMs: number;
14	  startedAt: number;
15	}
16	
17	export interface FullSectionConfig {
18	  pt: number;
19	  section: number;
20	  timer: TimerConfig;
21	}
22	
23	export interface TypeDrillConfig {
24	  qtypes: string[];
25	  difficulties: number[];
26	  pts: number[];
27	  count: number; // number of questions to drill
28	  selectedQids?: string[]; // optional pre-selected question IDs
29	  unseen_only?: boolean; // if true, force unseen-only filtering regardless of user's global setting
30	  qfeatures?: string[];
31	  reasoningTypes?: string[];
32	  sections?: number[];
33	  searchQuery?: string;
34	  questionNumber?: number;
35	}
36	
37	export interface DrillSession {
38	  mode: DrillMode;
39	  fullSectionConfig?: FullSectionConfig;
40	  typeDrillConfig?: TypeDrillConfig;
41	  questionQueue: string[]; // qids
42	  currentIndex: number;
43	  attempts: Map<string, {
44	    selectedAnswer: string;
45	    correct: boolean;

## assistant

Tool call: Grep
{"pattern": "full-section|navigate.*drill|pt.*section\" }|FullSectionConfig\">\n<parameter name=\"path\">C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\drill\\SectionSelector.tsx", "output_mode": "content", "-n": true}

## user

Tool result:
Search failed — ripgrep rejected the pattern, glob, or file type without searching:
rg: regex parse error:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1: (?:full-section|navigate.*drill|pt.*section" }|FullSectionConfig">
2: <parameter name="path">C:\Users\Joshu\dev\ai-os\projects\lsatu\src\components\drill\SectionSelector.tsx)
                              ^
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
error: invalid hexadecimal digit

## assistant

Tool call: Grep
{"pattern": "navigate\\(|mode=full-section|buildDrillLaunch|DrillLaunch", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\drill\\SectionSelector.tsx", "output_mode": "content", "-n": true}

## user

Tool result:
No matches found

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && wc -l src/components/drill/SectionSelector.tsx src/pages/TestingCentre.tsx", "description": "Line counts"}

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\pages\\TestingCentre.tsx"}

## user

Tool result:
1	/**
2	 * The Testing Centre.
3	 *
4	 * Two doors, and only two: sit one real section, or sit a full practice test.
5	 * Both are things you do under a clock with nothing revealed until the end,
6	 * which is what separates this room from Drill next door — drilling is practice
7	 * you stop and think inside, and a sitting is not. Keeping them apart is the
8	 * whole reason this is its own rail entry: nobody should start a 35:00 clock
9	 * while looking for a ten-question warm-up.
10	 *
11	 * Neither door owns a question runner. The section door hands off to
12	 * SectionSelector, which this page is the only consumer of; the practice-test
13	 * door hands off to the same two runners, one leg at a time.
14	 */
15	import * as React from "react";
16	import { useNavigate } from "react-router-dom";
17	import { Loader2 } from "lucide-react";
18	import { Button } from "@/components/ui/button";
19	import {
20	  Select,
21	  SelectContent,
22	  SelectItem,
23	  SelectTrigger,
24	  SelectValue,
25	} from "@/components/ui/select";
26	import { useQuestionBank } from "@/contexts/QuestionBankContext";
27	import { useUserSettings } from "@/contexts/UserSettingsContext";
28	import { SectionSelector } from "@/components/drill/SectionSelector";
29	import { AccommodationNote } from "@/components/drill/SectionTimingPicker";
30	import { PrepTestCombobox } from "@/components/testing/PrepTestCombobox";
31	import { loadAllIndexPassages } from "@/features/rc/lib/rcBank";
32	import { buildRcSections, type RcSection } from "@/features/rc/lib/rcSections";
33	import {
34	  buildPracticeTests,
35	  createPracticeTestRun,
36	  deletePracticeTestRun,
37	  formatPracticeTestClock,
38	  legLabel,
39	  listPracticeTestRuns,
40	  practiceTestPaces,
41	  practiceTestSectionSeconds,
42	  type PracticeTestBlueprint,
43	  type PracticeTestPaceId,
44	  type PracticeTestRun,
45	} from "@/lib/practiceTest";
46	import { practiceTestPath } from "@/lib/practiceTestRunner";
47	import "./testing-centre.css";
48	
49	type Door = null | "section" | "test";
50	
51	/** The panel both doors open into. Named so a door can point at it. */
52	const PANEL_ID = "testing-door-panel";
53	
54	/**
55	 * How much of the panel has to be on screen before opening a door is allowed to
56	 * move the page. Below this the panel is a sliver at the bottom edge and the
57	 * click reads as a no-op; above it the student can already see what happened.
58	 */
59	const PANEL_VISIBLE_MARGIN = 120;
60	
61	/**
62	 * RC sections, loaded only once something needs them.
63	 *
64	 * This used to run on mount, which pulled the whole Reading Comprehension index
65	 * across the wire to render two buttons. Only the practice-test door needs it —
66	 * the section door asks SectionSelector for its own — so it waits for `enabled`.
67	 */
68	function useRcSections(enabled: boolean) {
69	  const [sections, setSections] = React.useState<RcSection[] | null>(null);
70	  const [error, setError] = React.useState<string | null>(null);
71	
72	  React.useEffect(() => {
73	    if (!enabled) return;
74	    let cancelled = false;
75	    loadAllIndexPassages()
76	      .then((passages) => {
77	        if (!cancelled) setSections(buildRcSections(passages));
78	      })
79	      .catch(() => {
80	        if (!cancelled) setError("Reading Comprehension sections could not be loaded.");
81	      });
82	    return () => {
83	      cancelled = true;
84	    };
85	  }, [enabled]);
86	
87	  return { sections, error };
88	}
89	
90	/**
91	 * A status line that assistive tech is actually told about.
92	 *
93	 * Every wait on this page used to be a plain paragraph that appeared and
94	 * disappeared in silence: a screen reader user pressed a door and heard
95	 * nothing until they went looking.
96	 */
97	function Working({ children }: { children: React.ReactNode }) {
98	  return (
99	    <div
100	      className="flex items-center gap-3 py-4 text-sm"
101	      role="status"
102	      aria-live="polite"
103	    >
104	      <Loader2 className="h-4 w-4 animate-spin" aria-hidden />
105	      {children}
106	    </div>
107	  );
108	}
109	
110	function PracticeTestSelector({
111	  tests,
112	  onBegin,
113	}: {
114	  tests: PracticeTestBlueprint[];
115	  onBegin: (
116	    blueprint: PracticeTestBlueprint,
117	    pace: PracticeTestPaceId,
118	    sectionSeconds: number | null,
119	  ) => void;
120	}) {
121	  const [pt, setPt] = React.useState<number | null>(null);
122	  const [pace, setPace] = React.useState<PracticeTestPaceId>("standard");
123	  const { settings } = useUserSettings();
124	
125	  /**
126	   * The student's own standard clock, the same reading the section door takes
127	   * (SectionSelector's baseMinutes). Every pace here is a percentage of this,
128	   * so "Standard" is their normal section rather than a flat 35 minutes. This
129	   * door ignored the setting entirely before, which meant the same two words
130	   * named two different clocks in one room.
131	   */
132	  const baseMinutes =
133	    settings.defaultTimingMode === "52.5" ? 52.5 : settings.defaultTimingMode === "70" ? 70 : 35;
134	  const paces = React.useMemo(() => practiceTestPaces(baseMinutes * 60), [baseMinutes]);
135	  const sectionSeconds = practiceTestSectionSeconds(pace, baseMinutes * 60);
136	
137	  // The combobox orders its own rows newest-first. This page still needs the
138	  // blueprint behind the chosen number, for the shape table below.
139	  const ptOptions = React.useMemo(
140	    () => tests.map((t) => ({ pt: t.pt, detail: `${t.questionCount} questions` })),
141	    [tests],
142	  );
143	  const chosen = tests.find((t) => t.pt === pt) ?? null;
144	  const clock = formatPracticeTestClock(sectionSeconds);
145	
146	  if (tests.length === 0) {
147	    return (
148	      <div className="testing-panel">
149	        <p className="testing-note">
150	          No PrepTest in the bank currently has the two full Logical Reasoning
151	          sections and the full Reading Comprehension section a sitting needs.
152	          Single sections are still available through the other door.
153	        </p>
154	      </div>
155	    );
156	  }
157	
158	  return (
159	    <div className="testing-panel">
160	      <div className="testing-field">
161	        <label htmlFor="testing-pt" id="testing-pt-label">
162	          PrepTest
163	        </label>
164	        <PrepTestCombobox
165	          emptyMessage="No PrepTest by that number can be sat end to end."
166	          id="testing-pt"
167	          labelId="testing-pt-label"
168	          onChange={setPt}
169	          options={ptOptions}
170	          value={pt}
171	        />
172	      </div>
173	
174	      <div className="testing-field">
175	        <label htmlFor="testing-pace" id="testing-pace-label">
176	          Timing
177	        </label>
178	        <Select value={pace} onValueChange={(v) => setPace(v as PracticeTestPaceId)}>
179	          <SelectTrigger
180	            id="testing-pace"
181	            aria-labelledby="testing-pace-label testing-pace"
182	          >
183	            <SelectValue />
184	          </SelectTrigger>
185	          <SelectContent className="testing-menu">
186	            {paces.map((p) => (
187	              <SelectItem key={p.id} value={p.id}>
188	                {p.label}
189	                {p.sectionSeconds === null
190	                  ? " · no clock"
191	                  : ` · ${Math.round(p.sectionSeconds / 60)} min a section`}
192	              </SelectItem>
193	            ))}
194	          </SelectContent>
195	        </Select>
196	        {/* The section door has carried this since its timing control was
197	            built. Without it this door offered accommodations while saying
198	            nothing about the standing setting those percentages are taken
199	            from, on the longer of the two commitments. */}
200	        <p className="testing-note">
201	          <AccommodationNote baseMinutes={baseMinutes} />
202	        </p>
203	      </div>
204	
205	      {chosen && (
206	        <>
207	          <div className="testing-shape">
208	            {chosen.legs.map((leg, i) => (
209	              <div className="testing-shape-row" key={`${leg.kind}-${leg.section}`}>
210	                <b>Section {i + 1}</b>
211	                <span>{legLabel(leg as never)}</span>
212	                <em>
213	                  {leg.questionCount} questions
214	                  {clock ? ` · ${clock}` : ""}
215	                </em>
216	              </div>
217	            ))}
218	          </div>
219	          <p className="testing-note">
220	            {chosen.questionCount} scored questions, with a ten-minute break
221	            after the second section.
222	          </p>
223	          {/* The clock is read from the chosen pace rather than printed as
224	              35:00. It was hard-coded, which stopped being true the moment this
225	              door started honouring the student's own timing mode: an
226	              accommodated student saw 52:30 on the control and "the real 35:00"
227	              in the paragraph under it. The clause drops out entirely when
228	              there is no clock, rather than asserting a number for a sitting
229	              that is not being timed. */}
230	          {!chosen.rcFullLength && (
231	            <p className="testing-note">
232	              The Reading Comprehension section on this PrepTest runs a few
233	              questions short, because only questions with a published
234	              explanation can be drilled. All four passages are there
235	              {clock ? ` and the clock is the real ${clock}` : ""}, so the
236	              reading load is unchanged. Your score is simply out of{" "}
237	              {chosen.questionCount} rather than the high seventies.
238	            </p>
239	          )}
240	        </>
241	      )}
242	
243	      <div className="testing-actions">
244	        <Button disabled={!chosen} onClick={() => chosen && onBegin(chosen, pace, sectionSeconds)}>
245	          Begin practice test
246	        </Button>
247	      </div>
248	    </div>
249	  );
250	}
251	
252	function ResumeList({
253	  runs,
254	  onResume,
255	  onDiscard,
256	}: {
257	  runs: PracticeTestRun[];
258	  onResume: (run: PracticeTestRun) => void;
259	  onDiscard: (run: PracticeTestRun) => void;
260	}) {
261	  // Discard deletes a sitting that can be ninety minutes into a two-hour clock,
262	  // and it did that on one click with no confirm and no undo. Below 560px
263	  // .testing-shape-actions goes full width, which puts it exactly where a thumb
264	  // lands. The confirm is inline rather than a dialog: this room has no modal,
265	  // and a two-option question that belongs to one row does not need one.
266	  const [confirming, setConfirming] = React.useState<string | null>(null);
267	  const keepRef = React.useRef<HTMLButtonElement | null>(null);
268	
269	  // Focus the safe option, never the destructive one. A keyboard user who
270	  // pressed Enter on Discard would otherwise be a single Enter away from the
271	  // deletion this confirm exists to prevent. Moving focus is also what
272	  // announces the state change: the group carries the question as its name, so
273	  // a screen reader reads what is being asked before it reads the choice.
274	  React.useEffect(() => {
275	    if (confirming) keepRef.current?.focus();
276	  }, [confirming]);
277	
278	  // A sitting can leave from under an open confirm (resumed in another tab,
279	  // cleared elsewhere). Without this the row is stuck asking about something
280	  // that is no longer there.
281	  React.useEffect(() => {
282	    if (confirming && !runs.some((run) => run.id === confirming)) {
283	      setConfirming(null);
284	    }
285	  }, [runs, confirming]);
286	
287	  if (runs.length === 0) return null;
288	  return (
289	    <div className="testing-resume">
290	      {/* h2, not h3: this is the first section of the page and the only other
291	          heading is the page title. It sits above the doors because an
292	          unfinished sitting is the next step, not an afterthought. */}
293	      <h2>Unfinished sittings</h2>
294	      <div className="testing-shape">
295	        {runs.map((run) => {
296	          return (
297	            <div className="testing-shape-row" key={run.id}>
298	              <b>PT {run.pt}</b>
299	              <span>
300	                Section {Math.min(run.currentLeg + 1, run.legs.length)} of{" "}
301	                {run.legs.length}
302	              </span>
303	              {/* min-h-[44px] because Button's own sm size stops at 40px, and
304	                  the 44px floor is a defect gate here, not a preference. Both
305	                  carry a name saying which sitting they act on: two rows of
306	                  "Resume / Discard" are indistinguishable to a screen reader
307	                  reading the controls on their own. */}
308	              {confirming === run.id ? (
309	                <div
310	                  className="testing-shape-actions"
311	                  role="group"
312	                  aria-label={`Discard the unfinished PrepTest ${run.pt} sitting?`}
313	                >
314	                  <span className="testing-confirm">Discard this sitting?</span>
315	                  <Button
316	                    size="sm"
317	                    variant="ghost"
318	                    className="min-h-[44px]"
319	                    onClick={() => {
320	                      onDiscard(run);
321	                      setConfirming(null);
322	                    }}
323	                    aria-label={`Yes, discard the unfinished PrepTest ${run.pt} sitting`}
324	                  >
325	                    Discard
326	                  </Button>
327	                  <Button
328	                    ref={keepRef}
329	                    size="sm"
330	                    variant="outline"
331	                    className="min-h-[44px]"
332	                    onClick={() => setConfirming(null)}
333	                    aria-label={`Keep the unfinished PrepTest ${run.pt} sitting`}
334	                  >
335	                    Keep
336	                  </Button>
337	                </div>
338	              ) : (
339	                <div className="testing-shape-actions">
340	                  <Button
341	                    size="sm"
342	                    variant="outline"
343	                    className="min-h-[44px]"
344	                    onClick={() => onResume(run)}
345	                    aria-label={`Resume PrepTest ${run.pt}`}
346	                  >
347	                    Resume
348	                  </Button>
349	                  <Button
350	                    size="sm"
351	                    variant="ghost"
352	                    className="min-h-[44px]"
353	                    onClick={() => setConfirming(run.id)}
354	                    aria-label={`Discard the unfinished PrepTest ${run.pt} sitting`}
355	                  >
356	                    Discard
357	                  </Button>
358	                </div>
359	              )}
360	            </div>
361	          );
362	        })}
363	      </div>
364	    </div>
365	  );
366	}
367	
368	export default function TestingCentre() {
369	  const navigate = useNavigate();
370	  const { manifest, isLoading, error } = useQuestionBank();
371	  const [door, setDoor] = React.useState<Door>(null);
372	  const { sections: rcSections, error: rcError } = useRcSections(door === "test");
373	  const [runs, setRuns] = React.useState<PracticeTestRun[]>([]);
374	
375	  React.useEffect(() => {
376	    setRuns(listPracticeTestRuns().filter((r) => r.status === "in-progress"));
377	  }, []);
378	
379	  const tests = React.useMemo(
380	    () => (manifest && rcSections ? buildPracticeTests(manifest, rcSections) : []),
381	    [manifest, rcSections],
382	  );
383	
384	  const beginTest = (
385	    blueprint: PracticeTestBlueprint,
386	    pace: PracticeTestPaceId,
387	    sectionSeconds: number | null,
388	  ) => {
389	    const run = createPracticeTestRun(blueprint, pace, sectionSeconds);
390	    navigate(practiceTestPath(run.id));
391	  };
392	
393	  const discard = (run: PracticeTestRun) => {
394	    deletePracticeTestRun(run.id);
395	    setRuns((current) => current.filter((r) => r.id !== run.id));
396	  };
397	
398	  // A door's panel renders below the two door buttons, which on a laptop puts it
399	  // under the fold: the click looks like it did nothing, and the section type
400	  // picker (Logical Reasoning / Reading Comprehension) is never seen, so the door
401	  // reads as LR-only. Bring the panel to the student when it opens.
402	  //
403	  // Anchored on the doors rather than the panel. Scrolling the panel itself to
404	  // the top of the viewport over-corrected into the opposite failure: the panel
405	  // is taller than the viewport, so the page ran to its own scroll maximum and
406	  // took the room's name and the door that was just pressed with it. Measured at
407	  // 1280x900, .classroom-title landed at -234px and 78% of the door row was off
408	  // screen, at the moment a student commits to a timed section. Putting the door
409	  // row at the top keeps the choice that was just made on screen, and the panel
410	  // begins directly beneath it.
411	  const panelRef = React.useRef<HTMLDivElement | null>(null);
412	  const doorsRef = React.useRef<HTMLDivElement | null>(null);
413	  React.useEffect(() => {
414	    if (!door) return;
415	    const panel = panelRef.current;
416	    if (!panel) return;
417	    // Leave the page alone when the panel already starts on screen. The click
418	    // did not read as a no-op, and moving the page under a student who can
419	    // already see the result is its own small betrayal.
420	    const top = panel.getBoundingClientRect().top;
421	    if (top >= 0 && top <= window.innerHeight - PANEL_VISIBLE_MARGIN) return;
422	    const prefersReducedMotion = window.matchMedia?.(
423	      "(prefers-reduced-motion: reduce)",
424	    ).matches;
425	    (doorsRef.current ?? panel).scrollIntoView({
426	      behavior: prefersReducedMotion ? "auto" : "smooth",
427	      block: "start",
428	    });
429	  }, [door]);
430	
431	  return (
432	    <>
433	      <h1 className="classroom-title">Testing Centre</h1>
434	      <p className="testing-lede">
435	        Official LSAT material, timed like test day.
436	      </p>
437	
438	      <ResumeList
439	        runs={runs}
440	        onResume={(run) => navigate(practiceTestPath(run.id))}
441	        onDiscard={discard}
442	      />
443	
444	      {/* The doors carry a title and two supporting lines, and those used to be
445	          an h2 and a p. Neither is legal inside a button — its content model is
446	          phrasing only — and the h2s put two headings in the outline that a
447	          screen reader lands on as controls. They are spans that look the same.
448	
449	          aria-expanded, not aria-pressed: these are not toggle buttons, they
450	          disclose a panel, and aria-controls is what says which panel. */}
451	      <div className="testing-doors" ref={doorsRef}>
452	        <button
453	          type="button"
454	          className="testing-door"
455	          aria-expanded={door === "section"}
456	          aria-controls={PANEL_ID}
457	          onClick={() => setDoor(door === "section" ? null : "section")}
458	        >
459	          <span className="testing-door-title">Take a section</span>
460	          {/* No clock here: the meta line below already carries it. */}
461	          <span className="testing-door-body">
462	            One real LR or RC section from an official PrepTest.
463	          </span>
464	          <span className="testing-door-meta">One section · 35 minutes</span>
465	        </button>
466	
467	        <button
468	          type="button"
469	          className="testing-door"
470	          aria-expanded={door === "test"}
471	          aria-controls={PANEL_ID}
472	          onClick={() => setDoor(door === "test" ? null : "test")}
473	        >
474	          <span className="testing-door-title">Take a practice test</span>
475	          <span className="testing-door-body">
476	            Three scored sections from one PrepTest, in order, with a break.
477	          </span>
478	          <span className="testing-door-meta">Three sections · about 2 hours</span>
479	        </button>
480	      </div>
481	
482	      <div id={PANEL_ID} ref={panelRef}>
483	        {door === "section" && (
484	          <div className="testing-panel">
485	            {isLoading && <Working>Loading questions…</Working>}
486	            {!isLoading && error && <p className="testing-note">{error}</p>}
487	            {!isLoading && !error && manifest && (
488	              <SectionSelector
489	                manifest={manifest}
490	                onStartSection={(config) =>
491	                  navigate("/drill", {
492	                    state: { mode: "full-section", config, returnTo: "/testing" },
493	                  })
494	                }
495	                onStartRcSection={(href) => navigate(href)}
496	                onCancel={() => setDoor(null)}
497	              />
498	            )}
499	          </div>
500	        )}
501	
502	        {door === "test" && (
503	          <>
504	            {(isLoading || (!rcSections && !rcError)) && (
505	              <div className="testing-panel">
506	                <Working>Working out which PrepTests can be sat end to end…</Working>
507	              </div>
508	            )}
509	            {!isLoading && (error || rcError) && (
510	              <div className="testing-panel">
511	                <p className="testing-note">{error || rcError}</p>
512	              </div>
513	            )}
514	            {!isLoading && !error && !rcError && manifest && rcSections && (
515	              <PracticeTestSelector tests={tests} onBegin={beginTest} />
516	            )}
517	          </>
518	        )}
519	      </div>
520	    </>
521	  );
522	}
523	

## user

Tool result:
  565 src/components/drill/SectionSelector.tsx
  522 src/pages/TestingCentre.tsx
 1087 total

## assistant

Tool call: Grep
{"pattern": "qids|mode=|searchParams.get|location.state|full-section", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\components\\drill\\DrillLaunchGate.tsx", "output_mode": "content", "-n": true}

## user

Tool result:
14: * An older link — `?mode=type-drill&qids=…` — is read but never rewritten.
67:  const namedInUrl = !!searchParams.get('drill') || !!searchParams.get('mode');
87:    const routeState = location.state as (DrillHandoverState & { ptRun?: PtLegRef }) | null;
93:    const queryReturnTo = searchParams.get('returnTo');
104:  }, [searchParams, location.state]);
130:        const qids = await resolveDrillLaunch(launch, user?.id);
132:        if (launch.kind === 'bootcamp-day' && user?.id && qids?.length) {
133:          void recordExposures(user.id, qids).catch((error) => {
139:        setResolved({ key: launchKey, spec: drillRunSpecFromLaunch(launch, qids) });

## assistant

Good — confirms `?mode=type-drill&qids=…` is the legacy URL grammar, still supported, producing a `type-drill` DrillRunSpec (config.selectedQids), never `full-section`. Let's check `drillLaunch.ts` parsing to confirm this precisely.

## assistant

Tool call: Grep
{"pattern": "type-drill|qids|assignment|mode ===|parseDrillLaunch|function.*Launch", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillLaunch.ts", "output_mode": "content", "-n": true}

## user

Tool result:
15: * and `parseDrillLaunch` reads one back, and the pair round-trips. The runner
63: * drill is `drill=guided-drill`, not a list of qids with a flag beside it. But
78:  /** A classroom homework assignment the list belongs to. */
79:  assignmentId?: string;
118:  /** A classroom assignment. Its row owns the question list. */
119:  | { kind: 'assignment'; assignmentId: string; guidedSetId?: string }
120:  /** A guided drill, optionally the one handed over as an assignment. */
124:      assignmentId?: string;
149:      qids: string[];
177:  'assignment',
183:export function launchNeedsResolution(launch: DrillLaunch): boolean {
210:export function launchDrill(launch: DrillLaunch): string {
231:    case 'assignment':
232:      p.set('assignment', launch.assignmentId);
237:      if (launch.assignmentId) p.set('assignment', launch.assignmentId);
249:      p.set('qids', launch.qids.join(','));
255:        if (c.mode !== 'type-drill') p.set('runMode', c.mode);
261:        if (c.assignmentId) p.set('assignment', c.assignmentId);
337:function undefinedIfEmpty(options: DrillLaunchOptions): DrillLaunchOptions | undefined {
370:    (mode && mode !== 'type-drill') ||
376:    mode: mode ?? 'type-drill',
392:    assignmentId: p.get('assignment') || undefined,
412:    assignmentId: p.get('assignmentId') || undefined,
423:function readOptions(p: URLSearchParams): DrillLaunchOptions | undefined {
456:  forbid('qids', ['questions']);
460:function parseCanonical(p: URLSearchParams): DrillLaunch {
493:    case 'assignment': {
494:      const assignmentId = p.get('assignment');
495:      if (!assignmentId) {
496:        throw new DrillLaunchError('an assignment launch needs an assignment id');
500:        assignmentId,
508:      const assignmentId = p.get('assignment') || undefined;
509:      if (!drillId && !assignmentId) {
511:          'a guided-drill launch needs a drill id or an assignment id',
517:        assignmentId,
541:      const qids = list(p.get('qids'));
542:      if (qids.length === 0) {
545:      return { kind, qids, carry: readCarry(p), options };
579:function parseLegacy(p: URLSearchParams): DrillLaunch | null {
587:  if (mode === 'full-section') {
610:    // type-drill rather than an error.
615:    qids: list(p.get('qids')),
624:      (mode === 'practice-set' ? 'type-drill' : mode) as DrillMode,
635:export function parseDrillLaunch(searchParams: URLSearchParams): DrillLaunch | null {
681:  if (state.mode === 'adaptive') {
685:  if (state.mode === 'full-section') {
692:      timerMode: config.timer.mode === '35' ? undefined : config.timer.mode,
706:      qids: config.selectedQids,
709:        mode: state.mode === 'practice-set' ? 'type-drill' : state.mode,

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillLaunch.ts", "offset": 579, "limit": 55}

## user

Tool result:
579	function parseLegacy(p: URLSearchParams): DrillLaunch | null {
580	  const mode = p.get('mode');
581	  if (!mode) return null;
582	
583	  const returnTo = safeReturnTo(p.get('returnTo'));
584	  const sealed = p.get('sealed') === '1';
585	  const initialIndex = nonNegativeInt(p.get('initialIndex'));
586	
587	  if (mode === 'full-section') {
588	    const pt = positiveNumber(p.get('pt'));
589	    const section = positiveNumber(p.get('section'));
590	    if (pt && section) {
591	      // Today's section branch reads a heading and does not read `present`.
592	      return {
593	        kind: 'section',
594	        pt,
595	        section,
596	        // 52.5, 70 and unlimited are the accommodated clocks. Reducing them to
597	        // a number of minutes would quietly re-time an accommodated sitting.
598	        timerMode: readTimerMode(p.get('timer')),
599	        minutes: positiveNumber(p.get('minutes')),
600	        sealed: sealed || undefined,
601	        ptLeg: readPtLeg(p.get('runId'), p.get('leg')),
602	        options: undefinedIfEmpty({
603	          ...(returnTo ? { returnTo } : {}),
604	          ...(legacyLabel(p) ? { label: legacyLabel(p) as string } : {}),
605	          ...(initialIndex != null ? { initialIndex } : {}),
606	        }),
607	      };
608	    }
609	    // Falls through exactly as before: a malformed section link became an empty
610	    // type-drill rather than an error.
611	  }
612	
613	  return {
614	    kind: 'questions',
615	    qids: list(p.get('qids')),
616	    options: undefinedIfEmpty({
617	      ...(returnTo ? { returnTo } : {}),
618	      ...(legacyLabel(p) ? { label: legacyLabel(p) as string } : {}),
619	      ...(initialIndex != null ? { initialIndex } : {}),
620	      ...(p.get('present') === 'smart' ? { present: 'smart' as const } : {}),
621	    }),
622	    carry: readLegacyCarry(
623	      p,
624	      (mode === 'practice-set' ? 'type-drill' : mode) as DrillMode,
625	    ),
626	  };
627	}
628	
629	/**
630	 * Read a launch from the address bar. The canonical grammar wins; today's
631	 * grammar is tried second. Returns null when the URL names no drill at all,
632	 * which is the case the caller handles by falling back to route state during
633	 * the migration.

## assistant

Tool call: Grep
{"pattern": "drillRunSpecFromLaunch|case 'section'|case 'questions'|case 'assignment'\" -A 15", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillLaunch.ts", "output_mode": "content", "-n": true}

## user

Tool result:
16: * consumes a launch through `drillRunSpecFromLaunch`; there is no second
217:    case 'section':
248:    case 'questions': {
469:    case 'section': {
540:    case 'questions': {

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && grep -n \"drillRunSpecFromLaunch\" -A 60 src/lib/drillLaunch.ts | head -90", "description": "Inspect drillRunSpecFromLaunch (reverse) function"}

## user

Tool result:
16: * consumes a launch through `drillRunSpecFromLaunch`; there is no second
17- * grammar and no expansion step.
18- */
19-
20-import type {
21-  DrillMode,
22-  FullSectionConfig,
23-  TimerMode,
24-  TypeDrillConfig,
25-} from '@/types/drill';
26-import type { DrillResumeIdentity } from '@/lib/drillResumeSession';
27-
28-/**
29- * Switches that mean the same thing whatever kind of drill is running. Anything
30- * that belongs to one kind lives inside that kind instead, so that a link
31- * cannot ask for a section timer on a Smart Drill.
32- */
33-export interface DrillLaunchOptions {
34-  /** Where the runner's exit sends the student. Must be an app-relative path. */
35-  returnTo?: string;
36-  /** Heading shown while the drill runs. */
37-  label?: string;
38-  /** Open on this question rather than the first. Someone jumping deliberately. */
39-  initialIndex?: number;
40-  /**
41-   * Presentation only: render the adaptive Smart-Drill chrome even for a fixed
42-   * queue, so a hand-picked question looks identical to an Auto run.
43-   */
44-  present?: 'smart';
45-}
46-
47-/**
48- * Which test run and which leg of it this section belongs to. A practice-test
49- * leg is a Section with a run attached, not a kind of its own: it runs, looks
50- * and closes out identically, and the only difference is that something is
51- * waiting on the result. Losing it on refresh is what left a practice test
52- * permanently open, because the close-out had nothing to write against.
53- */
54-export interface PtLegRef {
55-  runId: string;
56-  legIndex: number;
57-}
58-
59-/**
60- * What a bare list of questions is carrying on its back.
61- *
62- * The canonical grammar expresses most of this as a kind of its own — a guided
63- * drill is `drill=guided-drill`, not a list of qids with a flag beside it. But
64- * two things still produce a list plus a flag: a link already sitting in a
65- * student's inbox, and a button that hands the run over in memory. Both name a
66- * real run, so what they say has to survive being written into the address bar
67- * and read back out.
68- *
69- * Every field here is optional except the two a `questions` launch always
70- * knows. Nothing is inferred: a value that was not sent stays absent rather
71- * than defaulting into a different run.
72- */
73-export interface RunCarry {
74-  mode: DrillMode;
75-  sealed: boolean;
76-  isGuidedDrill: boolean;

## assistant

Tool call: Grep
{"pattern": "export function drillRunSpecFromLaunch", "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src", "output_mode": "content", "-n": true}

## user

Tool result:
projects\lsatu\src\lib\drillRunSpec.ts:88:export function drillRunSpecFromLaunch(

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillRunSpec.ts"}

## user

Tool result:
1	/**
2	 * What the runner is told about the run it is about to start.
3	 *
4	 * A Drill Launch names a run (`?drill=saved-set&set=…`). This is that name
5	 * turned into the working shape the runner uses: the mode, the config, and the
6	 * handful of ids that say which stored row this run belongs to.
7	 *
8	 * It replaces `drillRouteState`, which derived the same thing by re-reading the
9	 * query string in a second, parallel grammar. There is now one reader — the
10	 * codec in `drillLaunch` — and one shape, built here and handed down by
11	 * `DrillLaunchGate`. The address bar keeps the short link it arrived with; the
12	 * runner no longer needs it expanded into a long one.
13	 *
14	 * See `docs/adr/0016-a-drill-link-names-a-run-it-does-not-contain-one.md`.
15	 */
16	
17	import type {
18	  DrillMode,
19	  FullSectionConfig,
20	  TimerConfig,
21	  TypeDrillConfig,
22	} from '@/types/drill';
23	import { DrillLaunchError, type DrillLaunch, type PtLegRef } from '@/lib/drillLaunch';
24	import type { DrillResumeIdentity } from '@/lib/drillResumeSession';
25	
26	export interface DrillRunSpec {
27	  mode?: DrillMode;
28	  config?: FullSectionConfig | TypeDrillConfig;
29	  /** Heading shown while the drill runs. */
30	  practicingLabel?: string;
31	  /** Where the runner's exit sends the student. Always app-relative. */
32	  returnTo?: string;
33	  /** True when the runner is launched from a Guided Drill. */
34	  isGuidedDrill?: boolean;
35	  guidedDurationMinutes?: number;
36	  /**
37	   * Presentation hint, independent of `mode`. When 'smart', the runner renders
38	   * the adaptive Smart-Drill chrome even for a fixed-queue type-drill.
39	   */
40	  present?: 'smart';
41	  /**
42	   * Seals the run: Answer and Explanation are not rendered at all, for the
43	   * whole session, for every question. A launch property and not a student
44	   * setting, because the person who assigns the section decides.
45	   */
46	  sealed?: boolean;
47	  /** Open on this question rather than the first. */
48	  initialIndex?: number;
49	
50	  // ── Which stored row this run belongs to ────────────────────────────────
51	  // Previously read straight off the query string by the runner, in a second
52	  // grammar that only agreed with the codec by coincidence.
53	  /** A classroom homework assignment. */
54	  assignmentId?: string;
55	  guidedSetId?: string;
56	  guidedDrillId?: string;
57	  guidedAssignmentId?: string;
58	  /** Intro to LR practice set: what it is, and which pool. */
59	  practiceSource?: string;
60	  practiceSlug?: string;
61	  /** Names the Run Record for a bootcamp day, so a re-draw cannot orphan it. */
62	  resumeIdentity?: DrillResumeIdentity;
63	  /** Which practice-test run and leg this section closes out. */
64	  ptRun?: PtLegRef;
65	}
66	
67	export interface DrillTimerConfig {
68	  mode: 'countdown' | 'stopwatch';
69	  durationMs?: number;
70	}
71	
72	function typeDrillConfig(qids: string[]): TypeDrillConfig {
73	  return {
74	    qtypes: [],
75	    difficulties: [],
76	    pts: [],
77	    count: qids.length,
78	    selectedQids: qids,
79	  };
80	}
81	
82	/**
83	 * Build the run spec from a launch.
84	 *
85	 * `resolvedQids` is how the id-named kinds arrive: their question list lives in
86	 * a row, and `resolveDrillLaunch` reads that row before this is called.
87	 */
88	export function drillRunSpecFromLaunch(
89	  launch: DrillLaunch,
90	  resolvedQids?: string[],
91	  now: number = Date.now(),
92	): DrillRunSpec {
93	  const options = launch.options ?? {};
94	  const base: DrillRunSpec = {
95	    returnTo: options.returnTo,
96	    practicingLabel: options.label,
97	    present: options.present,
98	    initialIndex: options.initialIndex,
99	  };
100	
101	  switch (launch.kind) {
102	    case 'smart-drill':
103	      return { ...base, mode: 'adaptive', sealed: false };
104	
105	    case 'section': {
106	      const config: FullSectionConfig = {
107	        pt: launch.pt,
108	        section: launch.section,
109	        timer: {
110	          mode: launch.timerMode ?? (launch.minutes ? 'custom' : '35'),
111	          customMinutes: launch.minutes,
112	          isPaused: false,
113	          elapsedMs: 0,
114	          startedAt: now,
115	        },
116	      };
117	      return {
118	        ...base,
119	        mode: 'full-section',
120	        config,
121	        sealed: !!launch.sealed,
122	        ptRun: launch.ptLeg,
123	      };
124	    }
125	
126	    case 'questions': {
127	      const carry = launch.carry;
128	      return {
129	        ...base,
130	        mode: carry?.mode ?? 'type-drill',
131	        config: typeDrillConfig(launch.qids),
132	        sealed: carry?.sealed ?? false,
133	        isGuidedDrill: carry?.isGuidedDrill ?? false,
134	        guidedDurationMinutes: carry?.guidedDurationMinutes,
135	        assignmentId: carry?.assignmentId,
136	        guidedSetId: carry?.guidedSetId,
137	        guidedDrillId: carry?.guidedDrillId,
138	        guidedAssignmentId: carry?.guidedAssignmentId,
139	        practiceSource: carry?.practiceSource,
140	        practiceSlug: carry?.practiceSlug,
141	        resumeIdentity: carry?.resumeIdentity,
142	        ptRun: carry?.ptLeg,
143	      };
144	    }
145	
146	    case 'filter':
147	      return {
148	        ...base,
149	        mode: 'type-drill',
150	        config: {
151	          qtypes: launch.qtypes ?? [],
152	          difficulties: launch.difficulties ?? [],
153	          pts: launch.pts ?? [],
154	          sections: launch.sections,
155	          qfeatures: launch.qfeatures,
156	          count: launch.count,
157	        },
158	        sealed: false,
159	      };
160	
161	    case 'saved-set':
162	    case 'assignment':
163	    case 'guided-drill':
164	    case 'practice-set':
165	    case 'bootcamp-day': {
166	      if (!resolvedQids) {
167	        throw new DrillLaunchError(
168	          `a ${launch.kind} launch must have its questions resolved before it can run`,
169	        );
170	      }
171	      const spec: DrillRunSpec = {
172	        ...base,
173	        mode: 'type-drill',
174	        config: typeDrillConfig(resolvedQids),
175	        sealed: false,
176	        isGuidedDrill: launch.kind === 'guided-drill',
177	      };
178	      if (launch.kind === 'assignment') {
179	        spec.assignmentId = launch.assignmentId;
180	        spec.guidedSetId = launch.guidedSetId;
181	      }
182	      if (launch.kind === 'guided-drill') {
183	        spec.guidedDurationMinutes = launch.durationMinutes;
184	        spec.guidedDrillId = launch.drillId;
185	        spec.guidedAssignmentId = launch.assignmentId;
186	      }
187	      if (launch.kind === 'practice-set') {
188	        // The two values the runner uses to recognise an Intro to LR practice
189	        // set and map it back to its module-progress completion id.
190	        spec.practiceSource = launch.source ?? 'intro-to-lr-practice-drills';
191	        spec.practiceSlug = launch.slug;
192	      }
193	      if (launch.kind === 'bootcamp-day') {
194	        // Keeps the Run Record named by the day rather than by the list the
195	        // picker happened to draw.
196	        spec.resumeIdentity = {
197	          kind: 'bootcamp-day',
198	          day: launch.day,
199	          part: launch.part,
200	        };
201	      }
202	      return spec;
203	    }
204	  }
205	}
206	
207	/** The clock this run starts under. */
208	export function timerConfigForRunSpec(
209	  spec: DrillRunSpec | null | undefined,
210	): DrillTimerConfig | null {
211	  if (spec?.isGuidedDrill && spec.guidedDurationMinutes) {
212	    return { mode: 'countdown', durationMs: spec.guidedDurationMinutes * 60 * 1000 };
213	  }
214	
215	  if ((spec?.mode === 'type-drill' || spec?.mode === 'practice-set') && spec.config) {
216	    const config = spec.config as TypeDrillConfig;
217	    if (config.selectedQids && config.selectedQids.length > 0) {
218	      return { mode: 'stopwatch' };
219	    }
220	  }
221	
222	  if (spec?.mode === 'full-section' && spec.config) {
223	    const timer = (spec.config as FullSectionConfig).timer as TimerConfig;
224	
225	    if (timer.mode === 'unlimited') {
226	      return { mode: 'stopwatch' };
227	    }
228	
229	    let durationMs: number;
230	    switch (timer.mode) {
231	      case '35':
232	        durationMs = 35 * 60 * 1000;
233	        break;
234	      case '52.5':
235	        durationMs = 52.5 * 60 * 1000;
236	        break;
237	      case '70':
238	        durationMs = 70 * 60 * 1000;
239	        break;
240	      case 'custom':
241	        durationMs = (timer.customMinutes || 35) * 60 * 1000;
242	        break;
243	      default:
244	        durationMs = 35 * 60 * 1000;
245	    }
246	
247	    return { mode: 'countdown', durationMs };
248	  }
249	
250	  return { mode: 'stopwatch' };
251	}
252	

## assistant

Tool call: Bash
{"command": "cd \"C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\" && grep -n \"interface RunCarry\" -A 25 src/lib/drillLaunch.ts", "description": "Show RunCarry interface"}

## user

Tool result:
73:export interface RunCarry {
74-  mode: DrillMode;
75-  sealed: boolean;
76-  isGuidedDrill: boolean;
77-  guidedDurationMinutes?: number;
78-  /** A classroom homework assignment the list belongs to. */
79-  assignmentId?: string;
80-  guidedSetId?: string;
81-  guidedDrillId?: string;
82-  guidedAssignmentId?: string;
83-  practiceSource?: string;
84-  practiceSlug?: string;
85-  /** Names the Run Record for a bootcamp day rather than for the drawn list. */
86-  resumeIdentity?: DrillResumeIdentity;
87-  ptLeg?: PtLegRef;
88-}
89-
90-export type DrillLaunchBody =
91-  /** The app picks. One continuous adaptive run per student. */
92-  | { kind: 'smart-drill' }
93-  /** A real PT section, optionally timed and optionally sealed. */
94-  | {
95-      kind: 'section';
96-      pt: number;
97-      section: number;
98-      /**

## assistant

Tool call: Read
{"file_path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\src\\lib\\drillLaunch.ts", "offset": 200, "limit": 80}

## user

Tool result:
200	  if (values && values.length > 0) params.set(key, values.join(','));
201	}
202	
203	/**
204	 * Write a launch as a query string. Never needs to read anything: writing a
205	 * link is always possible from the launch alone, which is what lets `/drill`
206	 * canonicalize its own URL on arrival.
207	 *
208	 * Returns the query string without a leading `?`.
209	 */
210	export function launchDrill(launch: DrillLaunch): string {
211	  const p = new URLSearchParams();
212	  p.set('drill', launch.kind);
213	
214	  switch (launch.kind) {
215	    case 'smart-drill':
216	      break;
217	    case 'section':
218	      p.set('pt', String(launch.pt));
219	      p.set('section', String(launch.section));
220	      if (launch.timerMode) p.set('timer', launch.timerMode);
221	      if (launch.minutes) p.set('minutes', String(launch.minutes));
222	      if (launch.sealed) p.set('sealed', '1');
223	      if (launch.ptLeg) {
224	        p.set('runId', launch.ptLeg.runId);
225	        p.set('leg', String(launch.ptLeg.legIndex));
226	      }
227	      break;
228	    case 'saved-set':
229	      p.set('set', launch.setId);
230	      break;
231	    case 'assignment':
232	      p.set('assignment', launch.assignmentId);
233	      if (launch.guidedSetId) p.set('guidedSet', launch.guidedSetId);
234	      break;
235	    case 'guided-drill':
236	      if (launch.drillId) p.set('guidedDrill', launch.drillId);
237	      if (launch.assignmentId) p.set('assignment', launch.assignmentId);
238	      if (launch.durationMinutes) p.set('minutes', String(launch.durationMinutes));
239	      break;
240	    case 'practice-set':
241	      p.set('slug', launch.slug);
242	      if (launch.source) p.set('source', launch.source);
243	      break;
244	    case 'bootcamp-day':
245	      p.set('day', String(launch.day));
246	      p.set('part', launch.part);
247	      break;
248	    case 'questions': {
249	      p.set('qids', launch.qids.join(','));
250	      // The carry rides in its own params. It never reuses a param that
251	      // belongs to another kind, so a `questions` link cannot be mistaken for
252	      // a section or a guided drill it merely remembers the id of.
253	      const c = launch.carry;
254	      if (c) {
255	        if (c.mode !== 'type-drill') p.set('runMode', c.mode);
256	        if (c.sealed) p.set('runSealed', '1');
257	        if (c.isGuidedDrill) p.set('guided', '1');
258	        if (c.guidedDrillId) p.set('guidedDrill', c.guidedDrillId);
259	        if (c.guidedAssignmentId) p.set('guidedAssignment', c.guidedAssignmentId);
260	        if (c.guidedDurationMinutes) p.set('guidedMinutes', String(c.guidedDurationMinutes));
261	        if (c.assignmentId) p.set('assignment', c.assignmentId);
262	        if (c.guidedSetId) p.set('guidedSet', c.guidedSetId);
263	        if (c.practiceSource) p.set('source', c.practiceSource);
264	        if (c.practiceSlug) p.set('slug', c.practiceSlug);
265	        if (c.resumeIdentity) {
266	          p.set('day', String(c.resumeIdentity.day));
267	          p.set('part', c.resumeIdentity.part);
268	        }
269	        if (c.ptLeg) {
270	          p.set('runId', c.ptLeg.runId);
271	          p.set('leg', String(c.ptLeg.legIndex));
272	        }
273	      }
274	      break;
275	    }
276	    case 'filter':
277	      p.set('count', String(launch.count));
278	      setList(p, 'qtypes', launch.qtypes);
279	      setList(p, 'difficulties', launch.difficulties);

## assistant

## Summary

**1. Route `/classroom/:assignmentId`**

Renders `ClassroomAssignmentView` in `src/components/classroom/ClassroomRouteViews.tsx:469-551`, registered in `App.tsx:535-537`. The Start button (`onClick={start}`, handler at `ClassroomRouteViews.tsx:476-487`) is **not** a dead stub — it navigates to `/drill?mode=type-drill&qids=<assignment.question_qids>&assignmentId=<id>`. But this is the legacy "type-drill" launch grammar, which produces an untimed, unsealed practice-set run, not a real timed section.

**2. Testing Centre → real timed section**

`SectionSelector` picks pt+section, producing `FullSectionConfig {pt, section, timer}` (`src/types/drill.ts:17-21`). `TestingCentre.tsx:488-494` calls `navigate("/drill", { state: { mode: "full-section", config, returnTo: "/testing" } })` — via router `state`, not a qid list. The runner (`src/pages/Drill.tsx`, session init `~544-547`) for `full-section` calls `questionBank.getSection(config.pt, config.section)` to derive questions itself, and applies a real countdown timer. It needs `pt`+`section`+`TimerConfig`, not qids.

**3. One shared runner, two incompatible launch shapes**

There's no separate "SectionRunner" — `Drill.tsx`'s `DrillContent` handles every mode, driven by `useDrillRunSpec()` built from `src/lib/drillLaunch.ts` + `src/lib/drillRunSpec.ts`. A qid list *is* already accepted directly (`kind:'assignment'`/`'questions'` in `drillRunSpec.ts:126-144,162-181`), but `drillRunSpecFromLaunch` hardcodes those to `mode:'type-drill'`, and `timerConfigForRunSpec` (`drillRunSpec.ts:215-220`) forces `{mode:'stopwatch'}` whenever `selectedQids` is set. Only `kind:'section'` (numeric pt+section) reaches `mode:'full-section'` with a countdown/sealed experience.

**4. Minimal fix — files to touch**

- `src/lib/drillLaunch.ts`: give the `assignment` launch body/`RunCarry` a way to request timed+sealed presentation (encoder at `231-234` currently writes neither).
- `src/lib/drillRunSpec.ts`: stop hardcoding `mode:'type-drill'` in the `'assignment'` case (`162-181`); extend `timerConfigForRunSpec` (`208-251`) to give a qid-list run a real countdown, mirroring the existing guided-drill branch at `211-213`.
- `src/pages/Drill.tsx`: the `type-drill`+`selectedQids` branch (`553-579`) needs to honor that flag and behave like `full-section` (real `hasTimer`, `revealSealed`).
- `ClassroomRouteViews.tsx:476-487`: `start()` needs to set `sealed=1` and a timer param once the above exists.
