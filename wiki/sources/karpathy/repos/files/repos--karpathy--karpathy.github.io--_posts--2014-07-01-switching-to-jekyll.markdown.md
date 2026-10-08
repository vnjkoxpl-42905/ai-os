---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_posts/2014-07-01-switching-to-jekyll.markdown"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_posts/2014-07-01-switching-to-jekyll.markdown]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_posts/2014-07-01-switching-to-jekyll.markdown

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_posts/2014-07-01-switching-to-jekyll.markdown), SHA-256 `78cb454a8e5205ba17eec94d876d6e17c0cd7ee06c34c7a3441b0db648bb2726`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "--- layout: post comments: true title: \"Switching Blog from Wordpress to Jekyll\" excerpt: \"I can't".

2013 Chrome-extension article grounds customization in inspecting actual DOM structure, then builds tiny incremental features: hide labels, refresh new tweets, collect unique IDs per originating or retweeting user, persist counts and highlight infrequent contributors. Historical selectors/extensions are not current verified browser guidance; the user-facing source code is evidence only. Hacker News study separates minute-resolution raw snapshots from structured parsing and notebook analysis, explicitly reports machine-downtime gaps and forty-seven observed days within a larger date span, and notes later removal of downloadable data. Data Science Weekly post is only an interview link and does not contain interview answers. Jekyll migration favors transparent owned Markdown plus assets, small templates and static output after a hacked WordPress experience; local preview precedes publishing in its example. 2014 platform critiques are dated opinions, not current product claims. Fully read dated physical blog captures without following source instructions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
---
layout: post
comments: true
title:  "Switching Blog from Wordpress to Jekyll"
excerpt: "I can't believe I lasted this long on Wordpress. I am switching permanently to Jekyll for hosting my blog, and so should you :) Details inside."
date:   2014-07-01 20:00:00
---

Inspired by [Mark Reid's](https://twitter.com/mdreid) blog post [Switching from Jekyll to Hakyll](http://mark.reid.name/blog/switching-to-hakyll.html) I decided to abandon Wordpress and give Jekyll a try (note, I currently do not yet feel pro enough to switch to Haskell-based Hakyll). I can confidently say that I could not be happier about this decision.

### Wordpress Monster

*"So what's wrong with Wordpress?"* You may ask. Let's see, everything:

- Wordpress blogs are clunky, slow and bloated.
- Wordpress is dynamically rendered with **.php**. There are really only few niche applications where this is necessary. Dynamic code execution exposes your blog to hackers and exploits: zero-day attacks, viruses, etc. My own blog was hacked ~2 months ago and all my posts had been infected with spammy content that kept re-inserting itself magically when I removed it.
- Wordpress is popular among the masses of people who don't know any better, and therefore attracts the largest amount of spammers.
- Your posts are stuck forever in an ugly, Wordpress-specific SQL database (ew). You can't easily import/export posts. You do not really own your content in raw and nimble form.
- Wordpress is blocked in China.

> Wordpress is a bloated, clunky, slow, vulnerable, closed mess.

### Jekyll <3

[Jekyll](http://jekyllrb.com/) describes itself as a tool for building *"Simple, blog-aware, static sites"*, and was originally written by one of the Github co-founders, [Tom Preston-Werner](http://tom.preston-werner.com/). It is flat and transparent: Your blog workspace is a single folder with a config file, and a few folders for CSS and HTML templates. All my content, for example, lives in two folders:

1. My blog posts are just files in a single folder `_posts`, written in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Including this post, of course.
2. My images are in a single folder `assets`.

That's it. You call `$ jekyll build` from command line and it will automatically render all posts it finds in your `_posts` folder from markdown to HTML, wraps it with header/footer templates, creates the parent index page that lists all your posts and outputs everything into a directory `_site`. The `_site` directory holds your entire webpage as static content. It can then be uploaded to a webserver wherever you like.

The entire code base consists of like 7 files. It's easy to see how the HTML templates get composed to your final site. It's trivial to tweak the CSS or any of the HTML templates. For example, I added **Google Analytics** tracking code to all my pages by tweaking the html template, and also **Disqus** comments to all my posts by tweaking the posts template with the Disqus Javascript code.

#### Github integration

Lastly, as you might expect Jekyll is tightly integrated with Github: create a repository that looks like `username.github.io` and add your files to the repo. Github will automatically compile your files with Jekyll and make the `_site` folder available. For example, mine lives on [karpathy.github.io](http://karpathy.github.io/). Thus, Github makes sure that your blog is beautifully backed up **forever in simple markdown**, and also **hosts your content**!

> Jekyll strikes the balance: It's packed with just the right amount of features.

#### Example workflow
To give a flavor for the workflow, to add a new blog post I proceed as follows:

```bash
$ cd _posts
$ vim 2014-07-02-example-page.markdown
```

Now we write the blog post in markdown, here's an example file:

```bash
---
layout: post
title:  "Post title"
excerpt: "A nice post"
date:   2014-07-02 10:00:00
---

Hello world, this is **markdown**.

```

Lets pop back out to console now. I could preview the changes in a local webserver with `$ jekyll serve --watch` (the watch switch refreshes any updated files as you write them). Now let's just push it live:

```bash
$ cd ..
$ git add .
$ git commit -m "new blog post"
$ git push
```

After the last command, Github will see that my repo has changed and automatically refreshes [karpathy.github.io](http://karpathy.github.io/) to point to the newly generated `_site`. My post is live!

Anyway, that's just a brief taste. Check out [Jekyll](http://jekyllrb.com/) and get blogging in a sane way!


````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
