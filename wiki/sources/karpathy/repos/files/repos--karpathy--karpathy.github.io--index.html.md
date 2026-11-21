---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/index.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/index.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/index.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/index.html), SHA-256 `0faffd72b704e909f06b130a0036012969eccf0e4349511783b87e512bcb2ca6`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
--- layout: default --- <div class="home"> <ul class="posts"> {% for post in site.posts %} <li>
```

All four site presentation assets fully read. RSS icon is Inkscape SVG with public-domain RDF metadata and unnamed creator, orange square and white signal geometry, not authored philosophy. main.css includes baseline reset, centered 800px column, article/code typography and highlighting, custom image captions and responsive footer/nav breakpoints; hover-only small-screen navigation is historical implementation rather than accessibility recommendation. RSS Liquid template escapes text and emits latest ten full-content posts with dates, tags, categories and canonical links. Index loops all posts showing date, title and excerpt. Site infrastructure provenance only, no independent persona principles.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
---
layout: default
---

<div class="home">
  
  <ul class="posts">
    {% for post in site.posts %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        <br>
        {{ post.excerpt }}
      </li>
    {% endfor %}
  </ul>

</div>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
