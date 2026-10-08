import test from "node:test";
import assert from "node:assert/strict";
import { createApi, collectPending } from "./calcom-pending-sweep.mjs";

const page = (data = [], hasMore = false, nextCursor = null) => ({ status: "success", data, pagination: { hasMore, nextCursor } });
const booking = (uid) => ({ uid, status: "pending", start: "2026-10-10T12:00:00Z" });

test("HTTP/auth, malformed JSON and API failures reject rather than imply empty", async () => {
  for (const response of [
    { ok: false, status: 401 },
    { ok: true, json: async () => { throw new Error("invalid"); } },
    { ok: true, json: async () => ({ status: "error" }) },
  ]) await assert.rejects(createApi("fixture", async () => response)("/bookings"));
});

test("cursor pagination includes later records and deduplicates across statuses", async () => {
  const paths = [];
  const responses = [page([booking("a")], true, "second"), page([booking("b")]), page([booking("a")])];
  const result = await collectPending(async (path) => { paths.push(path); return responses.shift(); });
  assert.deepEqual(result.map((b) => b.uid), ["a", "b"]);
  assert.match(paths[1], /cursor=second/);
  assert.match(paths[2], /status=past/);
});

test("valid complete empty sweep succeeds", async () => {
  assert.deepEqual(await collectPending(async () => page()), []);
});

test("missing data/pagination, bad booking, repeated cursor and page limit fail closed", async () => {
  for (const response of [{ status: "success" }, { data: [] }, page([{}]), page([], true, null)]) {
    await assert.rejects(collectPending(async () => response));
  }
  await assert.rejects(collectPending(async () => page([], true, "repeat")), /repeated/);
  let cursor = 0;
  await assert.rejects(collectPending(async () => page([], true, String(++cursor)), { maxPages: 2 }), /exceeded/);
});

test("API client pins documented list version and sends only explicit method", async () => {
  let options;
  await createApi("fixture", async (_, init) => { options = init; return { ok: true, json: async () => page() }; })("/bookings");
  assert.equal(options.headers["cal-api-version"], "2026-05-01");
  assert.equal(options.method, undefined);
});
