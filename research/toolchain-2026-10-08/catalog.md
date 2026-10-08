# A broad tool catalog without unnecessary repeat installations

Verified and organized 2026-10-08 for Joshua's Windows laptop. This accounts for every named example in the preceding tool list. Nothing was installed or downloaded during this inventory.

## How to use this list in an IDE

The main candidate tables retain tools with a distinct useful capability, even when related tools overlap. Already available tools are recorded separately and are not download recommendations. Only a paid tool or an already-covered exact need is excluded outright. Do not interpret this file as an instruction to install everything.

Use local/free editions, official upstream downloads or reputable package registries. Do not enable paid add-ons, hosted inference, automatic credit purchases, cloud provisioning or metered API calls. Free software does not make its external services free. Check the current license and installation requirements when selecting a tool, especially for commercial redistribution. No paid hosting or transcription service is required by the local-tool candidates.

Status: **Available** means a concrete executable/package was detected. **Bundled** means accessible through Codex's dependency runtime, not necessarily installed in the IDE's default interpreter. **Candidate** means not verified as available; absence from PATH/winget is not proof of absence in every virtual environment. **Conditional** means the free scope or external billing boundary needs attention.

## Already available: do not download again

| Tool | Verified availability | Use |
|---|---|---|
| Python | User Python 3.12.10; also Codex bundle | General scripts, extraction and data processing |
| Node.js / JavaScript | PATH Node 24.21.0; also Codex bundle | JavaScript scripts, integrations and applications |
| PowerShell | Windows PowerShell and bundled pwsh detected | Windows automation |
| Git | PATH executable and Codex bundle | Source/version management |
| GitHub CLI | Installed 2.102.0 | GitHub operations |
| Google Workspace CLI / gws | PATH executable | Existing authorized Workspace access |
| Firecrawl CLI | PATH; authenticated with existing root .env key when loaded | Web extraction; hosted calls consume existing credits, not unlimited free usage |
| ripgrep | PATH executable | Fast text search |
| curl | Windows executable | HTTP requests |
| 7-Zip | Installed 26.04; separate recovery-toolchain executable on PATH | Archive creation and extraction |
| winget | Windows executable | Windows package management |
| pip | User Python executable | Python packages |
| npm | 11.19.0 on PATH | JavaScript packages |
| pnpm | Codex bundled executable | JavaScript package management |
| Windows Terminal | Installed 1.24.12741 | Terminal sessions |
| yt-dlp | WinGet package 2026.08.19; resolves by command name after refreshing this shell from the saved user PATH | Media/subtitle/metadata retrieval |
| FFmpeg suite | WinGet package N-126374-g089a48eb36-20260831; ffmpeg, ffprobe and ffplay all report the installed build by package path | Media conversion, metadata and playback |
| Deno | WinGet package 2.9.7; version command succeeds by package path | JavaScript runtime used by yt-dlp's YouTube challenge support |
| uv | WinGet package 0.12.23; resolves by command name after refreshing this shell from the saved user PATH; uv --version and uv --help verified | Fast isolated Python environments, dependency management, and tool execution |
| youtube-transcript-api | User Python package 1.2.4; this video's 393 caption segments retrieved successfully | Available YouTube captions without a paid transcript API |
| Requests | User Python package 2.34.2 | HTTP requests from scripts |
| SQLite library | User Python sqlite3 uses SQLite 3.49.1 | Local SQL databases; standalone shell is a separate candidate |
| pandas | Codex bundled 3.0.1 | Dataframes |
| NumPy | Codex bundled 2.3.5 | Numerical arrays |
| lxml | Codex bundled 6.1.1 | XML/HTML parsing |
| Pillow | Codex bundled 12.3.0 | Image processing |
| pypdf | Codex bundled 6.10.0 | PDF manipulation |
| pdfplumber | Codex bundled 0.11.9 | PDF text/tables |
| python-docx | Codex bundled 1.2.0 | Word documents |
| python-pptx | Codex bundled 1.0.2 | PowerPoint documents |
| openpyxl | Codex bundled 3.1.5 | Excel reading/editing |
| XlsxWriter | Codex bundled 3.2.9 | Excel generation |
| Poppler pdfinfo / pdftoppm | Codex bundled binaries | PDF metadata and page rendering; pdftotext not detected |
| Superwhisper | Installed 1.6.5 | Existing dictation/transcription workflow; no new subscription proposed |
| Power Automate Desktop | Installed 1.0.2141 | Local attended flows; premium/unattended features excluded |
| Windows Task Scheduler | Windows component | Scheduled local jobs |
| Chrome / Codex browser controls | Existing browser access used in this session | Inspect sites and video frames through supported controls |

Also detected: Antigravity, Obsidian, Google Drive and Microsoft Office. This catalog does not recommend repurchasing them. Existing Office does not make LibreOffice's headless conversion workflow identical, so LibreOffice remains a candidate.

### Bundled access differs from a normal IDE installation

Codex bundle version: `26.1007.11041`.

```text
User Python:
C:\Users\Joshu\AppData\Local\Programs\Python\Python312\python.exe

Codex bundle root:
C:\Program Files\WindowsApps\OpenAI.CodexPrimaryRuntime.v26-1007-641-0_26.1007.641.0_x64__3k8sg7r9htsxt\dependencies

Bundled Python: <bundle root>\python\python.exe
Bundled Node: <bundle root>\node\bin\node.exe
Bundled pnpm: <bundle root>\bin\fallback\pnpm.cmd
Bundled Poppler: <bundle root>\native\poppler\Library\bin
```

An IDE can use the user interpreter or an isolated project environment. If a bundle-only library is needed in another interpreter, that is an environment-specific requirement, not proof it was absent from this computer. Do not copy dependencies into the Obsidian vault or modify Codex's managed bundle. Bundle paths may change after application updates.

## Languages, compilers and runtimes to retain as candidates

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| TypeScript | Type checking for JavaScript applications | Local compiler; may already be a project dependency, not separately verified |
| Bash | POSIX scripts and Linux tooling | Check Git Bash before adding a separate shell; existing Git may supply it |
| Go | Standalone compiled utilities/services | Local SDK |
| Rust | Efficient native programs and CLIs | Local rustup/cargo toolchain |
| .NET SDK / C# | Windows and cross-platform apps/services | Local SDK |
| Java / OpenJDK | JVM applications | Use a free OpenJDK distribution, not a paid-support product |
| Kotlin | Android/JVM applications | Local compiler/tooling |
| R | Statistical analysis | Local runtime |
| Julia | Numerical/scientific computation | Local runtime |
| Ruby | Ruby applications and scripting | Local runtime |
| PHP | PHP websites and scripts | Local runtime |
| Lua | Lightweight embedded scripting | Local runtime |
| GCC | C/C++ compilation | Free compiler; Windows toolchain setup varies |
| Clang | C/C++ tooling and analysis | Free compiler; not identical to GCC |
| MSVC Build Tools | Native Windows C/C++ compatibility | Free build tools under applicable Microsoft terms; not paid Visual Studio editions |

## Package managers and development workspaces

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| pipx | Isolated Python CLI apps | Avoids polluting normal Python environments |
| Yarn | Projects requiring Yarn conventions/lockfiles | Retain as compatibility option; npm/pnpm already available |
| Bun | Alternate JavaScript runtime/build/test workflow | Local runtime, not just another package installer |
| Conda / Miniforge | Scientific/binary Python environments | Prefer Miniforge + conda-forge; do not assume Anaconda repository access is free for every business |
| Chocolatey Community | Windows packages unavailable or awkward elsewhere | Free community client; paid business features excluded |
| Scoop | User-level portable CLI management | Different install model from winget |
| VS Code | Editor/debugging/extensions | Free editor; paid Copilot/API features excluded |
| JupyterLab | Interactive notebooks | Local server; no paid hosting required |

## Video, audio and transcription

| Tool | Distinct use | Why retained despite existing tools |
|---|---|---|
| faster-whisper | Scripted local batch transcription | Retain for bulk files/model control or measured quality benefit, not a second dictation app |
| whisper.cpp | Native local transcription/CLI deployment | Different runtime and hardware integration from Python transcription |
| WhisperX | Alignment and speaker-related workflows | Retain for capabilities not established in Superwhisper; some model assets require separate access/terms |
| Audacity | Edit/inspect waveforms | Editing is different from dictation |
| OBS Studio | Record screens and demonstrations | Different from transcription |
| VLC | Media playback and format inspection | Retain for broad format handling; routine playback already has Windows alternatives |
| MediaInfo | Detailed format/codec reports | Convenient structured inspection, not transcription |
| SoX | Audio processing CLI | Alternative signal/audio workflow |
| Demucs | Audio source separation | Separate vocals/instruments before analysis |
| Subtitle Edit | Subtitle correction and timing | Editing and review, not merely another transcription engine |

Use local models for the transcription candidates. Do not configure paid Whisper/model APIs. Superwhisper's [Windows features](https://superwhisper.com/windows) and [CLI](https://superwhisper.com/cli) should be evaluated first for the specific task before adding an overlapping pipeline. A transcription tool is not assumed more accurate until tested on representative material.

## Documents, PDF, OCR and ebooks

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| Pandoc | Document-format conversion | Local; PDF output needs an appropriate rendering engine |
| LibreOffice | Office formats and headless conversions | Local free application; Office is already installed for ordinary editing |
| Tesseract | OCR for images/scanned pages | Local OCR, no per-page API charge |
| OCRmyPDF | Add searchable text to scanned PDFs | Complements Tesseract/PDF tools |
| Poppler pdftotext / additional utilities | Extract PDF text and other operations | Add only missing utilities; pdfinfo/pdftoppm already bundled |
| PyMuPDF | PDF rendering, extraction and manipulation | Local library; observe AGPL/commercial licensing distinction if embedding/distributing |
| Calibre | Ebook conversion/management | Local app |
| EbookLib | Scripted EPUB reading/writing | Local library |
| qpdf | PDF structure, encryption and repair operations | Local utility |
| Ghostscript | PostScript/PDF interpretation | Free AGPL edition for compliant use; commercial distribution integration may require another license |
| LaTeX / MiKTeX | Mathematical/publication documents | Free local typesetting; Codex already has a separate built-in standalone LaTeX compiler |
| Typst | Alternative document/typesetting workflow | Local open-source CLI; paid hosted workspace excluded |

Existing PDF, Word, PowerPoint and Excel libraries are listed above, not repeated as downloads.

## Web extraction, HTTP and development testing

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| HTTPie | Human-friendly API requests | Local CLI; paid hosted features excluded |
| HTTPX | Async and sync Python HTTP client | Different concurrency model from installed Requests |
| Beautiful Soup | Convenient HTML parsing | Local extraction; lxml already available as a separate parser |
| Scrapy | Structured crawling framework | Local orchestration, no paid scraping proxy required by this list |
| Trafilatura | Article text extraction | Reduces navigation/boilerplate |
| Playwright | Dedicated application tests and browser workflows | Local library; use existing supported browser controls for the current user browser |
| Selenium | WebDriver compatibility/testing | Retain for projects using that ecosystem |
| Puppeteer | JS-centric browser workflows | Retain for browser/CDP projects requiring it |
| Postman | API inspection and testing | Free features only; paid collaboration/AI features excluded |
| Bruno | File-based local API collections | Free/open-source edition |
| mitmproxy | Inspect development traffic | Local tool; no certificate/security changes implied by cataloging it |
| Chrome DevTools | Browser debugging | Already supplied by Chrome; no separate download needed |

Firecrawl and curl are already available. Firecrawl is not categorized as unlimited free scraping; it consumes the existing account's credits.

## Data analysis, databases and spreadsheet processing

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| SQLite CLI | Shell-based SQL queries | Python SQLite already exists; shell is a distinct interface |
| DuckDB | Analytical SQL over files | Local database, no hosted service |
| PostgreSQL | Multi-user relational database | Local server; hosted providers excluded |
| DBeaver Community | Visual database inspection | Community edition, not paid enterprise editions |
| DB Browser for SQLite | Focused SQLite visual editor | Different from shell/library use |
| Polars | Alternative efficient dataframe engine | Not identical to pandas |
| SciPy | Scientific algorithms | Complements NumPy |
| PyArrow | Arrow/Parquet and columnar interoperability | Local library |
| jq | Dedicated JSON filtering CLI | Python/PowerShell overlap, but portable CLI recipes are distinct |
| yq | YAML processing CLI | Specify implementation when installing; several tools share this name |
| csvkit | CSV-focused CLI suite | Complements dataframe libraries |
| Datasette | Local browser exploration of SQLite | No hosted deployment required |
| Redis | Local cache/message/data server | Use free local edition with selected license; Redis Cloud/paid features excluded |
| SQLAlchemy | Python database abstraction | Local library |
| Alembic | Schema migrations | Complements SQLAlchemy |

pandas, NumPy and Excel libraries already available in Codex are excluded from the new-download queue.

## Search, archives, comparisons and backup utilities

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| fd | Fast filename discovery | Different from ripgrep text search |
| Everything | Indexed Windows filename search | Local application |
| fzf | Interactive fuzzy selection | Complements search tools |
| WinMerge | Visual file/folder comparison | Free application |
| Meld | Cross-platform visual comparisons | Alternative workflow, not required alongside WinMerge |
| delta | Git diff presentation | Complements existing Git |
| bat | Highlighted source-file viewing | CLI display utility |
| tree | Folder display | Windows tree.exe is supplied by OS; check it before considering any separate variant |
| ExifTool | File metadata inspection/editing | Distinct from image editing |
| rclone | Multi-provider transfers and checks | Client free; existing provider limits/costs still apply; no replacement sync job implied |
| restic | Encrypted/versioned backups | Local/free storage target; paid storage optional and excluded |
| Syncthing | Device-to-device file synchronization | Different from existing snapshot backups; do not layer sync onto active vault without design |
| BLAKE3 utilities | High-speed content hashing | Alternative hashing algorithm; existing SHA-256 remains provenance standard |

7-Zip, ripgrep and Git are already available. Beyond Compare is excluded from free candidates below.

## Graphics, images, diagrams and plots

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| ImageMagick | Batch image CLI operations | Different from available Pillow library |
| OpenCV | Computer vision/image analysis | Local library |
| GIMP | Raster image editing | Free application |
| Inkscape | Vector/SVG editing | Free application |
| Blender | 3D scenes/rendering | Local app; paid assets/render farms excluded |
| Graphviz | Graph layouts from text | Local utility |
| Mermaid CLI | Render Mermaid diagrams to artifacts | Complements existing inline Mermaid support |
| PlantUML | Architecture/sequence diagrams | Local rendering |
| Matplotlib | Scientific plotting | Local Python library |
| Plotly | Interactive charts | Local open-source library; paid hosting excluded |
| Seaborn | Statistical plotting | Complements Matplotlib |
| Manim | Programmatic mathematical animation | Local rendering |
| Sharp | Node.js image processing | Different language/runtime integration from Pillow |
| pngquant | PNG compression | Specialized compression |
| SVGO | SVG optimization | Different from vector editing |

## Code quality, testing and debugging

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| pytest | Python tests | Local runner |
| Ruff | Python lint/format | Local checks |
| mypy | Python type analysis | Retain for project compatibility |
| Pyright | Alternate Python type analysis | Different engine/ecosystem |
| ESLint | JS/TS lint rules | May already be a project dependency; verify there before adding |
| Prettier | Formatting | May already be project-local |
| Biome | Combined JS lint/format | Alternative, do not silently replace project conventions |
| Vitest | Vite-oriented JS/TS tests | Retain for project fit |
| Jest | JS tests | Retain for projects already using Jest |
| coverage.py | Python coverage measurement | Complements test runner |
| pre-commit | Repository checks | Local automation |
| ShellCheck | Shell script analysis | Local checks |
| PSScriptAnalyzer | PowerShell analysis | Local checks |
| Gitleaks | Detect accidentally exposed secrets | May already exist in sync toolchain; executable availability not established by this inventory |
| Semgrep | Static analysis | Free local engine/rules; paid platform excluded |
| Trivy | Dependency/container/config scans | Local scans; external registry limits can apply |
| k6 | Load tests | Local open-source runner; hosted load testing excluded |
| Hyperfine | Benchmark commands | Local utility |

## Build systems and local infrastructure

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| WSL | Linux environment on Windows | wsl.exe exists; installed distro/feature readiness not verified; no automatic feature changes |
| Docker Desktop | Container development | Conditional free eligibility, not universally free; see cost ledger |
| Docker Engine | Containers in Linux/WSL | Free engine alternative; Linux environment required |
| Dev Containers | Repeatable development environments | Extension/spec free; chosen container environment must fit free scope |
| CMake | Native build configuration | Local tool |
| Ninja | Native build execution | Complements CMake |
| Make | Build recipes | Different ecosystem compatibility |
| Task | YAML-defined command recipes | Local tool |
| just | Lightweight command recipes | Retained for project compatibility |
| OpenSSH | Remote terminals/file transfer | Check Windows optional component before another installation |
| Terraform | Infrastructure-as-code client | Local evaluation free under applicable license; resource provisioning not free by implication |
| OpenTofu | Open-source infrastructure-as-code client | Retained as distinct licensing/ecosystem choice; resources can cost |
| Ansible | Host configuration automation | Free tool; managed services optional |
| kubectl | Kubernetes client | Free client; use only a verified free/local target |
| Helm | Kubernetes packages | Free client; selected cluster/resources may cost |

## Deployment/provider CLIs: not an unrestricted no-cost queue

These names from the original list are retained for completeness. The clients can be free while the resources, deployments, API calls or subscription features are chargeable. Install only for a specific existing project and verified no-extra-cost route; do not provision anything from this catalog.

| Tool | Potential use | Cost boundary |
|---|---|---|
| Google Cloud CLI | Existing GCP services | Workspace/Google AI Pro does not establish free arbitrary GCP usage |
| AWS CLI | AWS services | Resources/API operations can be billed |
| Azure CLI | Azure services | Resources/API operations can be billed |
| Supabase CLI | Local development or eligible project operations | Local tools free; hosted limits/billing and current Lovable deployment rules still govern |
| Vercel CLI | Project preview/deployment | Verify business use eligibility and plan; no blanket free-hosting assumption |
| Netlify CLI | Local development/deployment | Hosted credits/limits can apply |

## Local AI, retrieval and machine learning

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| Ollama | Local model execution | Local only; optional cloud models excluded |
| llama.cpp | Native local inference | Different embedding/deployment capabilities |
| LM Studio | Local model desktop interface | Free local app; optional Bionic/cloud inference excluded |
| Hugging Face CLI | Model/artifact retrieval | Public/free assets with compatible licenses; paid endpoints/private features excluded |
| PyTorch | ML/model execution | Local CPU/GPU library |
| scikit-learn | Traditional ML | Local library |
| Transformers | Pretrained model tooling | Model licenses separate; no paid endpoint required |
| sentence-transformers | Local embeddings | Download suitable licensed model, no embedding API required |
| FAISS | Similarity indexes | Local library; Windows packaging may vary |
| Qdrant | Vector search | Local open-source server; managed cloud excluded |
| Chroma | Local embedding retrieval | Local edition; cloud excluded |
| LanceDB | Local vector/structured retrieval | Open-source/local edition |
| ONNX Runtime | Execute ONNX models | Local runtime |
| MLflow | Track experiments | Local server; hosted platform excluded |
| Optuna | Parameter optimization | Local library |
| qmd | Markdown retrieval | Local retrieval; model setup may be required; keep existing index/rg unless useful retrieval benefit demonstrated |
| NetworkX | Relationship/graph analysis | Local library |

No candidate includes rented GPUs, paid inference or paid transcription. Free-to-run software does not automatically grant rights to every model or dataset. RAM/GPU capacity affects feasible local workloads even when storage is plentiful.

## Workflow automation and existing Google entitlements

| Tool | Distinct use | Free-use scope / note |
|---|---|---|
| Google Apps Script | Automate existing Workspace services | No local download; account quotas apply; separately billed integrations excluded |
| n8n Community | Self-hosted integrations | Free internal workflows under Sustainable Use License; Cloud/paid features excluded |
| Node-RED | Local event/integration flows | Local runtime |
| AutoHotkey | Windows shortcuts/desktop scripting | Local runtime; no changes to existing shortcuts implied |
| APScheduler | Python job scheduling | Different from OS scheduler when app-managed jobs are needed |
| Prefect | Observable workflow execution | Self-hosted open-source engine; Cloud excluded |
| Dagster | Data workflows | Local/open-source edition; managed cloud excluded |
| Temporal | Durable workflows | Self-hosted server/CLI; Temporal Cloud excluded |
| ntfy | Notifications | Self-hosted server for assured local free scope; external push integrations may have limits |
| Apprise | Notification integrations | Local library free; chosen provider can have fees |

Google Workspace CLI, Power Automate Desktop and Task Scheduler are already present. Existing Gemini/Antigravity/Google AI Pro access may be useful within verified plan limits. Do not assume it provides unlimited API calls or automatically covers cloud charges.

## Removed or constrained, with reasons

| Original item / overlapping need | Disposition | Reason |
|---|---|---|
| Beyond Compare | Removed from free candidates | Trial is not free permanent use; paid license required. WinMerge/Meld retained |
| Already verified runtimes, CLIs and bundled libraries | Removed from download queue, preserved in availability ledger | Already usable; avoid unnecessary duplicate installs |
| Another ordinary live dictation application | Not added | Existing Superwhisper supplies that workflow; batch/alignment tools retained only for different capabilities |
| Anaconda default distribution/repositories | Prefer Miniforge + conda-forge | Repository licensing can depend on organization/use; do not promise universal free access |
| Docker Desktop | Conditional candidate | Free for qualifying small business/personal/educational use; eligibility not independently adjudicated here |
| Cloud transcription/model API services | Excluded from no-cost candidates | Metered calls can cost; use local inference/captions or verified existing entitlements |
| Cloud versions of local tools | Excluded from default selection | n8n Cloud, Prefect Cloud, Temporal Cloud, paid Redis, hosted vector databases and hosted inference are separate products |
| Power Automate premium/unattended features | Excluded | Existing attended local use does not establish premium licensing |
| Provider/deployment CLIs | Separate conditional section | Free executable is not a free backend; no provisioning authorization |
| Ghostscript/PyMuPDF | Retained for local compliant use | Free copyleft editions exist; embedding in a distributed product needs license review |

Related tools are deliberately retained where interfaces, outputs, compatibility or workflows differ. An alternative is not recommended for simultaneous installation merely because it appears here.

## Useful first additions, when you choose to install

1. uv + pipx: isolated, maintainable Python tooling.
2. Pandoc + Tesseract + OCRmyPDF: document conversion and scanned-text intake.
3. jq + missing Poppler text utilities + SQLite CLI: convenient extraction/data inspection.
4. DuckDB + ExifTool + ImageMagick: analytical files, metadata and batch images.

These are preferences for future selection, not installs completed in this task.

## Verification and authoritative cost references

Inventory used executable discovery, winget registration, Python package metadata in user and Codex interpreters, and the actual bundled dependency paths. On 2026-10-08, WinGet reported yt-dlp 2026.08.19, FFmpeg N-126374-g089a48eb36-20260831 and Deno 2.9.7. The user PATH already contained all three package directories. Codex's inherited process PATH was stale; refreshing this shell from saved user and machine PATH made yt-dlp, ffmpeg, ffprobe, ffplay and deno resolve by command name and return their expected versions. A yt-dlp diagnostic recognizes ffmpeg, ffprobe and Deno. Restart Codex to refresh the environment for future app processes if command lookup remains stale. Project-local virtual environments and npm dependency trees were not exhaustively searched. An installed executable is not proof that an account, model or backend is configured. The caption package was live-tested on the build video; other candidates were not execution-tested.

- [yt-dlp installation](https://github.com/yt-dlp/yt-dlp/wiki/Installation)
- [FFmpeg official download links](https://ffmpeg.org/download.html)
- [uv installation](https://docs.astral.sh/uv/getting-started/installation/)
- [Pandoc installation](https://pandoc.org/installing.html)
- [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/)
- [Beyond Compare licensing](https://www.scootersoftware.com/shop.php?zz=shop_promo)
- [Docker Desktop eligibility](https://docs.docker.com/subscription-billing/desktop-license/): small business requires fewer than 250 employees AND under US$10 million annual revenue.
- [n8n license scope](https://support.n8n.io/article/can-i-use-your-license-for-my-use-case)
- [Power Automate licensing](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/types)
- [Prefect open source](https://www.prefect.io/prefect/open-source)
- [Temporal self-hosting](https://docs.temporal.io/self-hosted-guide)
- [Redis licenses](https://redis.io/legal/licenses/)
- [LM Studio free local workplace use](https://lmstudio.ai/blog/free-for-work)
- [VS Code licensing FAQ](https://code.visualstudio.com/docs/supporting/faq)
- [Anaconda licensing and Miniforge distinction](https://www.anaconda.com/legal)
- [Ghostscript licensing](https://ghostscript.com/faq/)
- [Apps Script quotas](https://developers.google.com/apps-script/guides/services/quotas)
- [Gemini API billing](https://ai.google.dev/gemini-api/docs/billing/)
- [Google AI Studio subscription features](https://blog.google/innovation-and-ai/technology/developers-tools/google-one-ai-studio/)
- [Google AI credit limits and purchases](https://support.google.com/googleone/answer/17103110)

Future installation brief for another IDE:

```text
Use this catalog as a candidate list, not a blanket install command.
Verify the exact target environment and existing executables/packages first.
Skip already available tools. Use official free local editions and isolated environments.
Do not alter the AI OS vault, its instructions, active skills or managed Codex bundle.
Do not configure paid APIs, enable overage billing, purchase licenses, provision cloud
resources or install duplicate dictation software. Report costs/conditions before any
dependent step. Verify selected tools with versions and a relevant small functional check.
```
