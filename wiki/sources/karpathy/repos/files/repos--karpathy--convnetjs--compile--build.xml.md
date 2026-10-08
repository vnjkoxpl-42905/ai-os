---
type: source
subject: "GitHub source repos/karpathy/convnetjs/compile/build.xml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/compile/build.xml]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/compile/build.xml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/compile/build.xml), SHA-256 `ba2b1a00b1874b60da165439fd9d6dd48c2595146797d0f714a95a42dab80526`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<project name="Build" default="compress"> <target name="concatenate"> <concat destfile="../build/convnet.js" encoding="UTF-8" outputencoding="UTF-8" fixlastline="true"> <filelist id="filelist" dir="../src"> <file name="convnet_init.js"/>
```

Char-rnn utilities explicitly credit adapted parameter flattening code and preserve shared storage across timestep clones; OneHot caches the identity matrix. Convnet build concatenates a declared layer order and minifies via YUI. Autoencoder demo explains a bottleneck as the mechanism forcing useful compressed representations and exposes live loss, neurons and snapshots. MagicNet demo explicitly states CSV assumptions, separates training/validation/test roles, cross-validates architectures and ensembles selected models, with export/import. The explanatory demos support interactive inspection and held-out evaluation; external datasets and borrowed utilities are not independently authored philosophy, and no browser training was performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<project name="Build" default="compress">
  <target name="concatenate">
    <concat destfile="../build/convnet.js" encoding="UTF-8" outputencoding="UTF-8" fixlastline="true">
      <filelist id="filelist" dir="../src">
        <file name="convnet_init.js"/>
        <file name="convnet_util.js" />
        <file name="convnet_vol.js" />
        <file name="convnet_vol_util.js" />
        <file name="convnet_layers_dotproducts.js" />
        <file name="convnet_layers_pool.js" />
        <file name="convnet_layers_input.js" />
        <file name="convnet_layers_loss.js" />
        <file name="convnet_layers_nonlinearities.js" />
        <file name="convnet_layers_dropout.js" />
        <file name="convnet_layers_normalization.js" />
        <file name="convnet_net.js" />
        <file name="convnet_trainers.js" />
        <file name="convnet_magicnet.js" />
        <file name="convnet_export.js" />
      </filelist>
    </concat>
  </target>
  <target name="compress" depends="concatenate" description="Minify convnet.js to convnet-min.js">
    <apply executable="java" parallel="false">
      <filelist dir="../build" files="convnet.js" />
      <arg line="-jar" />
      <arg path="yuicompressor-2.4.8.jar" />
      <srcfile />
      <arg line="-o" />
      <mapper type="glob" from="*.js" to="../build/*-min.js" />
      <targetfile />
    </apply>
  </target>
</project>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
