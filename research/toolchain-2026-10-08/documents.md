# Document and data tool inventory, 2026-10-08

Read-only inventory. No software was installed or downloaded. Detection used `winget list` and executable lookup in the current shell; absence from these checks does not prove a tool is absent from every private environment.

| Tool | Detected status | Practical use |
|---|---|---|
| 7-Zip | Installed package 26.04.00.0; `7z.exe` resolves to `C:/Users/Joshu/Tools/recovery-toolchain-20261006/7zip/x64/7z.exe` | Inspect and extract ZIP/7z archives. Package and PATH copy can differ. |
| Poppler PDF utilities | Bundled `pdfinfo.exe` and `pdftoppm.exe` detected | Inspect PDF metadata and render PDF pages as images. |
| Pandoc | Not detected in PATH or installed-package inventory | Convert Markdown, HTML and document formats. PDF output requires an appropriate additional engine. |
| Tesseract OCR | Not detected in PATH or installed-package inventory | Extract text from screenshots and scanned pages. OCR requires accuracy review. Windows installers are third-party builds documented by the project. |
| jq | Not detected in PATH or installed-package inventory | Filter, inspect and transform JSON returned by APIs and CLIs. PowerShell and Python already provide alternatives. |
| SQLite CLI | `sqlite3` not detected in PATH or installed-package inventory | Query local structured databases and source manifests. Python may provide SQLite access without this standalone shell; that is a separate runtime check. |
| Poppler `pdftotext` | Not detected in PATH or bundled Poppler directory | Extract text from text-based PDFs; scanned pages require OCR. |

Bundled Poppler directory:
`C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1007-641-0_26.1007.641.0_x64__3k8sg7r9htsxt/dependencies/native/poppler/Library/bin`

## Prioritized candidates

Pandoc and OCR are the clearest additions for document ingestion and screenshot/video prompt extraction. A full PDF text utility is useful for document processing. jq and SQLite CLI are convenient rather than necessary when existing Python/PowerShell tooling suffices. Installation remains deferred under the latest instruction.

Official references checked on 2026-10-08:

- [Pandoc installation](https://pandoc.org/installing.html)
- [Tesseract downloads and Windows build information](https://tesseract-ocr.github.io/tessdoc/Downloads.html)
- [jq downloads](https://jqlang.org/download/)
- [SQLite downloads](https://sqlite.org/download.html)
- [SQLite command-line shell](https://sqlite.org/cli.html)

No executable conversion/OCR/SQL tests were run because the candidate tools were not installed and this scope was changed to inventory only.
