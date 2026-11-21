[Skip to main content](https://gwern.net/sidenote#markdownBody)

[CSS](https://gwern.net/doc/cs/css/index "Link to cs/css tag index"), [JS](https://gwern.net/doc/cs/js/index "Link to cs/js tag index"), [typography](https://gwern.net/doc/design/typography/index "Link to design/typography tag index")

In typography/design, ‘sidenotes’ place footnotes/endnotes in the margins for easier reading. I discuss design choices, HTML implementations and their pros/cons.

2020-08-06–4y2025-04-06_finished_[certainty](https://gwern.net/about#confidence-tags "Explanation of 'confidence' metadata: probability of overall being meaningfully correct, expressed as Kesselman Estimative Words (ranging 0–100%: 'certain'/'highly likely'/'likely'/'possible'/'unlikely'/'highly unlikely'/'remote'/'impossible')"): _certain_[importance](https://gwern.net/about#importance-tags "Explanation of 'importance' metadata: rating 1–10 about how much a topic matters to the world (‘N/A’ = unknown or unrateable)."): _2_[backlinks⁠](https://gwern.net/sidenote#backlinks "Reverse citations/backlinks for this page (the list of other pages which link to this page).")[similar⁠](https://gwern.net/sidenote#similars "Similar links for this link (by text embedding).")[bibliography⁠](https://gwern.net/sidenote#link-bibliography "Bibliography of links cited in this page (forward citations).")

- [Examples](https://gwern.net/sidenote#examples)
- [Implementation Strategies](https://gwern.net/sidenote#implementation-strategies)
- [Comparison](https://gwern.net/sidenote#comparison)
- [Implementations](https://gwern.net/sidenote#implementations)
  - [Tufte-CSS](https://gwern.net/sidenote#tufte-css)
  - [`sidenotes.js`](https://gwern.net/sidenote#sidenotes-js)
    - [Sidebar Tables](https://gwern.net/sidenote#sidebar-tables)
  - [Ink & Switch](https://gwern.net/sidenote#ink-switch)
  - [Robert Nystrom](https://gwern.net/sidenote#robert-nystrom)
  - [Matthew Butterick](https://gwern.net/sidenote#matthew-butterick)
  - [Koos Looijesteijn](https://gwern.net/sidenote#koos-looijesteijn)
  - [Harvard Law Review](https://gwern.net/sidenote#harvard-law-review)
  - [Yale Law Journal](https://gwern.net/sidenote#yale-law-journal)
  - [Knight Institute](https://gwern.net/sidenote#knight-institute)
  - [_New York_](https://gwern.net/sidenote#new-york)
  - [JQuery.sidenotes](https://gwern.net/sidenote#jquery-sidenotes)
  - [Sidenotes.js, Correia](https://gwern.net/sidenote#sidenotes-js-correia)
  - [_The India Forum_](https://gwern.net/sidenote#the-india-forum)
  - [Tables](https://gwern.net/sidenote#tables)
  - [Annotate, Molly White](https://gwern.net/sidenote#annotate-molly-white)
  - [George Pollard](https://gwern.net/sidenote#george-pollard)
  - [Miscellaneous](https://gwern.net/sidenote#miscellaneous)
- [See Also](https://gwern.net/sidenote#see-also)
- [External Links](https://gwern.net/sidenote#external-links)
- [Footnotes](https://gwern.net/sidenote#footnotes)
- [Backlinks](https://gwern.net/sidenote#backlinks-section)
- [Similar Links](https://gwern.net/sidenote#similars-section)
- [Bibliography](https://gwern.net/sidenote#link-bibliography-section)

![Demonstration of sidenotes.js handling multiple large dense endnote annotations on an annotated novel which has many allusions and technical references.](https://gwern.net/doc/cs/css/sidenotes.png)null

> **Sidenotes** & **margin notes** are a typographic convention which improves on footnotes & endnotes by instead putting the notes in the page margin to let the reader instantly read them without needing to refer back and forth to the end of the document (endnotes) or successive pages (footnotes spilling over).
>
> They are particularly useful for web pages, where ‘footnotes’ are de facto endnotes, and clicking back and forth to endnotes is a pain for readers. (Footnote variants, like “floating footnotes” which pop up on mouse hover, reduce the reader’s effort but don’t eliminate it.)
>
> However, they are not commonly used, perhaps because web browsers until relatively recently made it hard to implement sidenotes easily & reliably. Tufte-CSS has popularized the idea and since then, there has been a proliferation of slightly variant approaches. I review some of the available implementations.
>
> For general users, I recommend [Tufte-CSS-style approaches⁠](https://gwern.net/sidenote#tufte-css): it is fast & simple (using only compile-time generation of sidenotes, rendered by static HTML/CSS), popular, and Tufte-CSS-esque libraries are easy to integrate into many website workflows. For heavy footnote users or users who want a drop-in, runtime JavaScript-based solutions like [`sidenotes.js`⁠](https://gwern.net/sidenote#sidenotes-js) may be more useful.

Making use of margins

Sidenotes and margin notes (sometimes also called “asides”) are an alternative to [footnotes/endnotes⁠](https://en.wikipedia.org/wiki/Note_(typography) "Note (typography)") in design. Where footnotes put additional material in small sections at the bottom of the page, organized by number, and endnotes stuff them at the end of the document, sidenotes & margin notes instead use the large unused left/right margin of the page. If it is numbered & anchored to a specific point in the text, I call it a ‘sidenote’; if it is unnumbered & is merely placed next to a body of text, then I call it a ‘margin note’. (Margin notes are less useful & more obscure, so tend to be unsupported; I occasionally use margin notes for summarizing paragraphs, like the next paragraph here, where they function as extremely small ‘section headers’.)

Making use of margins. Because it’s uncomfortable to read sentences which wrap from edge to edge, particularly for large widths, documents use [short lines⁠](https://en.wikipedia.org/wiki/Line_length "Line length"). But with large screens, many documents have equally large margins, and wind up looking like a narrow river of text flowing down a vast blank map. This river of text may be studded with the occasional footnote or endnote, including ancillary material like citations or digressions or extended discussion of tricky points or anticipation of objections or just the author being witty, which require constant back and forth from the place in the text where they make sense and where they can actually be read. As a result, who ever reads endnotes in a physical book? Only the most diligent will keep a thumb in the back to actually look up endnotes, and so they are either unread or tend to be relegated to the most utilitarian uses like raw citations.

The situation is even worse on the Internet, because while footnotes in a book aren’t _too_ bad (as long as they stay on the same page), web pages don’t really have ‘pages’ and ‘footnotes’ wind up degrading to simply endnotes.⁠ [⁠1⁠](https://gwern.net/sidenote#fn1)

Why do we use endnotes? For the most part, we use them for citation metadata, abbreviations/definitions, and more extended discussions (often humorous). But none of these are served well online by endnotes: citation metadata is better provided as hyperlinks to fulltext, [definitions (`<defn>`)⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn "'<code>&lt;dfn&gt;</code>: The Definition element', MDN 2026")/ [abbreviations (`<abbr>`)⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr "'<code>&lt;abbr&gt;</code>: The Abbreviation element', MDN 2026") have native HTML support as tooltips/popups—leaving only the extended discussions use-case.

[Bringhurst⁠](https://en.wikipedia.org/wiki/Robert_Bringhurst "Robert Bringhurst") comments on the pros/cons ( _[The Elements of Typographic Style⁠](https://en.wikipedia.org/wiki/The_Elements_of_Typographic_Style "The Elements of Typographic Style")_, 200422ya):

> Footnotes are the very emblem of fussiness, but they have their uses. If they are short and infrequent, they can be made economical of space, easy to find when wanted and, when not wanted, easy to ignore. Long footnotes are inevitably a distraction: tedious to read and wearying to look at. Footnotes that extend to a second page (as some long footnotes are bound to do) are an abject failure of design.
>
> Endnotes can be just as economical of space, less trouble to design and less expensive to set, and they can comfortably run to any length. They also leave the text page clean except for a peppering of superscripts. They do, however, require the serious reader to use two bookmarks and to read with both hands as well as both eyes, swapping back and forth between the popular and the persnickety parts of the text.
>
> Sidenotes give more life and variety to the page and are the easiest of all to find and read. If carefully designed, they need not enlarge either the page or the cost of printing it. Footnotes rarely need to be larger than 8 or 9 point. Endnotes are typically set in small text sizes: 9 or 10 point. Sidenotes can be set in anything up to the same size as the main text, depending on their frequency and importance, and on the overall format of the page. If they are not too frequent, sidenotes can be set with no superscripts at all (as in this book), or with the same symbol (normally an asterisk) constantly reused, even when several notes appear on a single page.

Our extended discussions ought to be made easy to read in context and not hidden away at the end of the page. Sidenotes let us reuse some of that unused margin, in a way which is comfortable to read, and which is compatible with existing documents & workflows using endnotes: simply move those endnotes into the margin of the text they refer to. The user can comfortably saccade over to a sidenote instantly to skim it and back, the information density of the layout increases, it requires no exotic technologies or rewrites or user education, it has a long respectable history, and it’s just generally a good idea.

To see native sidenotes & margin notes on Gwern.net, use a wider screen.

# [Examples](https://gwern.net/sidenote\#examples "Link to section: § 'Examples'")

Some examples of sidenotes in books; Bringhurst uses sidenotes himself, of course:

![Bringhurst 200422ya example of sidenotes & margin notes (in this case, it repeats the section heading)](https://gwern.net/doc/design/typography/sidenote/2004-bringhurst-theelementsoftypographicstyle-pg70-marginsidenoteexample.png)

Bringhurst 200422ya example of sidenotes & margin notes (in this case, it repeats the section heading)

Sidenotes are extensively used in medieval manuscripts and early modern books such as the [Geneva Bible⁠](https://en.wikipedia.org/wiki/Geneva_Bible#Format "Geneva Bible § Format") ( [first 2 pages⁠](https://github.com/raphink/geneve_1564/releases/download/2015-07-08_01/geneve_1564.pdf)) (see also [rubrication⁠](https://gwern.net/red "'Rubrication Design Examples', Gwern 2019")), or Bayle’s awe-inspiringly ambitious use of (recursive) margin/side notes:

![Screenshot of Google Books (https://books.google.com/books?id=JmtXAAAAYAAJ&pg=PA900), showing advanced typography in a single page which contains body text, footnotes, and (recursively) sidenotes to footnotes, of Pierre Bayle’s famous Enlightenment text, the ‘Historical and Critical Dictionary’ (pg900 of volume 4 of the 1737 English edition).](https://gwern.net/doc/design/typography/sidenote/1737-bayle-dictionary-vol4-pg901.jpg)

[Pierre Bayle’s⁠](https://en.wikipedia.org/wiki/Pierre_Bayle "Pierre Bayle") [_Historical and Critical Dictionary_ ⁠](https://en.wikipedia.org/wiki/Dictionnaire_Historique_et_Critique "Dictionnaire Historique et Critique"), demonstrating recursive footnotes/sidenotes (1737289ya, volume 4, pg901; source: Google Books)

Sidenotes (and margin notes) have been less used in more contemporary books; the best-known popularizer is [Edward Tufte⁠](https://en.wikipedia.org/wiki/Edward_Tufte "Edward Tufte"):

![Example of Tufte’s use of sidenotes & margin notes: they provide additional examples, commentary, and citation metadata for the reader in context, without forcing inscrutable lookups buried deep at the end of the chapter (or worse, book) which few readers will ever bother with. (From pg61, “Layering & Separation”, Envisioning Information, Tufte 199036ya)](https://gwern.net/doc/design/typography/sidenote/1990-tufte-envisioninginformation-pg61-sidenotes.png)

Example of Tufte’s use of sidenotes & margin notes: they provide additional examples, commentary, and citation metadata for the reader in context, without forcing inscrutable lookups buried deep at the end of the chapter (or worse, book) which few readers will ever bother with. (From pg61, “Layering & Separation”, _Envisioning Information_, Tufte 199036ya)

[Donald Knuth⁠](https://en.wikipedia.org/wiki/Donald_Knuth "Donald Knuth") uses margin notes in [_Concrete Mathematics_ ⁠](https://en.wikipedia.org/wiki/Concrete_Mathematics "Concrete Mathematics") for a wide variety of ‘mathematical graffiti’ on the body contents: quotes from famous people or just unhappy students, jokes, criticism, questions to the reader, hints, etc. in his preprint drafts (‘fascicles’) of [_The Art of Computer Programming_ ⁠](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming "The Art of Computer Programming") uses margin notes as a kind of index, listing keywords in the margin as reminders for indexing in the final print version. The density of keywords can make the margins interesting to read on their own; an example from [TAOCP: pre-fascicle 4B: “A Draft of §7.2.1.7: History of Combinatorial Generation”⁠](https://www.antiquark.com/blogimg/fasc4b.pdf):

![Margin notes showing keywords for discussion of Chinese/Indian algorithmic history in Knuth.](https://gwern.net/doc/design/typography/sidenote/2004-knuth-taocp-fascicle-4-b-historyofcombinatorialgeneration-iching-marginnotes.png)

Margin notes showing keywords for discussion of Chinese/Indian algorithmic history in Knuth.

# [Implementation Strategies](https://gwern.net/sidenote\#implementation-strategies "Link to section: § 'Implementation Strategies'")

So, sidenotes are great. They are also easy in LaTeX PDFs.⁠ [⁠2⁠](https://gwern.net/sidenote#fn2) that may be used instead of `\marginpar`{.LaTeX\] at almost every place where `\marginpar`{.LaTeX\] cannot be used, eg. inside floats, footnotes, or in frames made with the `framed` package.”) (where the native `\marginpar{}`{.LaTeX\] command fails) packages.\] But how do we use them online for _HTML_?

Although sidenotes are ‘just’ snippets of text to the left or right of the main text and it might seem hard to screw it up, as always, there are a lot of ways to accomplish that goal, and many ways we can enhance (or screw up) them.

Do we put them on the left, right, or both sides? What of the several possible HTML elements are our sidenotes delimited as (`<span>`, `<a>`, `<div>`, [`<aside>`⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside), [`<small>`⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small "'<code>&lt;small&gt;</code>: the side comment element', MDN 2026"), or even `<table>`)? Do we use JavaScript, accepting that it’ll ‘flash’ an incorrectly rendered page as the JS loads & runs, and outright break for users with JS turned off (as is increasingly sensible on an ever-more-hostile Internet)? Does the user have to click or do anything to make sidenotes visible? If not, what about on mobile or tiny screens, which don’t _have_ any margins worth speaking of—do they get sidenotes in any form, and if so, do they render ‘inline’ as simply part of their paragraph, or do we display them as separate blocks (‘pop-in’) and by default or after a user click? How are many (or large, or both) sidenotes laid out, do they bump each other down the page or just overlap—it would seem that JS is necessary to avoid overlaps in most approaches, but is that too great a price? How does one add sidenotes support to an existing body of documents (typically Markdown)? Are there any known SEO concerns? (No, unless you do it in a bizarre way.) And so on.

Overall, I would say that good sidenotes should ideally: render on either both sides or the right (but not the left), use spans or links where possible, use static HTML/CSS, display by default (any user effort defeats the point!) but collapse to pop-ins (because mobile users don’t have screen real estate to spare for optional material although many authors choose expanded) with inline being an option for margin notes depending on how the writer uses them, with sidenotes overlapping as a tradeoff for not requiring JS (the author will just have to rewrite such excessive sidenote usage to avoid overlapping bugs), and endnotes in existing corpuses can be rewritten by whatever tool compiles the HTML into the appropriate span encoding.

Below I compare implementations I have found, and compile a table of what seems to me to be the key parts of the sidenotes taxonomy.

My recommendation is that for new or lightly-noted writings, one use Tufte-CSS-style sidenotes. For heavy sidenote use, a JS solution like `sidenotes.js` is probably necessary.

# [Comparison](https://gwern.net/sidenote\#comparison "Link to section: § 'Comparison'")

| [Tufte-CSS⁠](https://gwern.net/sidenote#tufte-css), Dave Liepmann | ✅ (201412ya) | **→** | ✅ | `<span>` | ✅ | ✅ | Pop-in (default: collapsed) | ❌ | [MIT⁠](https://en.wikipedia.org/wiki/MIT_License "MIT License") | Static, simple, popular; buggy block elements, endnote-incompatible, limited number supported |
| [`sidenotes.js`⁠](https://gwern.net/sidenote#sidenotes-js), Said Achmiz | ✅ (2019) | **↔︎** | ✅ | `<a>` | ❌ | ✅ | Pop-in/Endnotes (eg. on hover) | ✅ | MIT | Scales to many, Pandoc-compatible; slow(er). |
| [sidebar⁠](https://gwern.net/sidenote#sidebar-tables), Said Achmiz | ✅ (2020) | **→** | ✅ | `<div>` | ✅ | ✅ | Pop-in/❌ | ? | ? | Static; not intended for footnotes, one-sided only (currently). |
| [Ink & Switch⁠](https://gwern.net/sidenote#ink-switch) | ✅ (2016) | **→** | ✅ | `<aside>` | ✅ | ✅ | Pop-in | ❌ | ❌ | Static; non-Free, no sidenotes. |
| [Robert Nystrom⁠](https://gwern.net/sidenote#robert-nystrom) | ✅ (201412ya) | **→** | ✅ | `<aside>` | ❌ | ✅ | Inline | ❌ | ❌ | Offers inline fallback; custom, non-Free, requires JS. |
| [Matthew Butterick⁠](https://gwern.net/sidenote#matthew-butterick) | ✅ (201313ya) | **←** | ✅ | `<aside>` | ✅ | ✅ | Inline | ❌ | ❌ | Static, simple, offers inline fallback; custom, non-Free, no numbering. |
| [Koos Looijesteijn⁠](https://gwern.net/sidenote#koos-looijesteijn) | ✅ (2019) | **→** | ❌ | `<span>`/`<small>` | ❌ | ✅ | Pop-in (collapsed) | ❌ | ❌? | App/screen-reader-compatible, searchable; relatively complex, requires JS, non-Free. |
| [_Harvard Law Review_ ⁠](https://gwern.net/sidenote#harvard-law-review) | ✅ (2016?) | **↔︎** | ❌? | `<span>` | ❌ | ❌ | Pop-in | ✅ (too short! ☹) | ❌ | Uses both margins; custom, non-Free, requires clicks & JS. |
| [_Yale Law Journal_ ⁠](https://gwern.net/sidenote#yale-law-journal) | ✅ (2017?) | **→** | ❌? | `<div>` | ❌ | ❌ | ❌/❌ | ✅ (too short! ☹) | ❌ | Floating footnote fallback; custom, non-Free, requires clicks & JS, entire site unusable on mobile. |
| [Knight Institute⁠](https://gwern.net/sidenote#knight-institute) | ✅ (?) | **→** | ❌? | `<span>` | ❌ | ❌ | Pop-in (collapsed) | ✅ (too short! ☹) | ❌ | Somewhat more readable than _Harvard_/ _Yale_; custom, non-Free, requires clicks & JS. |
| [_New York_ ⁠](https://gwern.net/sidenote#new-york) | ✅ (?) | **←** | ❌? | `<span>` | ❌ | ❌ | Floating footnote | ❌ | MIT? | Floating footnote fallback; left margin, requires clicks for everything, requires JS, unclear license. |
| [jQuery.sidenotes⁠](https://gwern.net/sidenote#jquery-sidenotes), Clark | ❌ (201313ya) | **←** | ✅ | `<a>` | ❌ | ✅ | Endnotes/Pop-in (expanded) | ❌ | MIT | Featureful; slow, unmaintained, limited number, only on the left? |
| [Sidenotes.js⁠](https://gwern.net/sidenote#sidenotes-js-correia), Correia | ❌ (201511ya) | **↔︎** | ❌? | `data` | ❌ | ❌ | Slide-in | ❌ | MIT | Unique ‘slide-in’ approach; everything else. |
| [_The India Forum_ ⁠](https://gwern.net/sidenote#the-india-forum) | ✅ (?) | **→** | ❌ | `<a>` | ❌ | ❌ | Slide-in/Endnotes | ❌ | ❌ | Improved slide-in shows all footnotes; everything else. |
| [HTML tables⁠](https://gwern.net/sidenote#tables) | NA (NA) | **↔︎** | ✅ | `<table>` | ✅ | ✅ | ❌ | ❌ | NA | Static, simple; no mobile/narrow compatibility, rigid, no features, hard to write or modify. |
| [Annotate⁠](https://gwern.net/sidenote#annotate-molly-white), Molly White | ✅ (2022) | **→** | ❌? | `<section>`/`<div>` | ❌ | ✅ | ✅/? | ❌ | MIT | Annotates ‘ranges’ instead of being limited to an anchor/number; due to intended [fisking⁠](https://en.wikipedia.org/wiki/Robert_Fisk "Robert Fisk") use-case, can run off screen. |
| [George POllard⁠](https://gwern.net/sidenote#george-pollard) | ✅ (2019) | **→** | ✅ | `<span>`/```<aside>``<figure>``` | ✅ | ✅ | Inline | ❌ | CC-BY-NC-SA |  |

Comparison of sidenotes implementations for web pages.

Table columns:

01. **Name**: name/creator

02. **Active**: whether appeared actively maintained when last checked (usually ~2020)

03. **Layout**: whether it puts notes in the left, right, or both margins

04. **Margin Notes**: whether it appears to support margin notes (sidenotes without a number & anchor inside the text, just free-floating text)

05. **Element**: which HTML element/tag is used to denote the sidenote in the HTML source (eg. Markdown puts in a `<a>` linking to a definition in the footer)

06. **Non-JS**: whether JavaScript required (which is bad if it can be done without JS)

07. **No Click**: whether the reader has to effortfully click on a note to see it (rather than visible by default or easily seen with hover)

08. **Mobile/Narrow**: how it handles mobile browsers and/or narrow screens (often the same)

09. **Long Collapse**: how it handles long notes which would threaten to overload the margin and push notes ‘off-screen’

10. **FLOSS**: whether OSI-approved copyright license

11. **Pros/Cons**: miscellaneous comments.


**[Backlinks (8)⁠](https://gwern.net/design#backlink) for [⁠“Comparison”⁠](https://gwern.net/sidenote#comparison):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1219366581)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-3169163282)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1072277341)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-3045811172)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2589356850)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-4163489074)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2167416908)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-3349307934)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


# [Implementations](https://gwern.net/sidenote\#implementations "Link to section: § 'Implementations'")

## [Tufte-CSS](https://gwern.net/sidenote\#tufte-css "Link to section: § 'Tufte-CSS'")

Experiments in using CSS3 for sidenotes date back to at least 200323ya, but by far the most popular implementation, and the primary inspiration for most sidenotes users, is the c. 201412ya [Tufte-CSS⁠](https://edwardtufte.github.io/tufte-css/#sidenotes "'Tufte-CSS: Sidenotes: Footnotes and Marginal Notes', Liepmann 2026") ( [Github⁠](https://github.com/edwardtufte/tufte-css "edwardtufte/tufte-css: Style your webpage like Edward Tufte’s handouts")). Tufte-CSS is outdated in respects, but does sidenotes sensibly:

![Tufte-CSS’s section on sidenotes/margin notes, demonstrating sidenotes/margin notes (default desktop appearance).](https://gwern.net/doc/design/typography/sidenote/2020-tuftecss-sidenotesmarginnotes.png)

Tufte-CSS’s section on sidenotes/margin notes, demonstrating sidenotes/margin notes (default desktop appearance).

![Tufte-CSS “pop-in” sidenotes, collapsed vs uncollapsed (on a narrow window or mobile)](https://gwern.net/doc/design/typography/sidenote/2020-tuftecss-sidenotesmarginnotes-mobilecollapsed.png)

Tufte-CSS “pop-in” sidenotes, collapsed vs uncollapsed (on a narrow window or mobile)

A Tufte-CSS-formatted sidenote looks like this:

```
<label for="sn-extensive-use-of-sidenotes" class="margin-toggle sidenote-number"></label>

<input type="checkbox" id="sn-extensive-use-of-sidenotes" class="margin-toggle">

<span class="sidenote">This is a sidenote.</span>
```

By default (on desktop), the notes are floated right into the margin; no measures are taken to avoid collisions or overlaps (presumably if you have that problem, you ought to just rewrite your page or fix it yourself). On narrow windows & mobile, a media-query overrides the regular CSS, so the margin notes are not floated, simply indented, and toggled. The CSS looks like:

```
.sidenote,
.marginnote {
    float: right;
    clear: right;
    margin-right: -60%;
    width: 50%;
    margin-top: 0.3rem;
    margin-bottom: 0;
    font-size: 1.1rem;
    line-height: 1.3;
    vertical-align: baseline;
    position: relative;
}

...
label.sidenote-number {
    display: inline;
}

label.margin-toggle:not(.sidenote-number) {
    display: none;
}

...
/* The mobile fallback: */
@media (max-width: 760px) {
    .sidenote,
        .marginnote {
            display: none;
        }
        .margin-toggle:checked + .sidenote,
        .margin-toggle:checked + .marginnote {
            display: block;
            float: left;
            left: 1rem;
            clear: both;
            width: 95%;
            margin: 1rem 2.5%;
            vertical-align: baseline;
            position: relative;
        }
}
```

Margin notes are implemented similarly to sidenotes because a margin note can just be a sidenote whose number is hidden (at the possibility of some user confusion at the ‘missing’ endnote/sidenote, fixable with further CSS tweaks using number counters).

One thing to note about Tufte-CSS is that, like books, it displays sidenotes by default. Many websites experimenting with note variations throw away the greatest advantage—the effortlessness of reading sidenotes by simply saccading left/right—in favor of hassling the user and forcing them to do quite as much work by clicking various UI elements to expand/collapse notes, defeating much of the point compared to a normal hyperlinked endnote.

Tufte-CSS requires no JavaScript and is pure HTML/CSS, delegating layout to the browser. It is simple, fast, supports mobile well, and widely-used—it is definitely the most popular of HTML sidenote implementations. Its disadvantages are it will not handle gracefully many complex⁠ [⁠3⁠](https://gwern.net/sidenote#fn3) or lengthy sidenotes (which will overlap), and Tufte-CSS-style notes are not generated by default by many systems (so some sort of rewrite step is necessary to integrate Tufte-CSS into however one actually creates one’s website).

Because Tufte-CSS sidenotes/margin notes are located inline, rather than put at the end of the text like most document systems implement it (eg. Pandoc), one needs either to use JS to rewrite endnotes at runtime or to rewrite them at compile-time. Many projects generate Tufte-CSS sidenote spans directly or rewrite standard Markdown `<a>` endnotes to spans, such as the R packages [“tufte”⁠](https://cran.r-project.org/web/packages/tufte/index.html) & [“Tint Is Not Tufte: An implementation in R Markdown”](https://eddelbuettel.github.io/tint/ "Allaire et al 2016"). For Pandoc, [pandoc-sidenote⁠](https://github.com/jez/pandoc-sidenote "jez/pandoc-sidenote: Convert Pandoc Markdown-style footnotes into sidenotes") is a Haskell [Pandoc filter⁠](https://pandoc.org/filters.html "Pandoc filters") which rewrites Pandoc’s endnotes in Tufte-CSS-style spans, and can be used with Pandoc-based site builders like Hakyll or Jekyll (for the latter, see [tufte-pandoc-jekyll⁠](https://github.com/jez/tufte-pandoc-jekyll "A Jekyll theme for using Tufte CSS with Jekyll + Pandoc") & [tufte-jekyll⁠](https://github.com/clayh53/tufte-jekyll "Minimal Jekyll blog styled to resemble the look and layout of Edward Tufte's books")); [Guillaume Paumier⁠](https://github.com/gpaumier/gp2/commit/6f132a4cc684df807b0f3b6ad9d337e073bc3260 "Writer: Convert footnotes to Tufte-CSS side notes") & [Matt Palmer](https://mattwetmore.me/posts/hakyll-custom-writer "Using custom Pandoc writers with Hakyll") have Lua versions.

Tufte-CSS user examples: [Nicolas J. Duquette](http://nicolasduquette.com/research.html), [David Schmudde](https://schmud.de/posts/2020-08-04-mother-of-mothers.html "The Mothers of the Mother of All Demos"), [in Hebrew](https://digitalwords.net/about/ "אודות"), [Robin Schroer](https://blog.sulami.xyz/posts/common-lisp-restarts/ "Restarts in Common Lisp"), [Dan Pittman](https://blog.auxon.io/2019/10/25/type-level-registers/ "Using Type-Level Programming in Rust to Make Safer Hardware Abstractions"), [Jason Merrill](https://www.shapeoperator.com/2016/12/12/sunset-geometry/ "Sunset Geometry"), [Andrew Zuckerman](https://andzuck.com/blog/sfw/ "Super Free Will"), [Taeer Bar-Yam](https://taeer.bar-yam.me/blog/posts/hakyll-tikz/ "Hakyll + TikZ"), [Eric Marsden ( _Risk Engineering_)](https://risk-engineering.org/concept/Rasmussen-practical-drift "'Rasmussen and practical drift: Drift towards danger and the normalization of deviance', 2017"), [Tom Critchlow](https://tomcritchlow.com/2019/11/18/yes-and/ "'Yes! and... How to be effective in the theatre of work', 2019"), [Phil Crissman](http://philcrissman.net/posts/eulers-fizzbuzz/ "Euler’s FizzBuzz").

Similar approaches (some of these are more limited than Tufte-CSS; typically, authors fail to handle narrow/mobile):

- [“How can we develop transformative tools for thought?”⁠](https://numinous.productions/ttft/ "'How Can We Develop Transformative Tools For Thought?', Matuschak & Nielsen 2019"), Andy Matuschak & Michael Nielsen 2019 (mobile: floating footnotes)

- [Arxiv Vanity](https://www.arxiv-vanity.com/ "arXiv Vanity") (mobile: floating footnotes)

- [Nintil⁠](https://nintil.com/science-ending-frontier "Science") (mobile: pop-in, expanded)

- [Danila Fedorin’s](https://danilafe.com/blog/sidenotes/ "JavaScript-Free Sidenotes in Hugo") sidenotes (mobile: pop-in, collapsed) are inspired by Koos Looijesteijn’s approach, Fedorin’s implementation removes the JS but at the cost of guaranteeing accessibility and inheriting Tufte-CSS’s limitations on block elements/Markdown in sidenotes

- [“What does BERT dream of?”](https://pair-code.github.io/interpretability/text-dream/blogpost/ "A visual investigation of nightmares in Sesame Street by Alex Bäuerle (@a13xba) and James Wexler (@bengiswex) of PAIR.") (mobile: pop-in, expanded)

- [_Increment_](https://increment.com/open-source/the-rise-of-few-maintainer-projects/ "'The rise of few-maintainer projects: As casual contributions—coordinated by a handful of maintainers—become ever more prevalent, how should we reset our expectations for OSS?', Nadia Asparouhova 2019") (mobile: pop-in, expanded)

- [Matt Wilcox](https://mattwilcox.net/musing/the-ineffectiveness-of-icons "The ineffectiveness of lonely icons: If your target audience is a general population, you should not be using icons alone to convey anything meaningful. By doing so, you have made assumptions that are unlikely to be appropriate to a general audience."), with an unusual use of margin notes for paragraph/section _summaries_, similar to my use (mobile: pop-in, expanded)

- [“Dictionary of Numbers”](http://glench.com/closed-source/dictionaryofnumbers/ "Dictionary of Numbers"), Glen Chiacchieri (mobile: ❌)

- [Roman Gornitsky (The Temporary State)](https://letters.temporarystate.net/entry/3/ "Monospace Typography") (mobile: ❌)

- [Richard Rutter](https://clagnut.com/blog/2395 "All you need to know about hyphenation in CSS") (mobile: pop-in, expanded)

- [“Singular: Possible futures of the singularity”](https://jamesyu.org/singular/ "'Singular: Possible futures of the singularity', Yu & GPT-3 2020"), James Yu & GPT-3 (mobile: click-to-expand as a sticky pop-up)

- [“The Problem of Detecting Polygenic Selection from Temporal Data”](https://vincebuffalo.com/blog/2020/08/20/the-problem-of-detecting-polygenic-selection-from-temporal-data.html "The Problem of Detecting Polygenic Selection from Temporal Data"), Vince Buffalo (mobile: pop-in, expanded)

- [“How to do sidenotes in HTML documents using CSS and JavaScript”](https://fransdejonge.com/wp-content/uploads/2010/01/sidenotes.html), Frans de Jonge 200521ya (an early example, with consideration of cross-browser compatibility for the era)

- [Omar Rizwan](https://omar.website/posts/against-recognition/ "Against recognition") (Hugo)

- [Darius Kazemi/Emma Winston](https://runyourown.social/ "How to run a small social network site for your friends") (‘margin notes’, no apparent use of numbering to support ‘sidenotes’; nice retro theme; `<aside>`; pop-in, expanded; no truncation/wrapping; absolute positioning offset based on div around associated paragraph, so can’t handle overlaps which leads to bugs as [can be seen⁠](https://gwern.net/doc/design/typography/sidenote/2022-10-31-dariuskazemi-runyourownsocial-exampleofoverlappingsidenotesbug.png) in that page; apparently extraneous use of grid?)

- [Vale](https://verdagon.dev/blog/perfect-replayability-prototyped "'Heisenbugs: The most elusive kind of bug, and how to capture them with Perfect Replayability—Eliminate heisenbugs and endless debugging sessions!', Evan Ovadia 2022-06-29") (notable for strange handling of mobile: the sidenotes are hidden and their footnote numbers left in place, by being moved to the end of a section and grouped in a single list while being collapsed; clicking or tapping the footnote jumps to the end-block but does _not_ expand them, and they must be clicked on to expand them all.)

- [Tyler Vigen⁠](https://tylervigen.com/the-mystery-of-the-bloomfield-bridge): pop-in-only; tooltips used for ‘hover’, which is a bad idea⁠ [⁠4⁠](https://gwern.net/sidenote#fn4)

- [xkqr](https://entropicthoughts.com/markov-chains-for-queueing-systems "'Markov Chains for Queueing Systems', kqr 2022") (input checkbox mobile approach)

- examples with **no mobile** (❌) support:

  - [Hoefler&Co.](https://www.typography.com/blog/text-for-proofing-fonts "'Text for Proofing Fonts: A farewell to <em>The Quick Brown Fox</em>', Jonathan Hoefler 2020")

  - [Michael Petralia](http://www.michaelpetralia.com/theartofliving_epictetus.html "The Art of Living (Epictetus circa A.D. 100), as interpreted by Sharon Lebell")

  - The Morning After WordPress template’s “asides” ( [example](https://thecityasaproject.org/2020/05/a-pilgrimage-round-my-room-virtual-travel-to-the-holy-land-in-the-middle-ages/ "A Pilgrimage Round my Room: Virtual Travel to the Holy Land in the Middle Ages"))

  - [Francesco](https://mazzo.li/posts/vectorized-atan2.html "Speeding up atan2f by 50x") (overloads `<section>` & manually overrides list markers for numbering for one section per sidenote, with fragile grid default positioning; mobile is just desktop but made microscopic)

**[Backlinks (3)⁠](https://gwern.net/design#backlink) for [⁠“Tufte-CSS”⁠](https://gwern.net/sidenote#tufte-css):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1466131958)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-248586204)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-248586204)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [`sidenotes.js`](https://gwern.net/sidenote\#sidenotes-js "Link to section: § 'sidenotes.js'")

[`sidenotes.js`⁠](https://gwern.net/static/js/sidenotes.js) was developed by [Said Achmiz](https://wiki.obormot.net/ "Welcome to OborWiki") in 2019 for use on Gwern.net after looking at Tufte-CSS and deciding that Tufte-CSS’s simple approach (while appropriate for most users) would fail on particularly-heavily endnoted pages:

![Demonstration of sidenotes.js handling multiple large dense endnote annotations on Radiance.](https://gwern.net/doc/cs/css/sidenotes.png)

Demonstration of `sidenotes.js` handling multiple large dense endnote annotations on [_Radiance_ ⁠](https://gwern.net/doc/radiance/2002-scholz-radiance "'Radiance: A Novel', Scholz et al 2013").

![Gwern 2021](https://gwern.net/doc/design/2021-03-30-gwern-sidenotes-gwernnet-popins.png)

Pop-in of footnotes (handled by `extracts.js`/`popins.js` as a special-case of generalized annotations).

The advantage over Tufte-css is that `sidenotes.js` ‘manually’ lays out sidenotes at runtime to minimize overlap while trying to keep sidenotes within the same window as the anchor, enabling it to handle almost arbitrarily many long endnotes without rendering any unreadable. Sidenotes/endnotes can be arbitrarily long and contain most block elements like code blocks, blockquotes, lists, images, tables, etc. While it’s at it, sidenotes are highlighted & their matching anchors highlighted on hover, too-long sidenotes are partially collapsed (the user clicks to expand them). Further, it supports a custom “margin note” feature: any HTML spans of text with the class `margin-note` will be popped out of the text into the margin if there is room, or it will be left in place & italicized. (I place margin notes at the beginning of paragraphs as summaries, letting users more easily skim.) Finally, as a bit of an easter egg inspired by [`xeyes`⁠](https://en.wikipedia.org/wiki/Xeyes "Xeyes"), the sidenote return-to-anchor arrows are angled up or down so as to point to the original link in the body.

The disadvantage compared to pure static HTML/CSS approaches is that the JS needs to load and copy the endnotes into sidenotes, reflow as necessary over the whole page, which is user-visible & distracting; this is noticeable even putting the load in the HEAD to speed it up. It can also interact with other complicated features and while it will handle heavy note loads much better than most static approaches (most of which don’t even try to avoid errors like overlaps), it still has the occasional subtle bug.

For narrow windows, other approaches can be used. On Gwern.net, I use [floating footnotes⁠](https://gwern.net/static/js/popups.js "'<code>popups.js</code>', Achmiz 2019") which ‘pop up’ when the user hovers over a footnote anchor⁠ [⁠5⁠](https://gwern.net/sidenote#fn5), which avoids the need to navigate to the end of the page & back.

`sidenotes.js` assumes that the document has been generated from Pandoc Markdown and has normal Pandoc endnotes (of the form `<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>` for the anchor, and `<li id="fn1" role="doc-endnote"><p>Example</p></li>` for the endnote body at the end of the document). Hence, implementing sidenotes with it requires little more than a JS import like `<script src="/static/js/sidenotes.js" async></script>`. (This has some advantages: for example, footnotes/sidenotes remain linkable—one can link to `#fn1` or `#sn1` as desired.⁠ [⁠6⁠](https://gwern.net/sidenote#fn6))

Users or similar implementations:

- [Fantastic Anachronism](https://www.fantasticanachronism.com/2020/01/17/having-had-no-predecessor-to-imitate/index.html "Having Had No Predecessor to Imitate, He Had No Successor Capable of Imitating Him")

- Leo Gao (eg. [1](https://bmk.sh/2019/10/27/The-Difficulties-of-Text-Generation-with-Autoregressive-Language-Models/ "The Difficulties of Text Generation using Autoregressive Language Models: A Brief Overview"), [2](https://bmk.sh/2020/05/29/GPT-3-A-Brief-Summary/ "Why GPT-3 Matters")) designed his site inspired a little by Gwern.net, and uses sidenotes similarly; his approach seems to be simpler. (mobile: endnotes)

- OpenAI (eg. [1⁠](https://openai.com/research/how-ai-training-scales "How AI Training Scales: We’ve discovered that the gradient noise scale, a simple statistical metric, predicts the parallelizability of neural network training on a wide range of tasks. Since complex tasks tend to have noisier gradients, increasingly large batch sizes are likely to become useful in the future, removing one potential limit to further growth of AI systems. More broadly, these results show that neural network training need not be considered a mysterious art, but can be rigorized and systematized.")) (mobile: endnotes)

- [Marshall (Vandegrift) Bockrath](http://blog.platypope.org/2010/1/7/solving-puzzles-with-computer-science/ "Solving puzzles with (computer) science"), from [pre-2012](http://blog.platypope.org/2012/4/5/restore-features/ "Restoring Features")! (mobile: ❌)


**[Backlinks (3)⁠](https://gwern.net/design#backlink) for [⁠“sidenotes.js”⁠](https://gwern.net/sidenote#sidenotes-js):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2380014517)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2380014517)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2380014517)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


### [Sidebar Tables](https://gwern.net/sidenote\#sidebar-tables "Link to section: § 'Sidebar Tables'")

Said Achmiz has developed a pure CSS+HTML variant of sidenotes which is intended for easy cross-referencing of block elements such as small tables rather than footnotes. The block elements are floated inside a double `<div>` with the main column having a maximum width, so at wider windows the sidebar blocks slip rightwards into the margin (while their inner `<div>`s make them align left within the margin).

A demonstration of this sidebar is a [_Dungeons & Dragons_ manual on the “Athletics” skill](https://woa.obormot.net/Athletics "Worlds of Adventure"), where the tables & specialty skills are conveniently placed in the margin where possible, shrinking as necessary, but ultimately being popped inline for sufficiently narrow windows. There are so many tables that if they were placed in the main column, as usual, the text would be constantly interrupted and widely separated; the sidebar layout more closely replicates the dense layout of [D&D⁠](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons "<em>Dungeons & Dragons</em>") manuals, which is important when the players will be frequently consulting it for details.

![Sidebar, full width](https://gwern.net/doc/design/typography/sidenote/2020-11-obormot-sidebar-dand.png)

Sidebar, full width

![Sidebar, inline](https://gwern.net/doc/design/typography/sidenote/2020-11-obormot-sidebar-dand-collapsed.png)

Sidebar, inline

( [Max Kohler](https://www.maxkohler.com/posts/continuous-typography/ "Continuous Typography: Notes toward a continuous framework for screen typography") abuses `<aside>` elements + grid layouts to achieve something somewhat similar but inferior in that all his sidenotes get stacked at the end—which defeats the point of having sidenotes.)

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Sidebar Tables”⁠](https://gwern.net/sidenote#sidebar-tables):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1362060426)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Ink & Switch](https://gwern.net/sidenote\#ink-switch "Link to section: § 'Ink & Switch'")

[Ink & Switch’s](https://www.inkandswitch.com/index.html "Ink &amp; Switch") pages like [“Local-first software: You own your data, in spite of the cloud”’s](https://www.inkandswitch.com/local-first.html "'Local-first software: You own your data, in spite of the cloud [web]', Kleppmann et al 2019") 2016 static margin notes feature looks much like Tufte-CSS in using HTML/CSS to create right-aligned sidenotes, although Ink & Switch eschews explicit footnote numbering and its pop-ins are uncollapsed by default.

![Ink & Switch, “Local-first software” margin notes](https://gwern.net/doc/design/typography/sidenote/2016-inkandswitch-localfirstdesign-marginnotes.png)

Ink & Switch, “Local-first software” margin notes

![Ink & Switch, “Local-first software” margin notes, mobile (pop-in, default expanded)](https://gwern.net/doc/design/typography/sidenote/2016-inkandswitch-localfirstdesign-marginnotes-mobile.png)

Ink & Switch, “Local-first software” margin notes, mobile (pop-in, default expanded)

Implementation-wise, it takes a noticeably different tack in which CSS features it uses. The HTML itself is just an `<aside>` element:

```
<aside><p><a href="https://ourincrediblejourney.tumblr.com/">Our incredible journey</a>
    is a blog that documents startup products getting shut down after an acquisition.</p><​/​aside>
```

But [their CSS](https://gitlab.developers.cam.ac.uk/cst/dtg/trvedata/local-first/-/commit/7a8819e817a85173af7033e64bcdcc5054b9af50?expanded=1#e74ca419c79e4a87cb170f6eb8a6c0d2719e1c73_0_726 "Web article style files (7a8819e8) <span class=separator-inline>•</span> Commits <span class=separator-inline>•</span> Computer Lab / Digital Technology Group / TRVE Data / local-first") uses [`calc()`⁠](https://developer.mozilla.org/en-US/docs/Web/CSS/calc "'<code>calc()</code> - CSS: Cascading Style Sheets', MDN 2026") extensively to create positioning & readjust overlaps without JS:

```
article aside, figcaption, header>#byline {
  --aside-offset: 1rem;
  --aside-offset-lineheight: 1.5rem;
  box-sizing: border-box;
  margin-bottom: calc(var(--padding) * 2);
  padding: var(--padding);
  position: absolute;
  right: 0;
  width: var(--aside-width);
}

aside, figcaption, figure img, figure video {
  border-radius: calc(var(--padding)/4);
  max-width: 100%;
}

aside, aside>*, #byline, #byline li, figcaption, figcaption>*, blockquote footer {
  font-size: 0.8125rem;
  font-weight: 400;
  -ms-hyphens: none;
  -webkit-hyphens: none;
  hyphens: none;
  line-height: 1.25rem;
  margin-bottom: 0.5rem;
  text-align: left;
}

...
/* aside and figcaption nudge ---------------- */

/* using these can cause overlapping of elements. if you apply to one aside, you may
    need to apply and adjust other that precede clearing the blocks figcaption or section */

.move-up-1 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*1))/-1);
}

.move-up-2 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*2))/-1);
}
...
.move-up-25 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*25))/-1);
}
```

One downside is that there is no support for numbering I can see, so they’re all margin notes. The CSS is considerably more complex and I’m not sure what the complexity gains one compared to Tufte-CSS—correctness?

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Ink & Switch”⁠](https://gwern.net/sidenote#ink-switch):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1260122815)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Robert Nystrom](https://gwern.net/sidenote\#robert-nystrom "Link to section: § 'Robert Nystrom'")

Game programmer Robert Nystrom’s 201412ya book [_Game Programming Patterns_ ⁠](https://gameprogrammingpatterns.com/ "Game Programming Patterns"), makes heavy use of sidenotes implemented in HTML/CSS/JS, mostly similar to Tufte-CSS.

![Game Programming Patterns, desktop sidenotes](https://gwern.net/doc/design/typography/sidenote/2013-robertnystrom-gameprogrammingpatterns-doublebuffer-sidenotes.png)

_Game Programming Patterns_, desktop sidenotes

![Game Programming Patterns, mobile (inline, expanded by default)](https://gwern.net/doc/design/typography/sidenote/2013-robertnystrom-gameprogrammingpatterns-doublebuffer-sidenotes-mobile.png)

_Game Programming Patterns_, mobile (inline, expanded by default)

He takes a different approach: sidenotes are written using the HTML `<aside>` element, and a `<span>` with each aside’s ID specifies their placement in the text; [the JS⁠](https://gameprogrammingpatterns.com/script.js) then moves the aside into the margin. He designed it to handle resizing below <800px not by pop-in footnotes in a block, but by media-queries simply shifting the aside into the text, inline. (With no JS, the fallback is also including it inline.)

```
<p>Let&#8217;s say we want a happy face to appear on screen. Our program starts looping
through the framebuffer, coloring pixels. What we don&#8217;t realize is that the
video driver is pulling from the framebuffer right as we&#8217;re writing to it. As it
scans across the pixels we&#8217;ve written, our face starts to appear, but then it
outpaces us and moves into pixels we haven&#8217;t written yet. The result is
<em>tearing</em>, a hideous visual bug where you see half of something drawn on screen.</p>
<p><span name="tearing"></span></p>
<p><img src="images/double-buffer-tearing.png" alt="A series of images of an in-progress frame
    being rendered. A pointer writes pixels while another reads them. The reader outpaces the writer
    until it starts reading pixels that haven't been rendered yet."></p>
<aside name="tearing">

<p>We start drawing pixels just as the video driver starts reading from the
framebuffer (Fig. 1). The video driver eventually catches up to the renderer and
then races past it to pixels we haven&#8217;t written yet (Fig. 2). We finish drawing
(Fig. 3), but the driver doesn&#8217;t catch those new pixels.</p>
<p>The result (Fig. 4) is that the user sees half of the drawing. The name
&#8220;tearing&#8221; comes from the fact that it looks like the bottom half was torn off.</p>
​<​/​aside>
```

```
@media only screen and (min-width: 800px) {
  .page {
    padding-right: 300px; }

  aside {
    position: absolute;
    width: 240px;
    right: 30px;
    padding: 0;
    background: none;
    border: none;
    padding-left: 22px;
    border-radius: 0;
    border-left: solid 8px #f0e9db; }
  aside p, aside li {
      font: 14px/20px "Source Sans Pro", "Lucida Grande", "Lucida Sans Unicode", Verdana, sans-serif; } }
```

It’s unclear to me whether the JS is necessary, or whether inline is the best fallback for sidenotes. The use of `<aside>` is also a complication, as few formats include any native support for that.

Nystrom’s books are an interesting read for programmers, and also have some other interesting design aspects: see [“Zero to 95,688: How I wrote _Game Programming Patterns_”](https://journal.stuffwithstuff.com/2014/04/22/zero-to-95688-how-i-wrote-game-programming-patterns/ "Zero to 95,688: How I wrote Game Programming Patterns")/ [“Crafting _Crafting Interpreters_”](https://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/) on the build system & literate programming & his hand-drawn illustration workflow; & [“Zero to 353 Pages: Bringing My Web Book to Print and eBook”](https://journal.stuffwithstuff.com/2014/11/03/bringing-my-web-book-to-print-and-ebook/ "Zero to 353 Pages: Bringing My Web Book to Print and E-book") on working with EPUB & typesetting the print book.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Robert Nystrom”⁠](https://gwern.net/sidenote#robert-nystrom):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-445445051)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Matthew Butterick](https://gwern.net/sidenote\#matthew-butterick "Link to section: § 'Matthew Butterick'")

[Matthew Butterick’s⁠](https://en.wikipedia.org/wiki/Matthew_Butterick "Matthew Butterick") 201313ya ebook/website [_Practical Typography_](https://practicaltypography.com/ "Butterick’s <em>Practical Typography</em>") uses margin notes, but in a sidenotes way, on the left:

![Margin note left in Practical Typography.](https://gwern.net/doc/design/typography/sidenote/2013-matthewbutterick-practicaltypography-webemailaddresses-marginnote.jpg)

Margin note left in [_Practical Typography_](https://practicaltypography.com/web-and-email-addresses.html "Web &amp; email addresses").

They fallback to pop-ins defaulted to expanded on narrow/mobile windows:

![The same margin note, on a narrow window: it now appears as a pop-in block element, but expanded without the user needing to click (as they would in Tufte-CSS).](https://gwern.net/doc/design/typography/sidenote/2013-matthewbutterick-practicaltypography-webemailaddresses-marginnote-mobile.png)

The same margin note, on a narrow window: it now appears as a pop-in block element, but expanded without the user needing to click (as they would in Tufte-CSS).

The approach is HTML/CSS, but using `<aside>` elements, which are styled in CSS:

```
title-block, aside {
    display: block;
    float: left;
    position: absolute;
    margin-left: 0;
    left: 2.5rem;
    width: calc(2.5rem * 3);
    text-align: right;
    list-style-type: none;
    clear:both; margin-bottom: 1rem;
    font-variant-numeric: normal;
}

@media all and (min-width:1200px) {
    aside {
        left : 0;
        width: calc(2.5rem * 4);
    }
}

@media all and (max-width:520px) {
    title-block, aside { float: inherit;
    position: inherit;
    width: 100%;
    text-align: left;}

    aside {
        background: #fefefe;
        padding: 0.3rem 0.5rem;
        width: 90%;
        border: 1px solid #ccc;
        border-left: 3px solid #ccc;
    }

    aside > p:last-child {
        margin-bottom: 0;
    }
}
```

Presumably Butterick used his Racket-based [Pollen document system](https://docs.racket-lang.org/pollen/ "Pollen: the book is a program") with custom tags, since the base system doesn’t cover notes; [Sancho McCann](https://sanchom.github.io/pollen-footnotes.html "Sancho McCann") & [Jonas Hietala](https://www.jonashietala.se/blog/2019/03/04/pollen_sidenotes/) has documented Pollen sidenotes.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Matthew Butterick”⁠](https://gwern.net/sidenote#matthew-butterick):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1211371785)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Koos Looijesteijn](https://gwern.net/sidenote\#koos-looijesteijn "Link to section: § 'Koos Looijesteijn'")

[Koos Looijesteijn’s](https://www.kooslooijesteijn.net/) loosely Tufte-CSS-like sidenotes are right-aligned, symbol rather than number incremented, and narrow/mobile collapsed pop-ins:

![KL, desktop](https://gwern.net/doc/design/typography/sidenote/2019-looijesteijn-sidenotes.png)

KL, desktop

![KL, mobile (pop-in clicked)](https://gwern.net/doc/design/typography/sidenote/2019-looijesteijn-sidenotes-mobile.png)

KL, mobile (pop-in clicked)

In [“Semantic sidenotes for the web”](https://www.kooslooijesteijn.net/blog/semantic-sidenotes) 2019, he discusses his approach, intended to satisfy additional requirements:

> - The span that the sidenote refers to should have a proper semantic HTML element (no abuse of elements made for other purposes)
>
> - The content of the sidenote should have a similarly valid HTML tag. Additionally:
>
>   - The sidenote content may contain span elements such as `<a>` and `<em>`.
>
>   - The sidenote content may contain clickable elements that can receive keyboard focus.
>
>   - The sidenote content must be stylable.
> - The elements should not cause auto closing of their parent `<p>` tag.
>
> - Reader modes and apps like Pocket and RSS readers should show sidenote content in a typographically acceptable way. That means at the very least that I can’t rely on website’s CSS to place and style the elements correctly.
>
> - The sidenote content should be read by screen readers, in a flow that makes sense. That likely means the two parts should be placed together.

He came up with something initially like Tufte-CSS, but rejected pure `<span>`, `<aside>` as being not quite the right semantics, purely static as breaking reader mode/apps, and settled on JS-enhanced `<span>`/`<small>` combination.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Koos Looijesteijn”⁠](https://gwern.net/sidenote#koos-looijesteijn):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2765709007)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Harvard Law Review](https://gwern.net/sidenote\#harvard-law-review "Link to section: § 'Harvard Law Review'")

The [Harvard Law Review’s⁠](https://en.wikipedia.org/wiki/Harvard_Law_Review "Harvard Law Review") website has, since at least 2016, employed sidenotes, as is particularly appropriate for legal writing, which notoriously overuses footnotes for citations, precedents, and digressions. From [“The Potential-Use Test and the Northwest Passage”](https://harvardlawreview.org/print/vol-133/the-potential-use-test-and-the-northwest-passage/ "The Potential-Use Test and the Northwest Passage") (HLR editors 2020):

![HLR, desktop; note the default collapse/fade](https://gwern.net/doc/design/typography/sidenote/2020-harvardlawreview-sidenotes.png)

HLR, desktop; note the default collapse/fade

![HLR, mobile (pop-in on click)](https://gwern.net/doc/design/typography/sidenote/2020-harvardlawreview-sidenotes-mobile.png)

HLR, mobile (pop-in on click)

HLR’s proprietary are bidirectional, JS-based, and collapsed pop-in on mobile; they use `<span>`s which are rearranged by the JS:

```
Canada, on the other hand, asserts that the Northwest Passage constitutes internal waters and does
not fall under any definition of international strait.
<sup class="footnote-ref js-article-aside-trigger "><i class="ref-txt">2</em><i class="close-txt">&times;</em></sup>
<cite class="article-aside footnote short-crop">
    <span class="article-aside-txt">
        <span class="footnote-num">2.</span>
        <em>See</em> Territorial Sea Geographical Coordinates (Area 7) Order, SOR/1985-872 (Can.) (detailing Canada’s
        claims to land and waters that include the Northwest Passage); Note from the Canadian Embassy, Washington, D.C.,
        to the U.S. Department of State (June 11, 1985), <em>reprinted in</em> 2 <span class="small-caps">Marion Nash (Leich),
        Dep’t of State, Cumulative Digest of United States Practice in International Law 1981–1988</span>, at 2047 (1994).
    </span>
</cite>
```

Since it uses inline `<span>` in the usual Tufte-CSS, one might wonder why the JS is necessary, but checking with NoScript, one sees that without the JS, the sidenotes are all piled up on the left margin, overlapping badly, so the JS does the ‘alternating’. (Is it possible to use CSS to do this alternation automatically, removing the need for JS to do bidirectional sidenotes?)

More distressingly, HLR’s sidenotes are also on default collapsed on _desktop_, trimmed at a shockingly short length—typically not even half a sentence! While collapsing long footnotes is a good idea, it’s puzzling to collapse at such a short length that literally every sidenote will be collapsed, since this again defeats the point of having sidenotes, and making it hard to see if a sidenote is worth clicking on since only the first few words are exposed so one cannot even see if the sidenote is short (merely a bit of citation) or long (a more in-depth discussion).

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Harvard Law Review”⁠](https://gwern.net/sidenote#harvard-law-review):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-4264206102)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Yale Law Journal](https://gwern.net/sidenote\#yale-law-journal "Link to section: § 'Yale Law Journal'")

The [_Yale Law Journal_ ⁠](https://en.wikipedia.org/wiki/The_Yale_Law_Journal "<em>The Yale Law Journal</em>"), like HLR, uses sidenotes in online articles like [“Amazon’s Antitrust Paradox”](https://www.yalelawjournal.org/note/amazons-antitrust-paradox "Yale Law Journal - Amazon’s Antitrust Paradox") (Khan 2017), since at least 2016. Like HLR, all sidenotes are aggressively collapsed to near-unreadability, requiring a click to expand, whereupon they turn into floating footnotes.

![YLJ, default desktop](https://gwern.net/doc/design/typography/sidenote/2017-yalelawjournal-khan-sidenotes.png)

YLJ, default desktop

![YLJ, sidenotes clicked on to expand](https://gwern.net/doc/design/typography/sidenote/2017-yalelawjournal-khan-sidenotes-expanded.png)

YLJ, sidenotes clicked on to expand

They are JS-based, relocating footnotes grouped at the end of the article, but inside `<div>` elements rather than `<a>` elements like usual:

```
<div id="footnote_wrapper" style="position:relative;">
    <div id="footnote_1" style="display: none;" class="footnote_truncated">
        <div class="truncated_footnote_number">1</div>
        <div class="truncated_footnote_inner"><span> </span>David <span class="SpellE">Streitfeld</span>,
            <em>As Competition Wanes, Amazon Cuts Back Discounts</em>,
            <span class="forced_sans_reg">N.Y. Times</span> (July 4, 2013), http&hellip;
            </div>
    </div>
...</div>
```

Worse, YLJ appears to have no narrow or mobile support whatsoever—the page just gets smaller. YLJ is unreadable on mobile, requiring zooming & panning.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Yale Law Journal”⁠](https://gwern.net/sidenote#yale-law-journal):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-3394081238)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Knight Institute](https://gwern.net/sidenote\#knight-institute "Link to section: § 'Knight Institute'")

The [Knight First Amendment Institute](https://knightcolumbia.org/page/about-the-knight-institute) of [Columbia University⁠](https://en.wikipedia.org/wiki/Columbia_University "Columbia University") uses sidenotes somewhat like HLR/YLJ in its longform pages (eg. [“The Case for Digital Public Infrastructure: Harnessing past successes in public broadcasting to build community-oriented digital tools”](https://knightcolumbia.org/content/the-case-for-digital-public-infrastructure "The Case for Digital Public Infrastructure"), Zuckerman 2020):

![Knight Institute sidenotes (not expanded)](https://gwern.net/doc/design/typography/sidenote/2020-knightinstitute-zuckerman-sidenotes.png)

Knight Institute sidenotes (not expanded)

They are JS-based, right-aligned, collapsed (but with a slightly more generous length limit than HLR/YLJ), and fallback to Tufte-CSS-like pop-in blocks (default collapsed). As similar as it seems to those, Knight appears to have rolled its own JS, as the `site.js`’s implementation doesn’t have any Google/Github hits.

The fading, font size, and default collapsing of ‘long’ sidenotes are all not nearly as extreme as HLR/YLJ, so the Knight sidenotes are substantially more pleasant to read, as it’s much easier to see what sidenotes are merely a brief citation and what actually include additional commentary. (The use of buttons & chevrons are also nice touches in explaining the functionality to the reader.)

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Knight Institute”⁠](https://gwern.net/sidenote#knight-institute):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-912591539)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [_New York_](https://gwern.net/sidenote\#new-york "Link to section: § 'New York'")

[_New York_’s⁠](https://en.wikipedia.org/wiki/New_York_(magazine) "New York (magazine)") website CMS [Clay/Kiln⁠](https://github.com/clay) (used on NYmag.com/Vulture/the Cut/Grub Street/Slate) provide JS-based left sidenotes which require hover to expose and then fall back to click-driven floating footnotes:

![Vulture, desktop (on hover)](https://gwern.net/doc/design/typography/sidenote/2020-newyork-vulture-chrisrockinterview-sidenotes.png)

_Vulture_, desktop (on hover)

![Vulture, mobile (after clicking)](https://gwern.net/doc/design/typography/sidenote/2020-newyork-vulture-chrisrockinterview-sidenotes-mobile.png)

_Vulture_, mobile (after clicking)

NY uses spans, but they are put at the end and then JS reveals them when the user hovers:

```
<span class="clay-annotated kiln-phrase" aria-describedby="annotation-1" tabindex="0">Virgin Airlines first-class lounge</span>
...
<div data-uri="www.vulture.com/_components/annotations/instances/cjg2jwsso00c23k62pm0yv0qg@published"
     class="annotations" data-editable="content">
    <span role="tooltip" id="annotation-1" data-uri="www.vulture.com/_components/annotation/instances/cjg2jx3el00c73k62em8v15xy@published"
       class="annotation" data-editable="text">
       Offers spa treatments, “expert mixologists”, and, at Heathrow, a “lodge and viewing deck” with an “après-ski vibe.”
   </span>
</div>
```

I couldn’t find mention of sidenotes in the various Clay/Kiln Github repos but there are enough of them and it’s all complicated enough I may have missed them, so I don’t know if the relevant JS/CSS is MIT-licensed like the Clay/Kiln ecosystem generally seems to be.

While floating footnotes on mobile is a justifiable choice, the rest is not, and I do not like this sidenote design at all.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“New York”⁠](https://gwern.net/sidenote#new-york):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1582615559)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [JQuery.sidenotes](https://gwern.net/sidenote\#jquery-sidenotes "Link to section: § 'jQuery.sidenotes'")

Andrew Clark’s 201313ya [jQuery.sidenotes](https://acdlite.github.io/jquery.sidenotes/) ( [Github⁠](https://github.com/acdlite/jquery.sidenotes)) JS library implements sidenotes to the left, parsing Markdown endnotes; for narrow windows, it does inlined ‘pop-in’ but expanded by default; and for mobile it is just endnotes. Unusually, Clark’s demo puts sidenotes on the _left_ margin (there doesn’t seem to be an option for placing on the right, or both), and includes some keybindings.

![jQuery.sidenotes (default desktop appearance)](https://gwern.net/doc/design/typography/sidenote/2013-clark-jquerysidenotes-sidenotes.png)

jQuery.sidenotes (default desktop appearance)

The pop-in appearance looks like Tufte-CSS’s.

The implementation seems to take the expected approach of popping matching elements out into the margin with media queries controlling width-related behavior.

Clark’s jQuery.sidenotes offers more features than usual, but I’m not sure how useful they are. It’s also quite ‘heavyweight’ in being weighed down by jQuery/NPM infrastructure. One further caveat: I think the expected format/classes of endnotes has long since changed and the library has not been updated since 201313ya, at least for Pandoc, so jQuery.sidenotes’s defaults will probably break for recent Markdown documents.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“JQuery.sidenotes”⁠](https://gwern.net/sidenote#jquery-sidenotes):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2194154321)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Sidenotes.js, Correia](https://gwern.net/sidenote\#sidenotes-js-correia "Link to section: § 'Sidenotes.js, Correia'")

Bruno Correia’s 201511ya [Sidenotes.js](http://bcorreia.com/projects/sidenotes.js/src/demo.html) ( [Github⁠](https://github.com/bcorreia/sidenotes.js)), not to be confused with Said Achmiz’s [`sidenotes.js`⁠](https://gwern.net/sidenote#sidenotes-js), takes an entirely different approach to both presentation & encoding of sidenotes. Instead of reusing the existing margin, Sidenotes.js creates a new view by _sliding_ a sticky-element ‘tab’ into view with the sidenote contents, hiding the original page:

![Sidenotes.js, before/after clicking on an annotated link (desktop)](https://gwern.net/doc/design/typography/sidenote/2015-correia-sidenotes-slide.png)

Sidenotes.js, before/after clicking on an annotated link (desktop)

On narrow or mobile, the slid-in new page just takes up the whole screen.

The annotations are themselves written as [custom data attributes⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-* "'HTML: HyperText Markup Language', MDN 2026") on elements such as links (by default, others are supported):

```
<p>While the two headsmen were engaged in making fast cords to his flukes,
and in other ways getting the mass in readiness for towing,
some <a
    href="#"
    data-sidenote="&gt;strong&lt;Conversation:&gt;/strong&lt; the informal exchange of ideas by spoken words:
                   'the two men were deep in conversation'.">
    conversation</a>
ensued between them.</p>
```

This is a unique approach entirely unlike the others and an interesting experiment, but I do not recommend it for sidenotes.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Sidenotes.js, Correia”⁠](https://gwern.net/sidenote#sidenotes-js-correia):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-4236801561)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [_The India Forum_](https://gwern.net/sidenote\#the-india-forum "Link to section: § 'The India Forum'")

[_The India Forum_](https://www.theindiaforum.in/article/revolt-upper-castes "The Revolt of the Upper Castes") uses jQuery for a slide-in approach but improves over Correia’s by showing all the sidenotes in a pane after clicking:

![TIF, after clicking on footnotes](https://gwern.net/doc/design/typography/sidenote/2020-theindiaforum-revoltoftheuppercastes-sidenotes.png)

TIF, after clicking on footnotes

The ‘slide-in’ approach can be contrasted with the ‘slide-up’ approach used by Wikipedia:

![Screenshot of Artemy Vedel WP article after tapping a footnote in a mobile browser, showing a faded body and a highlighted footnote section which has ‘slid up’; this shows the footnote text (usually a brief citation) without shifting the overall layout or being too small to read.](https://gwern.net/doc/design/typography/sidenote/2023-02-23-wikipedia-mobilemode-tappedfootnoteslideupexample.png)

Screenshot of [Artemy Vedel⁠](https://en.wikipedia.org/wiki/Artemy_Vedel "Artemy Vedel") WP article after tapping a footnote in a mobile browser, showing a faded body and a highlighted footnote section which has ‘slid up’; this shows the footnote text (usually a brief citation) without shifting the overall layout or being too small to read.

And some other sites, like [Justin Duke](https://www.arcana.computer/):

![A tapped ‘footnote’ on Justin Duke’s website, showing how the footnote text has ‘slid up’ from the bottom in a floating/sticky element.](https://gwern.net/doc/design/typography/sidenote/2023-02-23-justinduke-aboutpage-mobileslideupfootnotescreenshot.png)

A tapped ‘footnote’ on Justin Duke’s website, showing how the footnote text has ‘slid up’ from the bottom in a floating/sticky element.

The ‘slide-in’ from left/right can make use of margin on bigger screens, but there is usually no margin on cramped mobile screens, so one faces a fundamental choice between inserting the footnote/sidenote text ‘into’ the body, usually forcing layout shift, and ‘over’ the body, obscuring some of it. (For Gwern.net, pop-ins were the only acceptable solution as they are less [modal⁠](https://en.wikipedia.org/wiki/Mode_(user_interface) "Mode (user interface)"): they let the reader continue navigating/reading the page, no matter how deep they drill into the recursively-linked pop-ins.)

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“The India Forum”⁠](https://gwern.net/sidenote#the-india-forum):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-2462285430)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Tables](https://gwern.net/sidenote\#tables "Link to section: § 'Tables'")

[Jukka “Yucca” Korpela](https://jkorpela.fi/www/fn.html#side "Footnotes, endnotes, and sidenotes on Web pages: Sidenotes as an alternative"), ~2007, demonstrates a completely different approach using HTML _tables_: define two columns with different sizes/style, and put the sidenotes in the second column.

> There are many possible approaches to including sidenotes on web pages. Having studied alternate methods like CSS positioning and floating, I have come to the conclusion that the simplest method gives the best results. This method consists of a two-column table, with the main text in one column, the sidenotes in the other. Using the CSS methods, it becomes awkward to control the heights of pieces of text so that each sidenote starts at the same vertical position as the main text that it relates to.

Easy:

![Sidenotes via 2-column HTML tables.](https://gwern.net/doc/design/typography/sidenote/2007-korpela-sidenotes-tablelayout.png)

Sidenotes via 2-column HTML tables.

This has the usual advantages/disadvantages of using tables for web design: it is fast, avoids JavaScript & (most) CSS complexities, and is straightforward; but it is rigid, degrades on smaller screens, difficult to write (eg. no numbering in Korpela’s examples, making them margin notes, unless the author manually adds superscripts or otherwise complicates it).

I include this for its historical interest—while this strategy may have made sense in 200719ya, the tradeoffs now are highly unfavorable given that [Tufte-CSS⁠](https://gwern.net/sidenote#tufte-css) etc. work, and I’m not sure anyone should use it.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Tables”⁠](https://gwern.net/sidenote#tables):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-4181379801)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Annotate, Molly White](https://gwern.net/sidenote\#annotate-molly-white "Link to section: § 'Annotate, Molly White'")

[“Annotate”⁠](https://github.com/molly/annotate) ( [demo](https://molly.github.io/annotate/)) is a CSS+JS framework by [Molly White⁠](https://en.wikipedia.org/wiki/Molly_White_(writer) "Molly White (writer)"), created for her [“The Edited Latecomers’ Guide To Crypto”](https://www.mollywhite.net/annotations/latecomers-guide-to-crypto/ "The (Edited) Latecomer's Guide to Crypto"), which is a heavily-commentated (side by side) fisking of an article on cryptocurrency.

Perhaps because the commentary may be longer than the text & complex, Annotate takes a novel approach: text+commentary pairs live in `<section>` elements, interleaving `<div>`s (possibly nested or ‘grouped’), with `<mark>` elements to specify highlighted ranges (eg. in yellow highlighting) for which part of the text a commentary is referring to. The CSS then uses CSS grids (row-based layout) to lay them out side by side. (JavaScript is used for live highlighting/focusing of ranges when clicked on, but otherwise appears optional.)

For mobile, it defaults to expanded pop-ins but does not appear to make any effort to interleave or separate pairs to ensure that the commentary for each visible highlighted range is also visible.

![Screenshot from its Github repo of Annotate used on “The Edited Latecomers’ Guide To Crypto”.](https://gwern.net/doc/design/typography/sidenote/2022-10-02-mollywhite-annotate-latecomersdesktopscreenshot.png)

Screenshot from its Github repo of Annotate used on “The Edited Latecomers’ Guide To Crypto”.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“Annotate, Molly White”⁠](https://gwern.net/sidenote#annotate-molly-white):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-794059002)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [George Pollard](https://gwern.net/sidenote\#george-pollard "Link to section: § 'George Pollard'")

Inspired by [Type Classes](https://typeclasses.com/coerce "Newtype coercion [in Haskell]") & Tufte-CSS; pure CSS ( [website repo⁠](https://github.com/Porges/ways-to-play/tree/main "<code>ways-to-play</code>: ‘A Site About Games’")), by [George Pollard](https://games.porg.es/about/).

Example pages: [“The Pigeon Lottery”](https://games.porg.es/games/pigeon-lottery/ "The Pigeon Lottery"), [“The History & Art of _Hanafuda_”](https://games.porg.es/articles/cards/japan/hanafuda/art/).

![Screenshot of “The Pigeon Lottery” showing rubricated margin-notes & sidenotes.](https://gwern.net/doc/design/typography/sidenote/2025-04-06-georgepollard-waystoplay-thepigeonlottery-sidenotescreenshot.png)

Screenshot of “The Pigeon Lottery” showing rubricated margin-notes & sidenotes.

**[Backlinks (1)⁠](https://gwern.net/design#backlink) for [⁠“George Pollard”⁠](https://gwern.net/sidenote#george-pollard):**

- [Sidenotes In Web Design⁠](https://gwern.net/sidenote) ( [context⁠](https://gwern.net/sidenote#gwern-1876329077)):


> [⁠\[backlink context\]](https://gwern.net/sidenote)


## [Miscellaneous](https://gwern.net/sidenote\#miscellaneous "Link to section: § 'Miscellaneous'")

Some implementations are just bad ideas or not worth discussing in detail with screenshots:

- [ILoveTypography.com](https://ilovetypography.com/2019/03/14/the-first-printed-math-books/ "'The First Printed Math Books', Boardley 2019") uses image captions & margin notes which, like Tufte-CSS, are floated/outdented right, but bizarrely, it uses _figure captions_—just [`<figcaption>`⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) with a special class inside an empty `<figure>` with no images!

This is invalid HTML, fails badly in some cases (eg. in the linked example, one margin note is almost unreadable because it overlaps with a giant pull-quote illustration), and has no advantage over a `<span>` that I can find; it does at least degrade gracefully into pop-in (default expanded) block elements on narrow/mobile.

- [BLDBLOG⁠](https://bldgblog.com/2015/12/four-floor-war/ "The Four-Floor War") generally avoids complex layout and footnotes entirely, and doesn’t have much margin to put sidenotes in, so I was surprised while reading the archives to find one post which has a left margin note, and even more surprised to check the HTML source and see that the ‘margin note’ is in fact a _header_: a `<h6>`.

Huh‽ It turns out that the header is floated left with some gruesome CSS. Said Achmiz summaries how the Rube Goldberg contraption works:


> The CSS uses absolute positioning. The nearest positioned ancestor is `<article>`, not `.entry-content`. Within `<article>`, `.entry-content` is right-floated and has a fixed width. This creates a variable-width space on the left (determined by how much horizontal space is left within `<article`\> after that fixed width is subtracted). The sidenote `<h6>` is then set with `position:absolute` and `left:0`. Vertical position is left unspecified, relying on the way browsers implement absolute positioning (ie. to place an element where it would be placed if position were `static`) to put it in the right place. Fragile, unsemantic, & hacky.

- [MIT Admissions](https://mitadmissions.org/blogs/entry/we-are-reinstating-our-sat-act-requirement-for-future-admissions-cycles/ "We are reinstating our SAT/ACT requirement for future admissions cycles") uses a footnote-sidenote hybrid:
![MIT Admissions blog, demonstrating fixed-floating sidenote](https://gwern.net/doc/design/typography/sidenote/2022-03-28-mitadmissions-footnotesidenote.png)

MIT Admissions blog, demonstrating fixed-floating sidenote


Span-annotated footnote links (with the trigger text lightly highlighted in red), on hover, trigger JS to create a single sticky/floating ‘sidenote’ which is located in the bottom-right corner; hovers on other footnotes replace it with their contents. (Layout does not take into account the sidebar or anything that may already be there, and the footnote popup box simply appears over it.)

For mobile/narrow windows, it uses pop-in, but not as a block element, instead, inline with red-colored brackets to delimit it:
![Mobile: popins but using rubricated bracket delimiters.](https://gwern.net/doc/design/typography/sidenote/2022-03-28-mitadmissions-footnotesidenote-mobilepopins-rubricated.png)

Mobile: popins but using rubricated bracket delimiters.

- [Evan Ovadia](https://verdagon.dev/home) ( [eg.](https://verdagon.dev/blog/linear-types-borrowing "What Vale Taught Me About Linear Types, Borrowing, and Memory Safety")): content & sidenotes are put into pairs of columns. Presumably does not handle many long sidenotes gracefully.

For mobile/narrow, it collapses them as a row of numbered links to expand on click.

- [Simon Tatham](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/commit-messages/ "'Writing commit messages', Simon Tatham 2024-05-19"): uses a highly unusual footnote format which I can’t decide if it’s a footnote or a sidenote.

Footnotes are duplicated in button toggles & at the bottom; footnote numbered anchors are set to the right margin, and when clicked, ‘popin’, but _to the side_ of the text, which reflows into a left text column vs right footnote column (no JS, just CSS+HTML):
![Tatham’s popin-sidenotes, expanded](https://gwern.net/doc/design/typography/sidenote/2024-05-25-simontatham-popinfootnotesidenote-expanded.png)

Tatham’s popin-sidenotes, expanded


# [See Also](https://gwern.net/sidenote\#see-also "Link to section: § 'See Also'")

- [Project Xanadu⁠](https://en.wikipedia.org/wiki/Project_Xanadu "Project Xanadu")


# [External Links](https://gwern.net/sidenote\#external-links "Link to section: § 'External Links'")

- Discussion: [HN⁠](https://news.ycombinator.com/item?id=37619361)

- [Quotebacks](https://quotebacks.net/) ( [“Introducing: Quotebacks—A Chrome extension to quote the web”](https://tomcritchlow.com/2020/06/09/quotebacks/))

- [“Expounder”](https://skorokithakis.github.io/expounder/), Stavros Korokithakis (inline alternative to [`<abbr`⁠](https://gwern.net/sidenote#mozdev-abbr)/ [`<defn>`⁠](https://gwern.net/sidenote#mozdev-defn) tags)

- [“Usability of Footnotes”](https://shkspr.mobi/blog/2020/07/usability-of-footnotes/); [“A (terrible?) way to do footnotes in HTML”](https://shkspr.mobi/blog/2020/12/a-terrible-way-to-do-footnotes-in-html/)

- [“Nutshell”](https://ncase.me/nutshell-wip/), Nicky Case 2021

- [“LW Beta Feature: Side-Comments”⁠](https://www.lesswrong.com/posts/A33sgjYoM4Ko9viJv/lw-beta-feature-side-comments)

- [“A library of words: Discovering _Roget’s Thesaurus_”⁠](https://austinkleon.substack.com/p/a-library-of-words "Austin Kleon, 2023-02-07")


* * *

[Link to section: § ‘Footnotes’](https://gwern.net/sidenote#footnotes "Link to section: § ‘Footnotes’")

1. [Link to footnote 1](https://gwern.net/sidenote#fn1 "Link to footnote 1")
You _can_ imagine web pages with true footnotes: where a sticky bottom margin is created, reserved for footnotes, and JS inserts the relevant footnotes into that as the user scrolls, but I’m not sure I’ve ever seen this outside of book skeuomorph web designs with explicit pagination, and screens are small enough that users would chafe at the loss of [vertical pixels⁠](https://x.com/admittedlyhuman/status/430532517389561856 "Every vertical pixel used for the UI bar signifies a theft from those who hunger and are not fed, those who are cold and are not clothed.").

Then should we put our notes on entirely separate pages? No: this only adds to the reader’s burden, and it’s even more work for the author. (The dedicated might embrace hypertextuality and create an enormous web of small nuggets of text which include and go beyond endnotes, but for people writing online, URLs/pages tend to be “heavyweight”, and a commitment, often corresponding to a single file on disk; creating hundreds of endnote-sized URLs also creates its own problems like naming, refinding, and navigating them.)

2. [Link to footnote 2](https://gwern.net/sidenote#fn2 "Link to footnote 2")
You can use the [`sidenotes`⁠](https://ctan.org/pkg/sidenotes "The package allows typesetting of texts with notes, figures, citations, captions and tables in the margin. This is common (for example) in science text books.")/ [`sidenotesplus`⁠](https://ctan.org/pkg/sidenotesplus "sidenotesplus: Place referenced notes, alerts, figures and tables into the document margin")/ [`snotez`⁠](https://ctan.org/pkg/snotez "snotez: Typeset notes, in the margin") packages, or the somewhat different \[`marginnote`\](https://ctan.org/pkg/marginnote “This package provides the command `\marginnote`{.LaTeX

3. [Link to footnote 3](https://gwern.net/sidenote#fn3 "Link to footnote 3")
Tufte-CSS sidenotes do not correctly support block elements like lists or paragraphs, because spans are inline and those are block elements; but [this is fixable⁠](https://github.com/edwardtufte/tufte-css/issues/93#issuecomment-670695382 "HTML list elements in sidenote do not appear correctly").

4. [Link to footnote 4](https://gwern.net/sidenote#fn4 "Link to footnote 4")
A simple way to provide ‘on hover’ annotations is to use HTML title tooltips, which was [my first popup system attempt⁠](https://gwern.net/design-graveyard#tooltips); Tyler Vigen attempts to provide his collapsed-inline footnotes as tooltips as well to minimize clicking & effort.

But while simple, tooltips bring in many problem discussed in my tooltip post-mortem, and several of them show up here: there is no way to ‘expand’ or search any of the tooltips, and because tooltips are capable only of containing plain text, while footnotes can (and Vigen’s do) contain multiple block elements like blockquotes or photos. There is no useful way to condense such footnotes into a tooltip, and Vigen’s tooltips often silently drop large parts of the footnote—rendering them worse than useless.

5. [Link to footnote 5](https://gwern.net/sidenote#fn5 "Link to footnote 5")
Some websites, like Grantland or Stratechery, support floating footnotes… but only when the user clicks! (Better is Grantland’s [history of the Gracies](https://grantland.com/one-hundred-years-arm-bars-gracie-jiu-jitsu-mma/ "One Hundred Years of arm bars: A family epic spanning the Gracie jiu-jitsu dynasty’s generations of combat and betrayal, from the Amazon to Hollywood to the UFC"), which helps the reader keep the clan straight by popping into the left margin an annotated family tree whenever they click a Gracie name.) FiveThirtyEight, on the other hand, does pop-in footnotes—but not sidenotes, despite ample margin. Compare [_Atlantic_’s web rendering⁠](https://www.theatlantic.com/magazine/archive/2005/04/host/303812/ "Host") using pop-ins with the original [2005 David Foster Wallace⁠](https://gwern.net/doc/sociology/2005-wallace.pdf "Host: Deep into the mercenary world of take–no–prisoners political talk radio") print essay which used elaborate recursive sidenotes integrated in unusual geometries. (Said Achmiz offers [an example⁠](https://gwern.net/doc/design/typography/sidenote/2005-wallace-redesign.pdf "'Host: Deep into the mercenary world of take-no-prisoners political talk radio [footnote redesign]', Achmiz 2020") of a less ugly redesign of that.)

6. [Link to footnote 6](https://gwern.net/sidenote#fn6 "Link to footnote 6")
Although arguably one should not (and I avoid doing so). If a footnote needs to be linked, it should be given a `<span>` anchor with a name. Pandoc footnote anchors/numbers are inherently unstable, and worse, tend to fail silently: the link just changes to a different footnote, and continues to ‘work’. And if anyone _needs_ to link a specific footnote it may be time to rewrite that footnote into a more-linkable section or appendix.


# [Backlinks](https://gwern.net/sidenote\#backlinks-section "Link to section: § 'Backlinks'")

- [Singular: Possible futures of the singularity](https://jamesyu.org/singular/):


> [\[backlink context\]](https://jamesyu.org/singular/ "Content is loading. Please wait.")

- [Subscripts For Citations⁠](https://gwern.net/subscript "'Subscripts For Citations', Gwern 2020") ( [⁠full context⁠](https://gwern.net/subscript#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/subscript "Content is loading. Please wait.")

- [Rubrication Design Examples⁠](https://gwern.net/red "'Rubrication Design Examples', Gwern 2019") ( [⁠full context⁠](https://gwern.net/red#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/red "Content is loading. Please wait.")

- [Design Of This Website⁠](https://gwern.net/design "'Design Of This Website', Gwern 2010") ( [⁠full context⁠](https://gwern.net/design#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/design "Content is loading. Please wait.")

- [Design Of This Website⁠](https://gwern.net/design "'Design Of This Website', Gwern 2010") ( [⁠full context⁠](https://gwern.net/design#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/design "Content is loading. Please wait.")

- [Design Of This Website⁠](https://gwern.net/design "'Design Of This Website', Gwern 2010") ( [⁠full context⁠](https://gwern.net/design#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/design "Content is loading. Please wait.")

- [Design Graveyard⁠](https://gwern.net/design-graveyard "'Design Graveyard', Gwern 2010") ( [⁠full context⁠](https://gwern.net/design-graveyard#gwern-sidenote)):


> [⁠\[backlink context\]](https://gwern.net/design-graveyard "Content is loading. Please wait.")


# [Similar Links](https://gwern.net/sidenote\#similars-section "Link to section: § 'Similar Links'")

- [Design Of This Website § Returns To Design?⁠](https://gwern.net/design#returns-to-design)

- [Design Of This Website § Backlink⁠](https://gwern.net/design#backlink)

- [Design Of This Website § Tags⁠](https://gwern.net/design#tags)

- [Design Graveyard § Popup Annotations⁠](https://gwern.net/design-graveyard#popup-annotations)

- [Design Graveyard § Link-Icon CSS Regexps⁠](https://gwern.net/design-graveyard#link-icon-css-regexps)

- [Design Graveyard § srcset Mobile Optimization⁠](https://gwern.net/design-graveyard#srcset-mobile-optimization)

- [Design Graveyard § Interviews⁠](https://gwern.net/design-graveyard#interviews)

- [A/B testing long-form readability on Gwern.net⁠](https://gwern.net/ab-test)

- [A/B testing long-form readability on Gwern.net § Covariate Impact On Power⁠](https://gwern.net/ab-test#covariate-impact-on-power)

- [A/B Testing Indentation & Justification⁠](https://gwern.net/ab-test-indent)

- [Subscripting Typographic Convention For Citations/Dates/Sources/Evidentials: A Proposal⁠](https://www.lesswrong.com/posts/NkjPp86uuyunxDoB8/subscripting-typographic-convention-for-citations-dates)

- [Manual of Style⁠](https://gwern.net/style-guide)

- [About This Website⁠](https://gwern.net/about)

- [Poetry HTML Typesetting⁠](https://gwern.net/poetry-html)

- [Supporting document development with Concordia⁠](https://gwern.net/doc/cs/lisp/emacs/1988-walker.pdf)

- [Tufte-CSS: Sidenotes: Footnotes and Marginal Notes⁠](https://edwardtufte.github.io/tufte-css/#sidenotes)

- **Search**: [GS⁠](https://scholar.google.com/scholar?q=%22Sidenotes%20In%20Web%20Design%22 "Reverse citations of this paper in Google Scholar"); [Google⁠](https://www.google.com/search?q=%22Sidenotes%20In%20Web%20Design%22 "Google search engine hits for ‘Sidenotes In Web Design’."); [site⁠](https://www.google.com/search?q=site:gwern.net+-site:gwern.net/metadata/Sidenotes%20In%20Web%20Design "Gwern.net site-wide search hits for ‘Sidenotes In Web Design’.")


[\[Similar links by topic\]⁠](https://gwern.net/metadata/annotation/similar/%252Fsidenote.html "Content is loading. Please wait.")

# [Bibliography](https://gwern.net/sidenote\#link-bibliography-section "Link to section: § 'Bibliography'")

[\[Bibliography of links/references used in page\]⁠](https://gwern.net/metadata/annotation/link-bibliography/%252Fsidenote.html "Content is loading. Please wait.")

[​](https://gwern.net/index "Gwern.net homepage")

nullnull

null

**Arrow keys:** Next/previous image

**Escape** or **click**: Hide zoomed image

**Space bar:** Reset image size & position

**Scroll** to zoom in/out

(When zoomed in, **drag** to pan;

**double-click** to reset size & position)

null

null


null


[Sidenotes In Web Design](https://gwern.net/sidenote#top)