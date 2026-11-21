---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_layouts/post.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_layouts/post.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_layouts/post.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_layouts/post.html), SHA-256 `8423fc58140d9e68c9c836f2b913a485c853ef29f603e1808331f2ad27f19849`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
--- layout: default --- <div class="post"> <header class="post-header"> <h1>{{ page.title }}</h1> <p class="meta">{{ page.date |
```

Jekyll config/includes/layouts define historical blog identity, RSS, canonical links, shared navigation/footer, conditional math and Disqus plus legacy analytics; these infrastructure templates do not supply personal reasoning beyond site metadata. CIFAR 2011 essay conducts a manual four-hundred-image human baseline near 94 percent, inspects ambiguous examples and training-neighbor coverage, distinguishes visual parts from contextual cues and explicitly labels conjectures. Its 2015 update admits the predicted 85-90 percent ceiling was wrong when systems reached about 95 percent, strong evidence to inspect data and revise forecasts. Computer Vision 2012 essay decomposes a humorous scale photograph into scene geometry, identities, physics, information access, social expectations and nested mental-state inference, arguing training data must support these mechanisms and speculating embodiment/interaction may matter. Historical AI inadequacy is dated 2012 perspective, not current canonical capability assessment. Both articles retain publication dates and foreign references; blog-domain duplicates should reconcile as alternate physical sources.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
---
layout: default
---
<div class="post">

  <header class="post-header">
    <h1>{{ page.title }}</h1>
    <p class="meta">{{ page.date | date: "%b %-d, %Y" }}{% if page.author %} • {{ page.author }}{% endif %}{% if page.meta %} • {{ page.meta }}{% endif %}</p>
  </header>

  <article class="post-content">
  {{ content }}
  </article>

  <!-- mathjax -->
  {% if page.mathjax %}
  <script type="text/javascript" src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  {% endif %}
  
  <!-- disqus comments -->
 {% if page.comments %}
 <div id="disqus_thread"></div>
  <script type="text/javascript">
      /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
      var disqus_shortname = 'karpathyblog'; // required: replace example with your forum shortname

      /* * * DON'T EDIT BELOW THIS LINE * * */
      (function() {
          var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
  {% endif %}
  
</div>
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
