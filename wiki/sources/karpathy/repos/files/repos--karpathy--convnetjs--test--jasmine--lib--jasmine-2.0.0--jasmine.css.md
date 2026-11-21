---
type: source
subject: "GitHub source repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.css), SHA-256 `5524d9a97ad70bf8894ce52da065b97fb1d0db231e001cf05aaddf8f43f542a2`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
body { background-color: #eeeeee; padding: 0; margin: 5px; overflow-y: scroll; } .html-reporter { font-size: 11px;
```

These three sources are vendored Jasmine 2.0 reporter code and CSS, credited to Pivotal Labs, not Karpathy authored reasoning. ConsoleReporter tracks passed, failed and pending specs, prints detailed stacks, elapsed time and a completion callback. HTML reporter builds a suite/spec results tree, exception toggle, failure details and query-string filtering; spec filter escapes regex metacharacters, and query parser normalizes boolean strings. CSS encodes passed/failed/pending status and report visibility. Retained as dependency evidence without deriving persona or engineering rules from third-party implementation. Complete text read, no test execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
body { background-color: #eeeeee; padding: 0; margin: 5px; overflow-y: scroll; }

.html-reporter { font-size: 11px; font-family: Monaco, "Lucida Console", monospace; line-height: 14px; color: #333333; }
.html-reporter a { text-decoration: none; }
.html-reporter a:hover { text-decoration: underline; }
.html-reporter p, .html-reporter h1, .html-reporter h2, .html-reporter h3, .html-reporter h4, .html-reporter h5, .html-reporter h6 { margin: 0; line-height: 14px; }
.html-reporter .banner, .html-reporter .symbol-summary, .html-reporter .summary, .html-reporter .result-message, .html-reporter .spec .description, .html-reporter .spec-detail .description, .html-reporter .alert .bar, .html-reporter .stack-trace { padding-left: 9px; padding-right: 9px; }
.html-reporter .banner .version { margin-left: 14px; }
.html-reporter #jasmine_content { position: fixed; right: 100%; }
.html-reporter .version { color: #aaaaaa; }
.html-reporter .banner { margin-top: 14px; }
.html-reporter .duration { color: #aaaaaa; float: right; }
.html-reporter .symbol-summary { overflow: hidden; *zoom: 1; margin: 14px 0; }
.html-reporter .symbol-summary li { display: inline-block; height: 8px; width: 14px; font-size: 16px; }
.html-reporter .symbol-summary li.passed { font-size: 14px; }
.html-reporter .symbol-summary li.passed:before { color: #5e7d00; content: "\02022"; }
.html-reporter .symbol-summary li.failed { line-height: 9px; }
.html-reporter .symbol-summary li.failed:before { color: #b03911; content: "x"; font-weight: bold; margin-left: -1px; }
.html-reporter .symbol-summary li.disabled { font-size: 14px; }
.html-reporter .symbol-summary li.disabled:before { color: #bababa; content: "\02022"; }
.html-reporter .symbol-summary li.pending { line-height: 17px; }
.html-reporter .symbol-summary li.pending:before { color: #ba9d37; content: "*"; }
.html-reporter .exceptions { color: #fff; float: right; margin-top: 5px; margin-right: 5px; }
.html-reporter .bar { line-height: 28px; font-size: 14px; display: block; color: #eee; }
.html-reporter .bar.failed { background-color: #b03911; }
.html-reporter .bar.passed { background-color: #a6b779; }
.html-reporter .bar.skipped { background-color: #bababa; }
.html-reporter .bar.menu { background-color: #fff; color: #aaaaaa; }
.html-reporter .bar.menu a { color: #333333; }
.html-reporter .bar a { color: white; }
.html-reporter.spec-list .bar.menu.failure-list, .html-reporter.spec-list .results .failures { display: none; }
.html-reporter.failure-list .bar.menu.spec-list, .html-reporter.failure-list .summary { display: none; }
.html-reporter .running-alert { background-color: #666666; }
.html-reporter .results { margin-top: 14px; }
.html-reporter.showDetails .summaryMenuItem { font-weight: normal; text-decoration: inherit; }
.html-reporter.showDetails .summaryMenuItem:hover { text-decoration: underline; }
.html-reporter.showDetails .detailsMenuItem { font-weight: bold; text-decoration: underline; }
.html-reporter.showDetails .summary { display: none; }
.html-reporter.showDetails #details { display: block; }
.html-reporter .summaryMenuItem { font-weight: bold; text-decoration: underline; }
.html-reporter .summary { margin-top: 14px; }
.html-reporter .summary ul { list-style-type: none; margin-left: 14px; padding-top: 0; padding-left: 0; }
.html-reporter .summary ul.suite { margin-top: 7px; margin-bottom: 7px; }
.html-reporter .summary li.passed a { color: #5e7d00; }
.html-reporter .summary li.failed a { color: #b03911; }
.html-reporter .summary li.pending a { color: #ba9d37; }
.html-reporter .description + .suite { margin-top: 0; }
.html-reporter .suite { margin-top: 14px; }
.html-reporter .suite a { color: #333333; }
.html-reporter .failures .spec-detail { margin-bottom: 28px; }
.html-reporter .failures .spec-detail .description { background-color: #b03911; }
.html-reporter .failures .spec-detail .description a { color: white; }
.html-reporter .result-message { padding-top: 14px; color: #333333; white-space: pre; }
.html-reporter .result-message span.result { display: block; }
.html-reporter .stack-trace { margin: 5px 0 0 0; max-height: 224px; overflow: auto; line-height: 18px; color: #666666; border: 1px solid #ddd; background: white; white-space: pre; }

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
