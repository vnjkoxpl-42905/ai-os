---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/static/style.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/style.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/static/style.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/style.css), SHA-256 `9ee950bca156cab6d5229c9836354e87c82f49147c78021169015b430f44cb87`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "body { margin: 0; padding: 0; font-family: sans-serif; line-height: 1.2; background-color: #eee; } #header {".

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    line-height: 1.2;
    background-color: #eee;
}
#header {
    height: 24px;
    background-color: #840000;
    color: white;
    padding-top: 8px;
    padding-left: 10px;
    border-bottom: 1px solid #622;
}
#home-link {
    display: inline-block;
 }
 #stats-link {
    float: right;
    margin: 0 10px 0 10px;
 }
 #login-link {
    float: right;
    margin: 0 10px 0 10px;
 }
#controls {
    margin: 10px 40px 0 40px;
    background-color: #eee;
}
#wrap {
    margin: 10px 40px 0 40px;
    font-size: 18px;
}
#tagwrap {
    margin: 10px 40px 0 40px;
    font-size: 18px;
}
#wordwrap {
    margin: 10px 40px 0 40px;
    font-size: 14px;
}
.rel_title {
    display: inline-block;
}

.rel_title a {
    color: #844;
}

.rel_paper {
    margin-bottom: 10px;
    padding: 10px;
    background-color: white;
    border-radius: 5px;
}

.rel_score {
    display: inline-block;
    margin-right: 6px;
    font-weight: bold;
}
.rel_authors {
    font-style: italic;
    font-size: 16px;
}
.rel_time {
    color: #050;
    display: inline-block;
    font-size: 16px;
}
.rel_abs {
    color: #333;
    font-size: 14px;
}
.rel_tags {
    color: #009;
    font-size: 16px;
    display: inline-block;
    margin-left: 5px;
}
.rel_tag { /* deletes a whole tag */
    position: absolute;
    color: white;
    left: 7px;
    cursor: pointer;
    text-align: center;
    border-radius: 3px;
    background-color: #f55;
    width: 22px;
    height: 22px;
}
.rel_utag { /* shows an active tag for a paper */
    background-color: #009;
    color: #fff;
    font-size: 16px;
    display: inline-block;
    margin-right: 5px;
    padding: 0 4px 0 4px;
    border-radius: 4px;
    cursor: pointer;
}
.rel_utag_all { /* distinguishes the special 'all' tag from others */
    background-color: #909;
}
.rel_utag_add { /* adds a paper to a tag */
    background-color: #55f;
    margin-right: 2px;
    width: 12px;
    text-align: center;
}
.rel_utag_sub { /* subs a tag from a paper */
    background-color: #f55;
    width: 12px;
    text-align: center;
}
.rel_utag a {
    color: white;
    text-decoration: none;
}
.rel more {
    font-size: 10px;
}
#sbox {
    width: 100%;
}
#qfield {
    width: 100%;
    box-sizing: border-box;

    height: 40px;
    font-size: 22px;

    border: solid 1px #999;
    color: "#333";

    padding-left: 50px;

    background-image: url('/static/search.png');
    background-repeat: no-repeat;
    background-position: left center;
    outline: 0;
  }
#cbox {
    margin-top: 5px;
    font-size: 14px;
}
#cbox input {
    margin-bottom: 5px;
}
#cbox_fast {
    font-size: 14px;
}
#cbox_fast a {
    display: inline-block;
    background-color: #eee;
    padding: 3px;
}
#header a{
    color: white;
    text-decoration: none;
}
.rel_more {
    font-size: 14px;
    display: inline-block;
    margin-right: 10px;
}
.rel_inspect {
    font-size: 14px;
    display: inline-block;
    margin-right: 10px;
}
#wordList {
    margin-top: 5px;
    margin-bottom: 10px;
}
.rel_word {
    display: inline-block;
    background-color: #eef;
    padding: 2px;
    margin: 2px;
}
.rel_word_weight {
    display: inline-block;
    color: #009;
}
.rel_word_idf {
    display: inline-block;
    margin-left: 5px;
}
.rel_word_txt {
    display: inline-block;
    margin-left: 5px;
}
#profile-warning {
    margin: 10px;
    padding: 10px;
    font-size: 16px;
    background-color: #fdd;
    border-radius: 5px;
}
#profile-warning p {
    margin: 0;
    padding: 0;
}
#profile-login-form, #email-form {
    max-width: 400px;
    margin: 30px auto;
    font-size: 18px;
}
#profile-login-form .form-control, #email-form .form-control {
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin: 5px 0 10px 0;
    padding: 5px;
    height: 34px;
    font-size: 16px;
    line-height: 1.42857143;
    color: #555;
    border: 1px solid #ccc;
    border-radius: 4px;
}
#profile-login-form .btn, #email-form .btn {
    display: block;
    width: 100%;
    padding: 5px;
    margin: 0;
    height: 34px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #fff;
    background-color: #337ab7;
    border: 1px solid #2e6da4;
    border-radius: 4px;
    cursor: pointer;
}
#log-fun-warn {
    text-align: center;
    background-color: #ffd;
    color: #777;
    font-size: 14px;
    padding: 3px;
}
#statswrap {
    margin: 10px 40px 0 40px;
    font-size: 16px;
}
#profilewrap {
    margin: 10px 40px 0 40px;
    font-size: 16px;
}
#aboutwrap {
    margin: 10px 40px 0 40px;
    font-size: 16px;
}
#tags_field {
    width: 100px;
}
#pid_field {
    width: 60px;
}
#time_filter_field {
    width: 20px;
}
#page_number_field {
    width: 20px;
}
#svm_c_field {
    width: 30px;
}
#tagList {
    display: inline-block;
}
#inspect_svm {
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    text-decoration: underline;
    color: #009;
}
@media only screen and (max-width: 720px) {
    #controls, #wrap, #profilewrap, #wordwrap, #aboutwrap, #statswrap {
		margin: 10px 20px 0 20px;
	}

}
#pagination {
    text-align: center;
    margin-bottom: 20px;
}
#link-prev-page, #link-next-page {
    margin: 0 5px 0 5px;
    font-size: 16px;
    cursor: pointer;
    color: #009;
    text-decoration: underline;
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
