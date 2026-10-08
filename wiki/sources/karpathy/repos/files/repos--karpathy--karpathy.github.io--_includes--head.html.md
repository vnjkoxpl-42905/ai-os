---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_includes/head.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_includes/head.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_includes/head.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_includes/head.html), SHA-256 `b1200490cbaf24a2f7bc062bf02888e1e90340a513feee76a7229f3a8f27e9f5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "<head> <meta charset=\"utf-8\"> <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> <title>{% if page.title %}{{ page.title }}{% else %}{{ site.title".

Jekyll config/includes/layouts define historical blog identity, RSS, canonical links, shared navigation/footer, conditional math and Disqus plus legacy analytics; these infrastructure templates do not supply personal reasoning beyond site metadata. CIFAR 2011 essay conducts a manual four-hundred-image human baseline near 94 percent, inspects ambiguous examples and training-neighbor coverage, distinguishes visual parts from contextual cues and explicitly labels conjectures. Its 2015 update admits the predicted 85-90 percent ceiling was wrong when systems reached about 95 percent, strong evidence to inspect data and revise forecasts. Computer Vision 2012 essay decomposes a humorous scale photograph into scene geometry, identities, physics, information access, social expectations and nested mental-state inference, arguing training data must support these mechanisms and speculating embodiment/interaction may matter. Historical AI inadequacy is dated 2012 perspective, not current canonical capability assessment. Both articles retain publication dates and foreign references; blog-domain duplicates should reconcile as alternate physical sources.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{% if page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}</title>
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="{{ site.description }}">
    <link rel="canonical" href="{{ page.url | replace:'index.html','' | prepend: site.baseurl | prepend: site.url }}">
    <link href="/feed.xml" type="application/atom+xml" rel="alternate" title="{{ site.title }} posts" />

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ "/css/main.css" | prepend: site.baseurl }}">

    <!-- Google Analytics -->
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-3698471-23', 'auto');
      ga('send', 'pageview');
    </script>

</head>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
