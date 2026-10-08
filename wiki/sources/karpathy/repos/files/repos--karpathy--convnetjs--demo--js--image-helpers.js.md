---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/js/image-helpers.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/js/image-helpers.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/js/image-helpers.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/js/image-helpers.js), SHA-256 `b2751fd70e619e15258cf9667983a31b313b42b1a35ffab81a5a4e9ad25d1a59`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "var loadFile = function(event) { var reader = new FileReader(); reader.onload = function(){ var preview".

Automatic prediction imports consistent CSV rows, infers numeric versus categorical columns, reuses training category mappings for test data, holds out a random test subset, exposes cross-validation progress and logs predicted versus actual test labels. Its neurons_max mistakenly reads nnmin in startCV and restart creates additional intervals, so intended controls are not guaranteed. Toy classification trains simple datasets and displays how the input grid and points deform into selected internal coordinates. Image helpers crop and resize uploaded images but use asynchronous images without waiting and return before resize callbacks, making reliability uncertain. These mechanics illustrate inspectable learning, with explicit source-level limitations and no runtime test.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

var loadFile = function(event) {
var reader = new FileReader();
reader.onload = function(){
  var preview = document.getElementById('preview_img');
  preview.src = centerCrop(reader.result);
  preview.src = resize(preview.src);
};
reader.readAsDataURL(event.target.files[0]);
};

function centerCrop(src){
    var image = new Image();
    image.src = src;

    var max_width = Math.min(image.width, image.height);
    var max_height = Math.min(image.width, image.height);

    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    canvas.width = max_width;
    canvas.height = max_height;
    ctx.drawImage(image, (max_width - image.width)/2, (max_height - image.height)/2, image.width, image.height);
    return canvas.toDataURL("image/png");
}

function resize(src){
    var image = new Image();
    image.src = src;

    var canvas = document.createElement('canvas');
    canvas.width = image.width;
    canvas.height = image.height;
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 0, image.width, image.height);

    var dst = document.createElement('canvas');
    dst.width = image_dimension;
    dst.height = image_dimension;

    window.pica.WW = false;
    window.pica.resizeCanvas(canvas, dst, {
    quality: 2,
    unsharpAmount: 500,
    unsharpThreshold: 100,
    transferable: false
  }, function (err) {  });
    window.pica.WW = true;
    return dst.toDataURL("image/png");
}
  

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
