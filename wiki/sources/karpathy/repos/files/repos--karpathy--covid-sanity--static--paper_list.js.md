---
type: source
subject: "GitHub source repos/karpathy/covid-sanity/static/paper_list.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/static/paper_list.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/covid-sanity/static/paper_list.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/static/paper_list.js), SHA-256 `041800fa88e02089141f206db835b47f02748ee6f43335892969347f8e2c3839`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "'use strict'; const Tweet = props => { const t = props.tweet; const turl =".

Convnet neural-net specs verify desugared layer count, normalized probabilities, increased ground-truth probability after a small unregularized update and finite-difference input gradients; comments explicitly qualify step size and coverage. Specs were read, not run; analytic gradients are taken before an update and numeric losses afterward, a comparison limitation. Jasmine license/runner preserve third-party dependency provenance. Covid-sanity updater fetches BioRxiv collection, uses title-plus-abstract unigram TF-IDF, balanced exemplar SVM similarities and a weighted inverted search dictionary prioritizing title and authors. Flask loads local generated JSON, adapts changed author API schema to a legacy string, ranks optional tweets by follower count and returns at most forty search or latest papers with a small recency boost. React shows abstracts, PDF/similarity links and expandable tweets. Fixed-width styling and CDN/Babel template are historical implementation choices. Banned list excludes automated preprint accounts. No current API availability or deployed behavior verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
'use strict';

const Tweet = props => {
  const t = props.tweet;
  const turl = "https://twitter.com/" + t.name + "/status/" + t.id;
  return (
    <div class='tweet'>
      <a href={turl}><img src={t.image_url}></img></a>
      <div class='meta'>
        <span class="following">{t.followers}</span>
        <span class="uname"><a href={turl}>{t.name}</a></span>
        <span class="text">{t.text}</span>
      </div>
    </div>
  )
}

const Tweets = props => {
  const [collapsed, setCollapsed] = React.useState(true);
  return (
    //Make sure there are tweets.
    props.tweets.length > 0 && (
      collapsed ? (
          //Show just the summary statistics.
          <div class='rel_tweets_summary' onClick={() => setCollapsed(false)}>
            {props.tweets.length + " tweets"}
          </div>
        ) : (
          //Show tweets in expanded view.
          <div class='rel_tweets'>
            {props.tweets.map((jtweet, ix) => <Tweet key={ix} tweet={jtweet} />)}
          </div>
        )
    )
  );
}

const Paper = props => {
  const p = props.paper
  const url = p.rel_link + '.full.pdf';
  return (
    <div class={'rel_paper ' + p.rel_site}>
      <div class='dllinks'>
        <div class='metadata action'><a href={'/sim/' + p.rel_doi}>show similar</a></div>
        <div class='metadata action'><a href={url}>pdf</a></div>
        <div class='metadata rel_date'>{p.rel_date}</div>
      </div>
      <div class='rel_title'><a href={p.rel_link}>{p.rel_title}</a></div>
      <div class='rel_authors'>{p.rel_authors}</div>
      <div class='rel_abs'>{p.rel_abs}</div>
      <Tweets tweets={p.tweets} />
    </div>
  )
}

const PaperList = props => {
  const lst = props.papers;
  const plst = lst.map((jpaper, ix) => <Paper key={ix} paper={jpaper} />);
  const msg = {
    "latest": "Showing latest papers:",
    "sim": 'Showing papers most similar to the first one:',
    "search": 'Search results for "' + gvars.search_query + '":'
  }
  return (
    <div>
      <div id="info">{msg[gvars.sort_order]}</div>
      <div id="paperList" class="rel_papers">
        {plst}
      </div>
    </div>
  )
}

ReactDOM.render(<PaperList papers={papers} />, document.getElementById('wrap'));

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
