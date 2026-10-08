---
type: source
subject: "GitHub source repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/boot.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/boot.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/boot.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/lib/jasmine-2.0.0/boot.js), SHA-256 `06d3b00fc21747308d1e087471eb4ab2142280a240d3fcb029f79dc2034e9907`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "/** Starting with version 2.0, this file \"boots\" Jasmine, performing all of the necessary initialization".

Trainer accumulates gradients until batch boundaries, adds L1 and L2 terms and implements SGD momentum, Adagrad, moving-window gradients, Adadelta, Nesterov and Adam. Adam bias corrections multiply rather than divide by one-minus-beta-power; this historical implementation must not be treated as a current correct reference. Utilities provide cached Box-Muller Gaussian sampling, typed-array zeros, permutations and weighted sampling with assumed normalized probabilities. Vol holds weights and gradients, initializes variance proportional to inverse fan-in and deliberately serializes weights but not gradients. Augmentation square-crops with zero-padding outside bounds and flips; grayscale takes the red channel rather than luminance and image conversion aborts selected browser errors. Jasmine boot is vendored third-party test framework initialization and contributes no Karpathy persona claim. Full source read, no execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
/**
 Starting with version 2.0, this file "boots" Jasmine, performing all of the necessary initialization before executing the loaded environment and all of a project's specs. This file should be loaded after `jasmine.js`, but before any project source files or spec files are loaded. Thus this file can also be used to customize Jasmine for a project.

 If a project is using Jasmine via the standalone distribution, this file can be customized directly. If a project is using Jasmine via the [Ruby gem][jasmine-gem], this file can be copied into the support directory via `jasmine copy_boot_js`. Other environments (e.g., Python) will have different mechanisms.

 The location of `boot.js` can be specified and/or overridden in `jasmine.yml`.

 [jasmine-gem]: http://github.com/pivotal/jasmine-gem
 */

(function() {

  /**
   * ## Require &amp; Instantiate
   *
   * Require Jasmine's core files. Specifically, this requires and attaches all of Jasmine's code to the `jasmine` reference.
   */
  window.jasmine = jasmineRequire.core(jasmineRequire);

  /**
   * Since this is being run in a browser and the results should populate to an HTML page, require the HTML-specific Jasmine code, injecting the same reference.
   */
  jasmineRequire.html(jasmine);

  /**
   * Create the Jasmine environment. This is used to run all specs in a project.
   */
  var env = jasmine.getEnv();

  /**
   * ## The Global Interface
   *
   * Build up the functions that will be exposed as the Jasmine public interface. A project can customize, rename or alias any of these functions as desired, provided the implementation remains unchanged.
   */
  var jasmineInterface = {
    describe: function(description, specDefinitions) {
      return env.describe(description, specDefinitions);
    },

    xdescribe: function(description, specDefinitions) {
      return env.xdescribe(description, specDefinitions);
    },

    it: function(desc, func) {
      return env.it(desc, func);
    },

    xit: function(desc, func) {
      return env.xit(desc, func);
    },

    beforeEach: function(beforeEachFunction) {
      return env.beforeEach(beforeEachFunction);
    },

    afterEach: function(afterEachFunction) {
      return env.afterEach(afterEachFunction);
    },

    expect: function(actual) {
      return env.expect(actual);
    },

    pending: function() {
      return env.pending();
    },

    spyOn: function(obj, methodName) {
      return env.spyOn(obj, methodName);
    },

    jsApiReporter: new jasmine.JsApiReporter({
      timer: new jasmine.Timer()
    })
  };

  /**
   * Add all of the Jasmine global/public interface to the proper global, so a project can use the public interface directly. For example, calling `describe` in specs instead of `jasmine.getEnv().describe`.
   */
  if (typeof window == "undefined" && typeof exports == "object") {
    extend(exports, jasmineInterface);
  } else {
    extend(window, jasmineInterface);
  }

  /**
   * Expose the interface for adding custom equality testers.
   */
  jasmine.addCustomEqualityTester = function(tester) {
    env.addCustomEqualityTester(tester);
  };

  /**
   * Expose the interface for adding custom expectation matchers
   */
  jasmine.addMatchers = function(matchers) {
    return env.addMatchers(matchers);
  };

  /**
   * Expose the mock interface for the JavaScript timeout functions
   */
  jasmine.clock = function() {
    return env.clock;
  };

  /**
   * ## Runner Parameters
   *
   * More browser specific code - wrap the query string in an object and to allow for getting/setting parameters from the runner user interface.
   */

  var queryString = new jasmine.QueryString({
    getWindowLocation: function() { return window.location; }
  });

  var catchingExceptions = queryString.getParam("catch");
  env.catchExceptions(typeof catchingExceptions === "undefined" ? true : catchingExceptions);

  /**
   * ## Reporters
   * The `HtmlReporter` builds all of the HTML UI for the runner page. This reporter paints the dots, stars, and x's for specs, as well as all spec names and all failures (if any).
   */
  var htmlReporter = new jasmine.HtmlReporter({
    env: env,
    onRaiseExceptionsClick: function() { queryString.setParam("catch", !env.catchingExceptions()); },
    getContainer: function() { return document.body; },
    createElement: function() { return document.createElement.apply(document, arguments); },
    createTextNode: function() { return document.createTextNode.apply(document, arguments); },
    timer: new jasmine.Timer()
  });

  /**
   * The `jsApiReporter` also receives spec results, and is used by any environment that needs to extract the results  from JavaScript.
   */
  env.addReporter(jasmineInterface.jsApiReporter);
  env.addReporter(htmlReporter);

  /**
   * Filter which specs will be run by matching the start of the full name against the `spec` query param.
   */
  var specFilter = new jasmine.HtmlSpecFilter({
    filterString: function() { return queryString.getParam("spec"); }
  });

  env.specFilter = function(spec) {
    return specFilter.matches(spec.getFullName());
  };

  /**
   * Setting up timing functions to be able to be overridden. Certain browsers (Safari, IE 8, phantomjs) require this hack.
   */
  window.setTimeout = window.setTimeout;
  window.setInterval = window.setInterval;
  window.clearTimeout = window.clearTimeout;
  window.clearInterval = window.clearInterval;

  /**
   * ## Execution
   *
   * Replace the browser window's `onload`, ensure it's called, and then run all of the loaded specs. This includes initializing the `HtmlReporter` instance and then executing the loaded Jasmine environment. All of this will happen after all of the specs are loaded.
   */
  var currentWindowOnload = window.onload;

  window.onload = function() {
    if (currentWindowOnload) {
      currentWindowOnload();
    }
    htmlReporter.initialize();
    env.execute();
  };

  /**
   * Helper function for readability above.
   */
  function extend(destination, source) {
    for (var property in source) destination[property] = source[property];
    return destination;
  }

}());

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
