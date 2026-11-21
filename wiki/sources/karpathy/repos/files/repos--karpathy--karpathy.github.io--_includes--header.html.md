---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_includes/header.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_includes/header.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_includes/header.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_includes/header.html), SHA-256 `2285ab93f220650ea05f785bc3099199c641551d295bafb0b04b564b4fcd2fc9`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<header class="site-header"> <div class="wrap"> <div style="float:left; margin-top:10px; margin-right:10px;"> <a href="{{ "/feed.xml" | prepend: site.baseurl }}">
```

Jekyll config/includes/layouts define historical blog identity, RSS, canonical links, shared navigation/footer, conditional math and Disqus plus legacy analytics; these infrastructure templates do not supply personal reasoning beyond site metadata. CIFAR 2011 essay conducts a manual four-hundred-image human baseline near 94 percent, inspects ambiguous examples and training-neighbor coverage, distinguishes visual parts from contextual cues and explicitly labels conjectures. Its 2015 update admits the predicted 85-90 percent ceiling was wrong when systems reached about 95 percent, strong evidence to inspect data and revise forecasts. Computer Vision 2012 essay decomposes a humorous scale photograph into scene geometry, identities, physics, information access, social expectations and nested mental-state inference, arguing training data must support these mechanisms and speculating embodiment/interaction may matter. Historical AI inadequacy is dated 2012 perspective, not current canonical capability assessment. Both articles retain publication dates and foreign references; blog-domain duplicates should reconcile as alternate physical sources.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<header class="site-header">

  <div class="wrap">

    <div style="float:left; margin-top:10px; margin-right:10px;">
    <a href="{{ "/feed.xml" | prepend: site.baseurl }}">
      <img src="/assets/rssicon.svg" width="40">
    </a>
    </div>

    <a class="site-title" href="{{ site.baseurl }}/">{{ site.title }}</a>
    
    <nav class="site-nav">
      <a href="#" class="menu-icon">
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
           viewBox="0 0 18 15" enable-background="new 0 0 18 15" xml:space="preserve">
          <path fill="#505050" d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0
            h15.031C17.335,0,18,0.665,18,1.484L18,1.484z"/>
          <path fill="#505050" d="M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0c0-0.82,0.665-1.484,1.484-1.484
            h15.031C17.335,6.031,18,6.696,18,7.516L18,7.516z"/>
          <path fill="#505050" d="M18,13.516C18,14.335,17.335,15,16.516,15H1.484C0.665,15,0,14.335,0,13.516l0,0
            c0-0.82,0.665-1.484,1.484-1.484h15.031C17.335,12.031,18,12.696,18,13.516L18,13.516z"/>
        </svg>
      </a>
      <div class="trigger">
        {% for page in site.pages %}
          {% if page.title and page.includelink %}<a class="page-link" href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>{% endif %}
        {% endfor %}
      </div>
    </nav>
  </div>

</header>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
