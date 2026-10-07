#!/usr/bin/env node
// Find cal.com bookings stuck at "pending" — a student filled the booking form but
// never finished Stripe checkout. The payment link holds the slot for 30 minutes and
// then dies; it CANNOT be re-sent (the uuid is not stored on the booking and API v2
// has no payments endpoint). Meanwhile the dead booking keeps holding the slot.
//
// cal.com sends no host notification for these, so they are invisible without this check.
//
//   node scripts/calcom-pending-sweep.mjs           # report
//   node scripts/calcom-pending-sweep.mjs --cancel  # also release future slots
//
// Needs CALCOM_API_KEY in .env. API v2 only — v1 is decommissioned.

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const env = Object.fromEntries(
  readFileSync(join(root, ".env"), "utf8")
    .split("\n")
    .filter((l) => l.trim() && !l.trim().startsWith("#") && l.includes("="))
    .map((l) => [l.slice(0, l.indexOf("=")).trim(), l.slice(l.indexOf("=") + 1).trim()])
);

const KEY = process.env.CALCOM_API_KEY || env.CALCOM_API_KEY;
if (!KEY) { console.error("CALCOM_API_KEY missing from .env"); process.exit(1); }

const api = (path, init = {}) =>
  fetch(`https://api.cal.com/v2${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${KEY}`,
      "cal-api-version": "2024-08-13",
      "Content-Type": "application/json",
      ...init.headers,
    },
  }).then((r) => r.json());

const ET = (iso) =>
  new Date(iso).toLocaleString("en-US", {
    timeZone: "America/Toronto", year: "numeric", month: "short",
    day: "numeric", hour: "numeric", minute: "2-digit",
  });

const pending = [];
for (const status of ["upcoming", "past"]) {
  const res = await api(`/bookings?status=${status}&take=100`);
  for (const b of res.data || []) if (b.status === "pending") pending.push(b);
}

if (!pending.length) { console.log("No stuck pending bookings. Nothing holding a slot."); process.exit(0); }

const now = Date.now();
const future = pending.filter((b) => new Date(b.start).getTime() > now);

console.log(`${pending.length} unpaid booking(s); ${future.length} still holding a future slot\n`);
for (const b of pending) {
  const who = (b.attendees || []).map((a) => a.email).join(", ");
  const holding = new Date(b.start).getTime() > now ? "  << HOLDING A SLOT" : "";
  console.log(`  ${ET(b.start).padEnd(26)} ${who.padEnd(34)} ${b.uid}${holding}`);
}

if (!process.argv.includes("--cancel")) {
  if (future.length) console.log(`\nRe-run with --cancel to release ${future.length} slot(s).`);
  console.log("Past-dated ones cannot be cancelled by cal.com and block nothing — leave them.");
  process.exit(0);
}

console.log("\nCancelling future unpaid bookings:");
for (const b of future) {
  const res = await api(`/bookings/${b.uid}/cancel`, {
    method: "POST",
    body: JSON.stringify({ cancellationReason: "Unpaid — payment window expired. Slot released." }),
  });
  console.log(`  ${b.uid}  ${res.status === "success" ? "released" : "FAILED: " + JSON.stringify(res.error).slice(0, 90)}`);
}
console.log("\nStudents must rebook to get a fresh 30-minute payment link.");
