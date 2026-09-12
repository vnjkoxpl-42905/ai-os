/**
 * A preview harness for Classroom Home, the student dashboard. Development only.
 *
 * Mounts the presentational half (`ClassroomHomeView`) on the same
 * `.classroom-root > .classroom-stage > .classroom-column` frame the shell
 * draws, fed by a fixture instead of the student's record, so the page can be
 * screenshotted at real density without signing in. Built for the 2026-09-11
 * Claude Design handoff; also useful whenever the home is mid-edit.
 *
 * Not routed and not imported by the app. Reached at
 * `/src/dev/classroom-home-preview.html` on the dev server. Vite only builds
 * `index.html`, so it never ships.
 *
 * `?state=full|empty` · `?theme=dark` to render the dark classroom.
 */
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { ClassroomHomeView } from "../components/classroom/home/ClassroomHomeView";
import {
  buildWeek,
  weekDates,
  type ClassroomHomeModel,
  type HomeRow,
} from "../components/classroom/home/homeModel";
import "../index.css";
import "../components/classroom/classroom.css";
import "../components/classroom/home/home.css";

const params = new URLSearchParams(location.search);
const state = params.get("state") ?? "full";
if (params.get("theme") === "dark") document.documentElement.classList.add("dark");
else document.documentElement.classList.add("light");

const TODAY = new Date(2026, 8, 11); // Friday, September 11, 2026

const row = (r: Partial<HomeRow> & Pick<HomeRow, "key" | "title" | "route">): HomeRow => ({
  kind: "activity",
  tone: "activity",
  meta: "",
  actionLabel: "Open",
  emphasis: false,
  isNew: false,
  dueToday: false,
  overdue: false,
  ...r,
});

const NEGATION = row({
  key: "a",
  title: "Negation Station",
  meta: "Activity · twelve prompts · due today",
  route: "/activities/a",
  emphasis: true,
  isNew: true,
  dueToday: true,
  canComplete: true,
});

const ROWS: HomeRow[] = [
  NEGATION,
  row({
    key: "b",
    title: "Logical Reasoning · Timed Section",
    kind: "homework",
    tone: "drill",
    meta: "Homework · 25 questions · due Sunday",
    route: "/classroom/item/b",
  }),
  row({
    key: "c",
    title: "Main Conclusion Bootcamp",
    kind: "bootcamp",
    tone: "drill",
    meta: "Bootcamp · Part 3 of 5 · due Tuesday",
    route: "/bootcamps/main-conclusion",
    canComplete: true,
  }),
  row({
    key: "d",
    title: "Recap · Thursday's session",
    kind: "recap",
    tone: "recap",
    meta: "Recap · read before Friday",
    route: "/classroom/recaps/d",
    actionLabel: "Read",
    isNew: true,
  }),
];

const week = buildWeek(weekDates(TODAY), [], TODAY).map((day, i) => {
  const plan: Record<number, { label: string; route: string }> = {
    0: { label: "Negation Station", route: "/activities/a" },
    2: { label: "Timed Section", route: "/classroom/item/b" },
    4: { label: "Session with Joshua", route: "/schedule" },
    5: { label: "Main Conclusion", route: "/bootcamps/main-conclusion" },
  };
  const p = plan[i];
  return p ? { ...day, label: p.label, route: p.route } : day;
});

const EMPTY: ClassroomHomeModel = {
  greeting: "Good afternoon",
  displayName: "Ada",
  isAdmin: false,
  access: { messages: true, schedule: true, activities: true, drill: true },
  dateline: "Friday · September 11 · 2026",
  subtitle: "Nothing is due today. Drill whatever you feel like.",
  dueTodayCount: 0,
  hero: null,
  rows: [],
  newCount: 0,
  message: null,
  messages: [],
  unreadMessages: 0,
  session: null,
  booking: { label: "Book one", href: "/booking", external: false, detail: null },
  week: buildWeek(weekDates(TODAY), [], TODAY),
  weekLabel: "September 11 to 17",
};

const FULL: ClassroomHomeModel = {
  ...EMPTY,
  subtitle: "One assignment is due today. Two more this week.",
  dueTodayCount: 1,
  hero: {
    row: NEGATION,
    eyebrow: "START HERE",
    kindLabel: "ACTIVITY",
    meta: "twelve prompts · due today",
    prose: "Negate each statement, then check whether it breaks the argument.",
    primaryLabel: "Start the activity",
    progress: { completed: 4, total: 12, unit: "prompts", estimateMinutes: 18 },
  },
  rows: ROWS,
  newCount: 2,
  message: {
    id: "m",
    from: "Joshua",
    initial: "J",
    timeLabel: "7:52 a.m.",
    body: "Do the twelve before we meet. Watch the ones where the conclusion is hedged.",
    unread: true,
    route: "/inbox",
  },
  messages: [],
  unreadMessages: 1,
  session: {
    startsAt: "2026-09-15T16:00:00",
    durationMin: 60,
    label: "Tuesday, September 15 · 4:00 p.m.",
    meta: "60 minutes with Joshua · in four days",
  },
  booking: { label: "Book another", href: "/booking", external: false, detail: "3 credits left on your pass" },
  week,
};

const model = state === "empty" ? EMPTY : FULL;

createRoot(document.getElementById("root")!).render(
  <MemoryRouter>
    <div className="classroom-root">
      <main className="classroom-stage">
        <div className="classroom-column">
          <ClassroomHomeView
            model={model}
            loading={false}
            onOpen={() => {}}
            onSeeAllWork={() => {}}
            onMarkDone={() => {}}
            onClearMessage={() => {}}
            completingKey={null}
          />
        </div>
      </main>
    </div>
  </MemoryRouter>,
);
