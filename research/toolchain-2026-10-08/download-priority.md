# Tools to download, in priority order

Prepared 2026-10-08. Start at the top and work downward. This is a generous list for Windows, Claude Code, Codex, automation, research, documents, images and media. Only new candidates appear here. Gaming, emulators and game-streaming tools are excluded. Nothing has been installed by this task.

Installed applications, PATH executables and the user/Codex Python inventories were checked. These entries were not detected in those checks, rather than proven absent from every project environment or portable folder. Before installing a library, the IDE should check its target environment once more and skip any existing copy. Libraries belong in an isolated environment outside the Obsidian vault.

Use the linked official free/local edition. No subscription, paid API, cloud inference or paid hosting is needed for the uses below. Local AI still needs suitable hardware and compatible model licenses. Priority reflects likely usefulness to Joshua, not storage size. Later entries are useful reserves; they do not all need to run in the background.

## Priority 1: the biggest immediate gains

| Order | Download | What it adds |
|---:|---|---|
| 1 | [FFmpeg, including ffprobe](https://ffmpeg.org/download.html) | Convert, trim and inspect audio/video; extract frames and audio for agents |
| 2 | [yt-dlp](https://github.com/yt-dlp/yt-dlp#installation) | Retrieve available media, subtitles and metadata; complements existing caption extraction |
| 3 | [uv](https://docs.astral.sh/uv/getting-started/installation/) | Fast isolated Python environments and script dependencies |
| 4 | [pipx](https://pipx.pypa.io/stable/installation/) | Install Python command-line tools without mixing their dependencies |
| 5 | [PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/) | Window layouts, bulk rename, keyboard remapping, launcher and other Windows utilities |
| 6 | [Everything](https://www.voidtools.com/) | Instant indexed filename search across the laptop |
| 7 | [ShareX](https://getsharex.com/) | Repeatable screen capture, annotation, GIFs and capture workflows beyond Snipping Tool |
| 8 | [Pandoc](https://pandoc.org/installing.html) | Convert Markdown, Word, HTML, EPUB and other document formats |
| 9 | [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html) | Read text from screenshots and scans locally; upstream links to Windows builds |
| 10 | [OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/installation.html) | Turn scanned PDFs into searchable sources; Windows setup commonly uses WSL |
| 11 | [jq](https://jqlang.org/download/) | Inspect and transform JSON returned by APIs and tools |
| 12 | [Poppler text utilities](https://github.com/oschwartz10612/poppler-windows/releases) | Add missing pdftotext for PDF extraction; use only missing utilities, not duplicate bundled renderers |
| 13 | [AutoHotkey](https://www.autohotkey.com/) | Automate repetitive Windows clicks, typing and keyboard workflows |
| 14 | [ImageMagick](https://imagemagick.org/script/download.php#windows) | Batch resize, crop, convert and combine images from scripts |
| 15 | [ExifTool](https://exiftool.org/) | Inspect and organize image, video and document metadata |
| 16 | [WinMerge](https://winmerge.org/) | Compare folders and documents before migrations or merges |
| 17 | [LocalSend](https://localsend.org/) | Transfer files between phone, Windows and Mac on the local network |
| 18 | [OBS Studio](https://obsproject.com/) | Record lessons, demonstrations and screen/audio sources with more control |
| 19 | [VLC](https://www.videolan.org/vlc/) | Broad-format video/audio playback and troubleshooting |
| 20 | [DuckDB](https://duckdb.org/docs/installation/) | Query CSV, JSON and Parquet files locally without setting up a database server |

## Priority 2: better documents, media and everyday Windows use

| Order | Download | What it adds |
|---:|---|---|
| 21 | [SQLite command-line tools](https://www.sqlite.org/download.html) | Inspect local databases directly; distinct from the existing Python SQLite library |
| 22 | [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/) | Free headless document conversion for agents; existing Office covers ordinary editing |
| 23 | [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader) | Lightweight PDF/ebook reading and command-line printing |
| 24 | [PDFsam Basic](https://pdfsam.org/download-pdfsam-basic/) | Merge, split and reorder PDFs locally; choose Basic, skip paid trial products |
| 25 | [qpdf](https://github.com/qpdf/qpdf/releases) | Repair and inspect PDF structure from scripts |
| 26 | [Audacity](https://www.audacityteam.org/download/) | Edit recordings, remove unwanted sections and inspect audio |
| 27 | [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit/releases) | Review transcripts, subtitle timing and caption formats |
| 28 | [LosslessCut](https://github.com/mifi/lossless-cut/releases) | Trim recordings without re-encoding; use free GitHub builds |
| 29 | [HandBrake](https://handbrake.fr/downloads.php) | Easy video conversion and compression presets |
| 30 | [Kdenlive](https://kdenlive.org/download/) | Full local video editing, layered lessons, titles and subtitles |
| 31 | [Shutter Encoder](https://www.shutterencoder.com/) | Batch professional media conversion, subtitle and encoding workflows |
| 32 | [MediaInfo](https://mediaarea.net/en/MediaInfo/Download/Windows) | Explain codecs, formats and recording problems |
| 33 | [File Converter](https://file-converter.io/) | Convert files from the Windows Explorer context menu |
| 34 | [Krita](https://krita.org/en/download/) | Drawing, annotation and illustration beyond basic image editing |
| 35 | [GIMP](https://www.gimp.org/downloads/) | Photo editing, masks, compositing and retouching |
| 36 | [Inkscape](https://inkscape.org/release/) | Vector diagrams, SVG graphics and scalable branding assets |
| 37 | [Upscayl desktop](https://github.com/upscayl/upscayl/releases) | Local AI image enlargement; desktop edition, suitable GPU required |
| 38 | [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases) | Offline workflow, architecture and teaching diagrams |
| 39 | [Calibre](https://calibre-ebook.com/download_windows) | Organize and convert ebooks and research collections |
| 40 | [Notepad++](https://notepad-plus-plus.org/downloads/) | Lightweight large-text, log and structured-file editing |
| 41 | [Ditto](https://ditto-cp.sourceforge.io/) | Searchable clipboard history and reusable snippets; distinct from basic Windows clipboard |
| 42 | [KDE Connect](https://kdeconnect.kde.org/download.html) | Phone/computer integration, clipboard and remote controls; features depend on phone OS |
| 43 | [QuickLook](https://github.com/QL-Win/QuickLook/releases) | Spacebar file previews in Explorer |
| 44 | [EarTrumpet](https://github.com/File-New-Project/EarTrumpet/releases) | Convenient per-application audio controls |
| 45 | [Twinkle Tray](https://twinkletray.com/) | Convenient external-monitor brightness controls on supported monitors |

## Priority 3: give coding agents stronger local capabilities

| Order | Download | What it adds |
|---:|---|---|
| 46 | [Playwright](https://playwright.dev/docs/intro) | Browser tests, screenshots and repeatable app checks |
| 47 | [Bruno open-source edition](https://www.usebruno.com/downloads) | Local API collections that agents can version with code |
| 48 | [HTTPie CLI](https://httpie.io/docs/cli/installation) | Convenient manual API inspection |
| 49 | [HTTPX](https://www.python-httpx.org/) | Parallel asynchronous Python HTTP requests |
| 50 | [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) | Structured HTML extraction |
| 51 | [Trafilatura](https://trafilatura.readthedocs.io/en/latest/installation.html) | Extract article text instead of page navigation and boilerplate |
| 52 | [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) | Maintainable multi-page crawlers and extraction pipelines |
| 53 | [Ruff](https://docs.astral.sh/ruff/installation/) | Fast Python linting and formatting |
| 54 | [pytest](https://docs.pytest.org/en/stable/getting-started.html) | Check that Python automations actually work |
| 55 | [Pyright](https://github.com/microsoft/pyright) | Catch Python type mistakes before execution |
| 56 | [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) | Check PowerShell automation quality |
| 57 | [Gitleaks](https://github.com/gitleaks/gitleaks/releases) | Detect secrets before accidental publication; recheck existing sync tool folder before install |
| 58 | [pre-commit](https://pre-commit.com/) | Run useful repository checks automatically |
| 59 | [fd](https://github.com/sharkdp/fd/releases) | Fast filename discovery from the command line |
| 60 | [fzf](https://github.com/junegunn/fzf#installation) | Interactive fuzzy picking of files, commands and history |
| 61 | [delta](https://github.com/dandavison/delta/releases) | More readable Git differences |
| 62 | [bat](https://github.com/sharkdp/bat/releases) | Syntax-highlighted command-line file viewing |
| 63 | [yq, Mike Farah implementation](https://github.com/mikefarah/yq/releases) | Query and edit YAML configuration |
| 64 | [csvkit](https://csvkit.readthedocs.io/en/latest/) | Inspect and transform CSV files from scripts |
| 65 | [VS Code](https://code.visualstudio.com/Download) | A general editor/debugger for projects needing its extension ecosystem; Antigravity already covers routine editing |
| 66 | [JupyterLab](https://jupyter.org/install) | Interactive Python experiments and extraction notebooks |
| 67 | [Go](https://go.dev/dl/) | Build portable utilities and install useful Go-based CLIs |
| 68 | [Rust via rustup](https://rustup.rs/) | Build/install native tools and efficient utilities |
| 69 | [.NET SDK](https://dotnet.microsoft.com/download) | Build Windows integrations and C# applications; SDK differs from installed runtime components |
| 70 | [MSVC Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio) | Compile Windows native dependencies; free Build Tools, not paid IDE editions |
| 71 | [CMake](https://cmake.org/download/) | Build native AI/media dependencies |
| 72 | [Ninja](https://github.com/ninja-build/ninja/releases) | Fast native build execution |
| 73 | [Bun](https://bun.sh/) | Alternate fast JavaScript runtime and integrated tooling |
| 74 | [Deno](https://docs.deno.com/runtime/getting_started/installation/) | TypeScript scripting and compatibility with some media extraction workflows |
| 75 | [just](https://github.com/casey/just/releases) | Give agents short, repeatable project commands |

## Priority 4: local AI and automation without per-call fees

| Order | Download | What it adds |
|---:|---|---|
| 76 | [Ollama](https://ollama.com/download/windows) | Local language/embedding models; choose local models, not cloud endpoints |
| 77 | [LM Studio](https://lmstudio.ai/download) | Desktop model browsing/testing and local serving; free local features |
| 78 | [llama.cpp](https://github.com/ggml-org/llama.cpp/releases) | Native local inference and embedding utilities |
| 79 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Programmable bulk-file transcription; adds automation beyond current dictation |
| 80 | [WhisperX](https://github.com/m-bain/whisperX) | Word alignment and optional speaker separation; some model access needs registration |
| 81 | [whisper.cpp](https://github.com/ggml-org/whisper.cpp/releases) | Native offline transcription in a different runtime |
| 82 | [PyTorch](https://pytorch.org/get-started/locally/) | Run local transcription, vision and generation models |
| 83 | [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) | Download suitable free model assets |
| 84 | [Transformers](https://huggingface.co/docs/transformers/installation) | Work with local pretrained models |
| 85 | [sentence-transformers](https://www.sbert.net/docs/installation.html) | Create local text embeddings for retrieval |
| 86 | [ONNX Runtime](https://onnxruntime.ai/docs/install/) | Efficient local model execution |
| 87 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Local image-generation and image-processing workflows; use compatible free model assets |
| 88 | [rembg](https://github.com/danielgatis/rembg) | Remove image backgrounds locally |
| 89 | [OpenCV](https://pypi.org/project/opencv-python/) | Analyze screenshots, frames and images programmatically |
| 90 | [Node-RED](https://nodered.org/docs/getting-started/local) | Local visual automation and event-driven integrations |
| 91 | [n8n Community, self-hosted](https://docs.n8n.io/hosting/) | Visual integrations under free internal-use license; not n8n Cloud |
| 92 | [APScheduler](https://apscheduler.readthedocs.io/en/master/userguide.html) | Schedule jobs inside Python applications |
| 93 | [Prefect open-source engine](https://docs.prefect.io/) | Track, retry and inspect multi-step automations locally |
| 94 | [ntfy, self-hosted](https://docs.ntfy.sh/install/) | Agent/job notifications; server needs Linux/container setup |
| 95 | [Apprise](https://github.com/caronc/apprise) | Deliver notifications through existing free/covered destinations |
| 96 | [Chroma local](https://docs.trychroma.com/) | Local semantic retrieval for document collections |
| 97 | [LanceDB open-source](https://lancedb.com/documentation/) | Local vector and structured retrieval |
| 98 | [Qdrant local](https://qdrant.tech/documentation/quickstart/) | Vector database for more developed retrieval workflows; Docker/WSL needed for typical local server setup |
| 99 | [qmd](https://github.com/tobi/qmd) | Markdown retrieval experiments; verify current Windows/WSL support and model setup |
| 100 | [NetworkX](https://networkx.org/documentation/stable/install.html) | Analyze relationships and graph imports without changing canonical notes |

## Priority 5: protect, inspect and manage the laptop and its files

| Order | Download | What it adds |
|---:|---|---|
| 101 | [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer) | See which processes hold files or consume resources |
| 102 | [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon) | Diagnose file, registry and application failures |
| 103 | [Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns) | Inspect startup programs and unwanted background tasks |
| 104 | [TCPView](https://learn.microsoft.com/en-us/sysinternals/downloads/tcpview) | Inspect application network connections |
| 105 | [Libre Hardware Monitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases) | Inspect temperatures, fans and hardware sensors locally |
| 106 | [WinDirStat](https://windirstat.net/) | Visualize folder sizes and unexpected growth, even when capacity is plentiful |
| 107 | [rclone](https://rclone.org/downloads/) | Check and transfer files with existing Drive/storage accounts |
| 108 | [restic](https://restic.readthedocs.io/en/stable/020_installation.html) | Encrypted, versioned backups to existing storage |
| 109 | [Syncthing](https://syncthing.net/downloads/) | Direct device-to-device sync for a deliberately chosen folder |
| 110 | [FreeFileSync standard edition](https://freefilesync.org/download.php) | Review folder differences and mirror selected collections; no second live-vault sync without design |
| 111 | [WinSCP](https://winscp.net/eng/download.php) | Visual SFTP/SCP transfers to servers |
| 112 | [Meld](https://meldmerge.org/) | Alternate visual three-way merge workflow |
| 113 | [BLAKE3 b3sum](https://github.com/BLAKE3-team/BLAKE3/releases) | Fast content comparison; keep existing SHA-256 provenance conventions |
| 114 | [Ant Renamer](https://www.antp.be/software/renamer/download) | Advanced free filename transformations beyond basic bulk rename |
| 115 | [dupeGuru](https://dupeguru.voltaicideas.net/) | Review duplicate files before deciding what to keep |
| 116 | [VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) | Optional encrypted containers for separate archives; do not replace current credential model |
| 117 | [Cryptomator](https://cryptomator.org/downloads/) | Free desktop encrypted cloud folders; mobile app may cost and is not included |
| 118 | [Rufus](https://rufus.ie/) | Create bootable recovery/install USB drives |
| 119 | [Ventoy](https://www.ventoy.net/en/download.html) | Keep multiple bootable recovery images on one USB drive |
| 120 | [TestDisk and PhotoRec](https://www.cgsecurity.org/wiki/TestDisk_Download) | File/partition recovery tools for emergencies |

## Priority 6: creative projects, richer outputs and useful technical reserves

| Order | Download | What it adds |
|---:|---|---|
| 121 | [Blender](https://www.blender.org/download/) | 3D visuals, animation and scene rendering |
| 122 | [Graphviz](https://graphviz.org/download/) | Automatically lay out graphs and dependency diagrams |
| 123 | [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) | Export diagrams as image/PDF artifacts |
| 124 | [PlantUML](https://plantuml.com/download) | Sequence and system diagrams; requires compatible Java runtime |
| 125 | [Typst CLI](https://github.com/typst/typst/releases) | Local polished reports and mathematical documents |
| 126 | [MiKTeX](https://miktex.org/download) | Multi-file local LaTeX builds beyond Codex's built-in standalone compiler |
| 127 | [Matplotlib](https://matplotlib.org/stable/install/index.html) | Produce publication-style plots from extracted data |
| 128 | [Plotly local library](https://plotly.com/python/getting-started/) | Interactive charts without paid hosting |
| 129 | [Manim](https://docs.manim.community/en/stable/installation.html) | Animate teaching explanations and reasoning diagrams |
| 130 | [Sharp](https://sharp.pixelplumbing.com/install/) | Image processing inside JavaScript applications |
| 131 | [pngquant](https://pngquant.org/) | Optimize PNG images |
| 132 | [SVGO](https://github.com/svg/svgo) | Optimize SVG assets |
| 133 | [EbookLib](https://pypi.org/project/EbookLib/) | Extract and generate EPUB content from scripts |
| 134 | [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/installation.html) | Alternate fast PDF extraction/rendering; free copyleft use, distributed embedding needs license review |
| 135 | [Ghostscript](https://ghostscript.com/releases/gsdnld.html) | PDF/PostScript transformations; free AGPL edition for compliant local use |
| 136 | [Polars](https://docs.pola.rs/user-guide/installation/) | Process large tables efficiently; distinct from existing pandas |
| 137 | [PyArrow](https://arrow.apache.org/docs/python/install.html) | Work with Parquet/Arrow datasets |
| 138 | [Datasette](https://docs.datasette.io/en/stable/installation.html) | Browse extracted SQLite collections through a local website |
| 139 | [DBeaver Community](https://dbeaver.io/download/) | Visual inspection of multiple database types |
| 140 | [DB Browser for SQLite](https://sqlitebrowser.org/dl/) | Focused local database editing |
| 141 | [PostgreSQL](https://www.postgresql.org/download/windows/) | Local database for apps outgrowing flat files |
| 142 | [SQLAlchemy](https://www.sqlalchemy.org/download.html) | Reliable Python database access |
| 143 | [Alembic](https://alembic.sqlalchemy.org/en/latest/front.html) | Version database schema changes |
| 144 | [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/) | Compatibility with projects using WebDriver |
| 145 | [Puppeteer](https://pptr.dev/guides/installation) | JavaScript browser/CDP workflows |
| 146 | [mitmproxy](https://mitmproxy.org/) | Inspect traffic when debugging an integration |
| 147 | [Semgrep Community engine](https://semgrep.dev/docs/getting-started/) | Local static code scans; Windows typically through WSL/container |
| 148 | [Trivy](https://trivy.dev/latest/getting-started/installation/) | Scan dependencies, containers and configuration; check supported execution environment |
| 149 | [k6](https://grafana.com/docs/k6/latest/set-up/install-k6/) | Local performance/load checks |
| 150 | [Hyperfine](https://github.com/sharkdp/hyperfine/releases) | Measure which script or tool actually runs faster |
| 151 | [coverage.py](https://coverage.readthedocs.io/) | Measure Python test coverage |
| 152 | [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) | Alternate type checker for projects that require it |
| 153 | [ShellCheck](https://github.com/koalaman/shellcheck#installing) | Catch errors in Bash scripts |
| 154 | [Task](https://taskfile.dev/installation/) | YAML-based reusable automation recipes |
| 155 | [Miniforge](https://github.com/conda-forge/miniforge/releases) | Install difficult binary Python dependencies through conda-forge |
| 156 | [LLVM/Clang](https://github.com/llvm/llvm-project/releases) | Compile native tools and analyze C/C++ dependencies |
| 157 | [MSYS2](https://www.msys2.org/) | Windows packages for GCC, Make and POSIX-oriented build tools |
| 158 | [OpenJDK via Eclipse Temurin](https://adoptium.net/temurin/releases/) | Run Java-based diagram/document tools |
| 159 | [Scoop](https://scoop.sh/) | User-level portable CLI installs for gaps in the existing package manager |
| 160 | [Chocolatey Community](https://chocolatey.org/install) | Alternate Windows package coverage; free community features |

## Priority 7: leisure, learning, personal collections and a nicer PC

These are worthwhile possibilities beyond work. The order within this group starts with broadly useful personal tools and ends with optional hobbies. Keep the distinctions, rather than installing several alternatives for exactly the same routine task.

| Order | Download | What it adds |
|---:|---|---|
| 161 | [MusicBee](https://getmusicbee.com/) | Organize local music, playlists, tags and playback |
| 162 | [foobar2000](https://www.foobar2000.org/download) | Customizable audio playback, format handling and conversion |
| 163 | [Jellyfin](https://jellyfin.org/downloads/) | Serve your own movies, music and recordings to devices without a server subscription |
| 164 | [Kodi](https://kodi.tv/download/) | A couch-friendly local media-center interface |
| 165 | [mpv.net](https://github.com/mpvnet-player/mpvnet/releases) | Scriptable Windows video player for keyboard-heavy and automated workflows |
| 166 | [Zotero](https://www.zotero.org/download/) | Organize research papers, reading and citations; use local storage or existing WebDAV, not paid storage upgrades |
| 167 | [Anki desktop](https://apps.ankiweb.net/) | Spaced-repetition learning for languages, hobbies or facts; desktop free, some mobile apps cost |
| 168 | [Thorium Reader](https://www.edrlab.org/software/thorium-reader/) | Accessible EPUB reading, audiobooks and reading navigation |
| 169 | [digiKam](https://www.digikam.org/download/) | Organize large personal photo collections with tags and local analysis |
| 170 | [darktable](https://www.darktable.org/install/) | Non-destructive RAW photo development |
| 171 | [RawTherapee](https://rawtherapee.com/downloads/) | Alternate detailed RAW conversion with different controls |
| 172 | [Paint.NET](https://www.getpaint.net/download.html) | Quick layered image editing; official website edition is free, Store edition may cost |
| 173 | [Scribus](https://www.scribus.net/downloads/) | Design print layouts, booklets, posters and personal projects |
| 174 | [Freeplane](https://docs.freeplane.org/) | Visual mind maps for trips, life planning and brainstorming; Java required |
| 175 | [ActivityWatch](https://activitywatch.net/downloads/) | Local time-use tracking to understand where laptop time goes |
| 176 | [NVDA](https://www.nvaccess.org/download/) | Free screen reader for accessibility and checking how interfaces sound |
| 177 | [Deskflow](https://github.com/deskflow/deskflow/releases) | Share a keyboard and mouse between nearby computers; check current platform permissions |
| 178 | [CrystalDiskInfo](https://crystalmark.info/en/software/crystaldiskinfo/) | Inspect drive health and temperature |
| 179 | [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/) | Measure drive performance instead of guessing |
| 180 | [Stellarium desktop](https://stellarium.org/) | Explore the sky, planets and constellations; free Windows planetarium |
| 181 | [Marble](https://marble.kde.org/) | Virtual globe, maps and geography exploration; offline maps depend on downloaded data |
| 182 | [Kiwix](https://kiwix.org/en/applications/) | Read offline encyclopedias and other freely available knowledge collections |
| 183 | [Sweet Home 3D desktop](https://www.sweethome3d.com/download.jsp) | Plan rooms, furniture and a home office; use free upstream desktop distribution |
| 184 | [Pencil2D](https://www.pencil2d.org/download/) | Simple hand-drawn animation |
| 185 | [OpenToonz](https://opentoonz.github.io/e/) | More elaborate 2D animation workflows |
| 186 | [LMMS](https://lmms.io/download) | Create music, beats and sound projects locally |
| 187 | [MuseScore Studio](https://musescore.org/en/download) | Write and play musical notation; not a paid score-library subscription |
| 188 | [OpenMPT](https://openmpt.org/download) | Tracker-style music and sample-based composition |
| 189 | [Tenacity](https://tenacityaudio.org/) | Alternate open-source audio editor for projects needing its workflow |

## What the IDE must verify before installing project dependencies

TypeScript, ESLint, Prettier, Vitest, Jest, Biome and Yarn were not exhaustively checked across application repositories. They are deliberately not presented as missing downloads. Check each project's manifest and lockfile first; add only a missing dependency that fits that project's conventions. The same applies if any library above is already in a project environment.

WSL is an existing Windows command, so it is not a new download entry. If a listed tool needs Linux, inspect WSL's installed distribution and feature status before setting it up. Docker Desktop is omitted from the unconditional free queue because business eligibility is conditional; Docker Engine in an appropriate Linux environment is a possible later dependency.

R and unrelated specialist language stacks were removed. Paid products, extra dictation apps, cloud provisioning CLIs, paid model services and installed/bundled tools were removed from this download queue. Google Apps Script needs no download. Ordinary office/browser replacements were avoided unless the candidate adds a distinct automation or media capability.

## Install safely without buying anything

```text
Work through this file in ascending order. Check the actual target environment first
and skip any item already present. Use official free local editions, not trials or
paid hosted variants. Install app tools outside the Obsidian vault and Python libraries
in an isolated environment. Check Windows/WSL requirements before installation.
Do not change active vault sync, existing skills, instructions or credential storage.
Do not enable cloud inference, paid APIs, paid features or automatic overage billing.
Do not download bundled dependencies separately when a selected app includes them.
Verify each installed tool with its version and a small relevant functional check.
```

The existing [full inventory](catalog.md) holds the verification details and cost references. It is not the download queue. This file is the download queue.
