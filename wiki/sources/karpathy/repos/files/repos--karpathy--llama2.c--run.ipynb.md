---
type: source
subject: "GitHub source repos/karpathy/llama2.c/run.ipynb"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/run.ipynb]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/run.ipynb

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/run.ipynb), SHA-256 `c670a207a6009c4e887d91b83caccc9a3651f7b7704747116fdec1693e237e6c`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
{ "cells": \[ { "cell_type": "markdown", "metadata": { "id": "HLdoj4cz-xal" }, "source": \[ "# Run.c\n",
```

llama2.c Colab run notebook fully read, no embedded executed outputs. Clone, fast build, select15M42M110M downloadable TinyStories model, adjust token/temperature/nucleus sliders and prompt, run CLI. Optional gated Meta7B download uses placeholder HF token and export. Notebook is demo convenience, no execution proof. Shell command constructed from unescaped prompt is unsafe for untrusted prompt strings; retain evidence but do not copy unsafe interpolation. No credential or download used.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HLdoj4cz-xal"
      },
      "source": [
        "# Run.c\n",
        "\n",
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/karpathy/llama2.c/blob/master/run.ipynb)\n",
        "\n",
        "More details can be found in the [README.md](README.md) ."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Une3Ozlnu1B7"
      },
      "outputs": [],
      "source": [
        "#@title Clone Project\n",
        "\n",
        "!git clone https://github.com/karpathy/llama2.c.git\n",
        "%cd llama2.c"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "#@title Build\n",
        "\n",
        "!make runfast"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "thm0ZBrtSgoC"
      },
      "outputs": [],
      "source": [
        "#@title Pick Your Model\n",
        "\n",
        "#@markdown Choose model\n",
        "model = \"stories15M\" #@param [\"stories15M\", \"stories42M\", \"stories110M\"]\n",
        "\n",
        "download_url = \"\"\n",
        "\n",
        "if(model == \"stories15M\"):\n",
        "  download_url = \"https://huggingface.co/karpathy/tinyllamas/resolve/main/stories15M.bin\"\n",
        "if(model == \"stories42M\"):\n",
        "  download_url = \"https://huggingface.co/karpathy/tinyllamas/resolve/main/stories42M.bin\"\n",
        "if(model == \"stories110M\"):\n",
        "  download_url = \"https://huggingface.co/karpathy/tinyllamas/resolve/main/stories110M.bin\"\n",
        "\n",
        "print(f\"download_url: {download_url}\")\n",
        "\n",
        "!wget $download_url\n",
        "\n",
        "model_file = model + \".bin\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OgAc3KjuT-NM"
      },
      "outputs": [],
      "source": [
        "#@title Generate Stories\n",
        "\n",
        "# Generate args\n",
        "max_token = 256 #@param {type:\"slider\", min:32, max:1024, step:32}\n",
        "temperature = 0.8 #@param {type:\"slider\", min:0.0, max:1, step:0.05}\n",
        "top_p = 0.9 #@param {type:\"slider\", min:0.0, max:1.0, step:0.05}\n",
        "prompt = \"One day, Lily met a Shoggoth\" #@param {type:\"string\"}\n",
        "\n",
        "print(f\"model: {model_file}, max_token: {max_token}, temperature: {temperature}, top_p: {top_p}, prompt: {prompt}\")\n",
        "print(f\"----------------------------\\n\")\n",
        "\n",
        "cmd = f'./run {model_file} -t {temperature} -p {top_p} -n {max_token} -i \"{prompt}\"'\n",
        "!{cmd}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "#@title Run Meta's Llama 2 models\n",
        "\n",
        "#@markdown input your huggingface [access token](https://huggingface.co/settings/tokens) to download Meta's Llama 2 models.\n",
        "\n",
        "from huggingface_hub import snapshot_download\n",
        "\n",
        "token = \"replace your huggingface access token\" #@param {type:\"string\"}\n",
        "path = snapshot_download(repo_id=\"meta-llama/Llama-2-7b\",cache_dir=\"Llama-2-7b\", use_auth_token=token)\n",
        "\n",
        "!python export.py llama2_7b.bin --meta-llama $path\n",
        "\n",
        "print(\"./run llama2_7b.bin\\n\")\n",
        "!./run llama2_7b.bin"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
