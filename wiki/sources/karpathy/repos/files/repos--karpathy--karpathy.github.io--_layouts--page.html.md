---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_layouts/page.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_layouts/page.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_layouts/page.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_layouts/page.html), SHA-256 `70c491f346acd0941a57f5778bb56aff81eec51661e0f9c4ebf1acfb3821b69d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
--- layout: default --- <div class="post"> <header class="post-header"> <h1>{{ page.title }}</h1> </header> <article class="post-content"> {{
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
  </header>

  <article class="post-content">
  {{ content }}
  </article>

  <!-- disqus comments -->
 {% if page.comments %}
 <div id="disqus_thread"></div>
  <script>
  /**
  *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
  *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
  var disqus_config = function () {
    this.page.url = "{{site.url}}{{page.url}}";  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = "{{page.url}}"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
  };
  (function() { // DON'T EDIT BELOW THIS LINE
  var d = document, s = d.createElement('script');
  s.src = 'https://karpathyblog.disqus.com/embed.js';
  s.setAttribute('data-timestamp', +new Date());
  (d.head || d.body).appendChild(s);
  })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  {% endif %}
  
</div>

<!-- mathjax -->
{% if page.mathjax %}
<script type="text/javascript" src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
