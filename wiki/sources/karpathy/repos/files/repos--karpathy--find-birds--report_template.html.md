---
type: source
subject: "GitHub source repos/karpathy/find-birds/report_template.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/report_template.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/find-birds/report_template.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/report_template.html), SHA-256 `66c902c5697e2c0a0049b01ab3c0ed1b867f92bff9705fc4edc42ff90a1ab2a4`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "<!doctype html> <html lang=\"en\"> <head> <meta charset=\"utf-8\"> <title>find-birds report page!!</title> <style> body { margin: 0;".

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>find-birds report page!!</title>

<style>
body {
    margin: 0;
    padding: 0;
    font-family: Arial, Helvetica, sans-serif;
}
#header {
    height: 80px;
    background-color: #F55555;
    text-align: center;
    font-size: 40px;
    color: white;
    padding-top: 40px;
    margin-bottom: 20px;
}
#meat {
    margin-left: 20px;
}
th, td {
    margin: 0;
    padding: 4px 10px 4px 10px;
}
tr:nth-child(even) {
    background-color: #f2f2f2;
}
th {
    background-color: #4CAF50;
    color: white;
}

</style>
</head>

<body>

<!-- header -->
<div id="header">
    find-birds!
</div>

<!-- meat -->
<div id="meat">
MEAT_GOES_HERE
</div>

</body>

</html>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
