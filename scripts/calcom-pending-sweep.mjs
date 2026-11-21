#!/usr/bin/env node
// Report pending Cal.com bookings for review. Pending status alone does not prove
// a failed payment. Confirm payment state before explicitly authorizing cancellation.
// Read pagination contract: https://cal.com/docs/api-reference/v2/bookings/get-all-bookings
//
//   node scripts/calcom-pending-sweep.mjs           # report
//   node scripts/calcom-pending-sweep.mjs --cancel  # also release future slots
//
// Needs CALCOM_API_KEY in .env. API v2 only — v1 is decommissioned.

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, resolve } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
async function main() {
  const env = Object.fromEntries(
    readFileSync(join(root, ".env"), "utf8")
      .split("\n")
      .filter((l) => l.trim() && !l.trim().startsWith("#") && l.includes("="))
      .map((l) => [l.slice(0, l.indexOf("=")).trim(), l.slice(l.indexOf("=") + 1).trim()])
  );

  const KEY = process.env.CALCOM_API_KEY || env.CALCOM_API_KEY;
  if (!KEY) { console.error("CALCOM_API_KEY missing from .env"); process.exit(1); }

  const api = createApi(KEY);

  const ET = (iso) =>
    new Date(iso).toLocaleString("en-US", {
      timeZone: "America/Toronto", year: "numeric", month: "short",
      day: "numeric", hour: "numeric", minute: "2-digit",
    });

  const pending = await collectPending(api);

  if (!pending.length) { console.log("No pending bookings found in the completed upcoming/past sweep."); return; }

  const now = Date.now();
  const future = pending.filter((b) => new Date(b.start).getTime() > now);

  console.log(`${pending.length} pending booking(s); ${future.length} future booking(s) require payment/status review\n`);
  for (const b of pending) {
    const who = (b.attendees || []).map((a) => a.email).join(", ");
    const holding = new Date(b.start).getTime() > now ? "  << FUTURE PENDING" : "";
    console.log(`  ${ET(b.start).padEnd(26)} ${who.padEnd(34)} ${b.uid}${holding}`);
  }

  if (!process.argv.includes("--cancel")) {
    if (future.length) console.log(`\nReview payment state before explicitly authorizing --cancel for ${future.length} booking(s).`);
    console.log("Past-dated ones block no future slot.");
    return;
  }

  console.log("\nCancelling future pending bookings:");
  for (const b of future) {
    await api(`/bookings/${encodeURIComponent(b.uid)}/cancel`, {
      method: "POST",
      body: JSON.stringify({ cancellationReason: "Unpaid — payment window expired. Slot released." }),
      headers: { "cal-api-version": "2024-08-13" },
    });
    console.log(`  ${b.uid}  released`);
  }
  console.log("\nStudents must rebook to get a fresh payment link.");
}

export function createApi(key, fetchImpl = fetch) {
  return async (path, init = {}) => {
    const response = await fetchImpl(`https://api.cal.com/v2${path}`, {
      ...init,
      signal: init.signal ?? AbortSignal.timeout(30000),
      headers: {
        Authorization: `Bearer ${key}`,
        "cal-api-version": "2026-05-01",
        "Content-Type": "application/json",
        ...init.headers,
      },
    });
    if (!response.ok) throw new Error(`Cal.com HTTP ${response.status} for ${init.method ?? "GET"} ${path.split("?")[0]}`);
    let payload;
    try { payload = await response.json(); }
    catch { throw new Error("Cal.com returned invalid JSON"); }
    if (!payload || payload.status !== "success") throw new Error("Cal.com did not report API success");
    return payload;
  };
}

export async function collectPending(api, { maxPages = 100 } = {}) {
  const pending = new Map();
  for (const status of ["upcoming", "past"]) {
    let cursor;
    const seen = new Set();
    for (let page = 0; ; page++) {
      if (page >= maxPages) throw new Error(`Cal.com ${status} pagination exceeded ${maxPages} pages; sweep incomplete`);
      const query = new URLSearchParams({ status, take: "100" });
      if (cursor) query.set("cursor", cursor);
      const result = await api(`/bookings?${query}`);
      if (!Array.isArray(result.data) || typeof result.pagination?.hasMore !== "boolean") throw new Error("Malformed Cal.com bookings/pagination response; sweep incomplete");
      for (const booking of result.data) {
        if (!booking || typeof booking.status !== "string" || typeof booking.uid !== "string" || !booking.uid || !Number.isFinite(Date.parse(booking.start))) throw new Error("Malformed Cal.com booking; sweep incomplete");
        if (booking.status === "pending") pending.set(booking.uid, booking);
      }
      if (!result.pagination.hasMore) break;
      const next = result.pagination.nextCursor;
      if (typeof next !== "string" || !next || seen.has(next)) throw new Error("Invalid or repeated Cal.com pagination cursor; sweep incomplete");
      seen.add(next);
      cursor = next;
    }
  }
  return [...pending.values()];
}

if (process.argv[1] && fileURLToPath(import.meta.url) === resolve(process.argv[1])) {
  main().catch((error) => {
    // Only our bounded diagnostics are printed. API bodies and tokens stay private.
    if (/^(Cal\.com |Malformed Cal\.com |Invalid or repeated Cal\.com )/.test(error.message)) console.error(error.message);
    console.error("Cal.com sweep failed or was incomplete. No zero-booking conclusion can be drawn; check authentication, API schema, network and pagination.");
    process.exitCode = 1;
  });
}
