---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/feed.xml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/feed.xml]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/feed.xml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/feed.xml), SHA-256 `10feb472ba6b07a8b707d45dcc37284e4e1ac55960dab6c0b4035be331648bbc`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "--- layout: none --- <?xml version=\"1.0\" encoding=\"UTF-8\"?> <rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\"> <channel> <title>{{ site.title | xml_escape".

All four site presentation assets fully read. RSS icon is Inkscape SVG with public-domain RDF metadata and unnamed creator, orange square and white signal geometry, not authored philosophy. main.css includes baseline reset, centered 800px column, article/code typography and highlighting, custom image captions and responsive footer/nav breakpoints; hover-only small-screen navigation is historical implementation rather than accessibility recommendation. RSS Liquid template escapes text and emits latest ten full-content posts with dates, tags, categories and canonical links. Index loops all posts showing date, title and excerpt. Site infrastructure provenance only, no independent persona principles.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
---
layout: none
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{{ site.title | xml_escape }}</title>
    <description>{{ site.description | xml_escape }}</description>
    <link>{{ site.url }}{{ site.baseurl }}/</link>
    <atom:link href="{{ "/feed.xml" | prepend: site.baseurl | prepend: site.url }}" rel="self" type="application/rss+xml" />
    <pubDate>{{ site.time | date_to_rfc822 }}</pubDate>
    <lastBuildDate>{{ site.time | date_to_rfc822 }}</lastBuildDate>
    <generator>Jekyll v{{ jekyll.version }}</generator>
    {% for post in site.posts limit:10 %}
      <item>
        <title>{{ post.title | xml_escape }}</title>
        <description>{{ post.content | xml_escape }}</description>
        <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>
        <link>{{ post.url | prepend: site.baseurl | prepend: site.url }}</link>
        <guid isPermaLink="true">{{ post.url | prepend: site.baseurl | prepend: site.url }}</guid>
        {% for tag in post.tags %}
        <category>{{ tag | xml_escape }}</category>
        {% endfor %}
        {% for cat in post.categories %}
        <category>{{ cat | xml_escape }}</category>
        {% endfor %}
      </item>
    {% endfor %}
  </channel>
</rss>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
