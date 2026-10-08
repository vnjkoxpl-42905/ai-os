---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/static/word_list.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/word_list.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/static/word_list.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/word_list.js), SHA-256 `972e1741d73c5677b43b55257e5086cdab4e0c637feecfdd4691bc0f2fbd6a01`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "'use strict'; const Word = props => { const p = props.word; // word, weight,".

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
'use strict';

const Word = props => {
    const p = props.word;
    // word, weight, idf
    return (
    <div class='rel_word'>
        <div class='rel_word_weight'>{p.weight.toFixed(2)}</div>
        {/* <div class='rel_word_idf'>{p.idf.toFixed(2)}</div> */}
        <div class="rel_word_txt">{p.word}</div>
    </div>
    )
}

const WordList = props => {
    const lst = props.words;
    const words_desc = props.words_desc;
    const wlst = lst.map((jword, ix) => <Word key={ix} word={jword} />);
    return (
        <div>
            <div>{words_desc}</div>
            <div id="wordList" class="rel_words">
                {wlst}
            </div>
        </div>
    )
}

var elt = document.getElementById('wordwrap');
if(elt) {
    ReactDOM.render(<WordList words={words} words_desc={words_desc} />, elt);
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
