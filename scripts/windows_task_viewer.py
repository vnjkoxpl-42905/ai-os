"""Laptop Control Board for Windows. Uses only Python's standard library."""

from __future__ import annotations

import ctypes
import json
import subprocess
import threading
import tkinter as tk
from ctypes import wintypes
from tkinter import messagebox, ttk


if not hasattr(ctypes, "windll"):
    raise SystemExit("Laptop Control Board runs on Windows only.")

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
psapi = ctypes.windll.psapi

PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
WM_CLOSE = 0x0010
TH32CS_SNAPPROCESS = 0x00000002
HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010


class PROCESSENTRY32W(ctypes.Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ProcessID", wintypes.DWORD),
        ("th32DefaultHeapID", ctypes.c_size_t),
        ("th32ModuleID", wintypes.DWORD),
        ("cntThreads", wintypes.DWORD),
        ("th32ParentProcessID", wintypes.DWORD),
        ("pcPriClassBase", wintypes.LONG),
        ("dwFlags", wintypes.DWORD),
        ("szExeFile", wintypes.WCHAR * 260),
    ]


class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD),
        ("PageFaultCount", wintypes.DWORD),
        ("PeakWorkingSetSize", ctypes.c_size_t),
        ("WorkingSetSize", ctypes.c_size_t),
        ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
        ("QuotaPagedPoolUsage", ctypes.c_size_t),
        ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
        ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
        ("PagefileUsage", ctypes.c_size_t),
        ("PeakPagefileUsage", ctypes.c_size_t),
    ]


class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", wintypes.DWORD),
        ("dwMemoryLoad", wintypes.DWORD),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]


kernel32.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
kernel32.CreateToolhelp32Snapshot.argtypes = [wintypes.DWORD, wintypes.DWORD]
kernel32.Process32FirstW.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
kernel32.Process32NextW.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
kernel32.OpenProcess.restype = wintypes.HANDLE
kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
psapi.GetProcessMemoryInfo.argtypes = [
    wintypes.HANDLE,
    ctypes.POINTER(PROCESS_MEMORY_COUNTERS),
    wintypes.DWORD,
]
kernel32.GlobalMemoryStatusEx.restype = wintypes.BOOL
kernel32.GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(MEMORYSTATUSEX)]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.IsWindowVisible.restype = wintypes.BOOL
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextLengthW.restype = ctypes.c_int
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowTextW.restype = ctypes.c_int
user32.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
user32.EnumWindows.restype = wintypes.BOOL
user32.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.PostMessageW.restype = wintypes.BOOL
user32.SetWindowPos.argtypes = [
    wintypes.HWND,
    wintypes.HWND,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    wintypes.UINT,
]


def memory_snapshot() -> tuple[int, int]:
    status = MEMORYSTATUSEX()
    status.dwLength = ctypes.sizeof(status)
    if not kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        return 0, 0
    return int(status.ullTotalPhys), int(status.ullAvailPhys)


def process_snapshot() -> dict[int, dict[str, int | str]]:
    """Read process names, parent IDs, and each process's working memory."""
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    invalid_handle = ctypes.c_void_p(-1).value
    if not snapshot or snapshot == invalid_handle:
        return {}

    rows: dict[int, dict[str, int | str]] = {}
    entry = PROCESSENTRY32W()
    entry.dwSize = ctypes.sizeof(entry)
    try:
        ok = kernel32.Process32FirstW(snapshot, ctypes.byref(entry))
        while ok:
            pid = int(entry.th32ProcessID)
            handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
            ram = 0
            if handle:
                counters = PROCESS_MEMORY_COUNTERS()
                counters.cb = ctypes.sizeof(counters)
                if psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb):
                    ram = int(counters.WorkingSetSize)
                kernel32.CloseHandle(handle)
            rows[pid] = {
                "pid": pid,
                "parent": int(entry.th32ParentProcessID),
                "name": str(entry.szExeFile),
                "ram": ram,
            }
            ok = kernel32.Process32NextW(snapshot, ctypes.byref(entry))
    finally:
        kernel32.CloseHandle(snapshot)
    return rows


def visible_windows() -> list[dict[str, int | str]]:
    windows: list[dict[str, int | str]] = []
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    def visit(hwnd: int, _lparam: int) -> bool:
        if not user32.IsWindowVisible(hwnd):
            return True
        length = user32.GetWindowTextLengthW(hwnd)
        if length < 1:
            return True
        title = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, title, length + 1)
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        windows.append({"hwnd": int(hwnd), "pid": int(pid.value), "title": title.value})
        return True

    user32.EnumWindows.argtypes = [callback_type, wintypes.LPARAM]
    user32.EnumWindows(callback_type(visit), 0)
    return windows


def root_process(pid: int, processes: dict[int, dict[str, int | str]]) -> int:
    """Collapse same-named helper processes to the app's main process."""
    if pid not in processes:
        return pid
    name = str(processes[pid]["name"]).casefold()
    root = pid
    seen: set[int] = set()
    while root in processes and root not in seen:
        seen.add(root)
        parent = int(processes[root]["parent"])
        if parent not in processes or str(processes[parent]["name"]).casefold() != name:
            break
        root = parent
    return root


def descendants(root: int, processes: dict[int, dict[str, int | str]]) -> set[int]:
    family = {root}
    changed = True
    while changed:
        changed = False
        for pid, info in processes.items():
            if pid not in family and int(info["parent"]) in family:
                family.add(pid)
                changed = True
    return family


def format_mb(byte_count: int) -> str:
    return f"{byte_count / (1024 * 1024):,.0f} MB"


class ControlBoard:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Laptop Control Board")
        root.geometry("1100x700")
        root.minsize(820, 520)

        self.processes: dict[int, dict[str, int | str]] = {}
        self.window_rows: dict[str, dict[str, int | str]] = {}
        self.process_rows: dict[str, dict[str, int | str]] = {}
        self.automation_loading = False
        self.is_topmost = tk.BooleanVar(value=True)
        root.attributes("-topmost", True)

        header = ttk.Frame(root, padding=(16, 14, 16, 8))
        header.pack(fill="x")
        ttk.Label(header, text="Laptop Control Board", font=("Segoe UI", 18, "bold")).pack(side="left")
        ttk.Button(header, text="Refresh now", command=self.refresh).pack(side="right", padx=(8, 0))
        ttk.Checkbutton(
            header,
            text="Keep on top",
            variable=self.is_topmost,
            command=self.toggle_topmost,
        ).pack(side="right")

        self.ram_label = ttk.Label(root, text="Reading system memory…", font=("Segoe UI", 11, "bold"))
        self.ram_label.pack(anchor="w", padx=18)
        self.ram_bar = ttk.Progressbar(root, maximum=100, mode="determinate")
        self.ram_bar.pack(fill="x", padx=18, pady=(5, 7))
        self.explanation = ttk.Label(
            root,
            text=(
                "Memory belongs to Windows processes. ChatGPT/Codex desktop can share memory across chats; "
                "the app does not expose a reliable per-chat split to Windows. App totals add process working sets, "
                "so shared memory pages can be counted more than once."
            ),
            wraplength=1040,
        )
        self.explanation.pack(anchor="w", padx=18, pady=(0, 10))

        tabs = ttk.Notebook(root)
        tabs.pack(fill="both", expand=True, padx=14, pady=(0, 8))
        self.windows_tab = ttk.Frame(tabs, padding=8)
        self.processes_tab = ttk.Frame(tabs, padding=8)
        self.automation_tab = ttk.Frame(tabs, padding=8)
        tabs.add(self.windows_tab, text="Open windows")
        tabs.add(self.processes_tab, text="All processes")
        tabs.add(self.automation_tab, text="Login & scheduled")

        self.windows_table = self.make_table(
            self.windows_tab,
            ("title", "app", "pid", "memory"),
            (("title", "Window / current page title", 450, "w"),
             ("app", "App", 190, "w"),
             ("pid", "Window PID", 100, "e"),
             ("memory", "App family RAM (shared)", 200, "e")),
        )
        ttk.Label(
            self.windows_tab,
            text="For individual Chrome tabs, open Chrome and press Shift + Esc. This list shows window titles.",
        ).pack(anchor="w", pady=(6, 0))

        self.processes_table = self.make_table(
            self.processes_tab,
            ("name", "pid", "parent", "memory", "window"),
            (("name", "Process", 280, "w"),
             ("pid", "PID", 95, "e"),
             ("parent", "Parent PID", 110, "e"),
             ("memory", "This process RAM", 150, "e"),
             ("window", "Window", 290, "w")),
        )

        automation_bar = ttk.Frame(self.automation_tab)
        automation_bar.pack(fill="x", pady=(0, 6))
        ttk.Button(automation_bar, text="Refresh login and scheduled items", command=self.load_automation_data).pack(side="left")
        self.automation_status = ttk.Label(automation_bar, text="Loading Windows startup information…")
        self.automation_status.pack(side="left", padx=10)

        ttk.Label(
            self.automation_tab,
            text="Login apps start when you sign in. Scheduled tasks can run at login or boot, or while the laptop is idle. This page is read-only.",
        ).pack(anchor="w", pady=(0, 8))
        ttk.Label(self.automation_tab, text="Apps configured to start at login", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.startup_table = self.make_table(
            self.automation_tab,
            ("name", "source", "user", "program"),
            (("name", "Name", 220, "w"),
             ("source", "Registered in", 220, "w"),
             ("user", "Account", 180, "w"),
             ("program", "Program", 390, "w")),
        )
        self.startup_table.configure(height=7)
        ttk.Label(self.automation_tab, text="Enabled tasks that run at login or boot, plus tasks running now", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10, 0))
        self.scheduled_table = self.make_table(
            self.automation_tab,
            ("task", "state", "trigger", "program"),
            (("task", "Scheduled task", 300, "w"),
             ("state", "State", 100, "w"),
             ("trigger", "Starts when", 190, "w"),
             ("program", "Program", 420, "w")),
        )
        self.scheduled_table.configure(height=8)

        footer = ttk.Frame(root, padding=(16, 4, 16, 12))
        footer.pack(fill="x")
        ttk.Button(footer, text="Close selected window…", command=self.close_selected_window).pack(side="left")
        ttk.Label(
            footer,
            text="This sends a normal close request. It does not force-kill shared background processes.",
        ).pack(side="left", padx=10)
        self.status = ttk.Label(footer, text="Refreshing every 3 seconds")
        self.status.pack(side="right")

        self.refresh()
        self.load_automation_data()

    @staticmethod
    def make_table(parent: ttk.Frame, columns: tuple[str, ...], specs: tuple[tuple[str, str, int, str], ...]) -> ttk.Treeview:
        table = ttk.Treeview(parent, columns=columns, show="headings", selectmode="browse")
        for key, label, width, anchor in specs:
            table.heading(key, text=label)
            table.column(key, width=width, anchor=anchor)
        table.pack(fill="both", expand=True)
        return table

    def toggle_topmost(self) -> None:
        self.root.attributes("-topmost", self.is_topmost.get())

    def refresh(self) -> None:
        self.processes = process_snapshot()
        windows = visible_windows()
        total_ram, available_ram = memory_snapshot()
        used_ram = max(total_ram - available_ram, 0)
        used_percent = (used_ram / total_ram * 100) if total_ram else 0
        self.ram_label.configure(
            text=f"System RAM: {format_mb(used_ram)} used of {format_mb(total_ram)}  |  {format_mb(available_ram)} available"
        )
        self.ram_bar["value"] = used_percent

        self.window_rows.clear()
        self.process_rows.clear()
        for row in self.windows_table.get_children():
            self.windows_table.delete(row)
        for row in self.processes_table.get_children():
            self.processes_table.delete(row)

        window_titles_by_pid: dict[int, list[str]] = {}
        roots_with_windows: set[int] = set()
        for window in windows:
            pid = int(window["pid"])
            if pid not in self.processes:
                continue
            title = str(window["title"])
            window_titles_by_pid.setdefault(pid, []).append(title)
            roots_with_windows.add(root_process(pid, self.processes))

        family_ram: dict[int, int] = {}
        for root_pid in roots_with_windows:
            family_ram[root_pid] = sum(
                int(self.processes[pid]["ram"])
                for pid in descendants(root_pid, self.processes)
                if pid in self.processes
            )

        windows.sort(
            key=lambda item: family_ram.get(root_process(int(item["pid"]), self.processes), 0),
            reverse=True,
        )
        for window in windows:
            pid = int(window["pid"])
            if pid not in self.processes:
                continue
            proc = self.processes[pid]
            root_pid = root_process(pid, self.processes)
            iid = str(window["hwnd"])
            self.window_rows[iid] = window
            self.windows_table.insert(
                "", "end", iid=iid,
                values=(window["title"], proc["name"], pid, format_mb(family_ram.get(root_pid, int(proc["ram"]))),),
            )

        process_by_memory = sorted(
            self.processes.values(), key=lambda item: int(item["ram"]), reverse=True
        )
        title_by_pid = {pid: " | ".join(titles[:2]) for pid, titles in window_titles_by_pid.items()}
        for proc in process_by_memory:
            pid = int(proc["pid"])
            iid = str(pid)
            self.process_rows[iid] = proc
            self.processes_table.insert(
                "", "end", iid=iid,
                values=(proc["name"], pid, proc["parent"], format_mb(int(proc["ram"])), title_by_pid.get(pid, "")),
            )

        self.status.configure(text=f"Updated. {len(windows)} titled windows, {len(self.processes)} processes.")
        self.root.after(3000, self.refresh)

    def load_automation_data(self) -> None:
        if self.automation_loading:
            return
        self.automation_loading = True
        self.automation_status.configure(text="Reading startup entries and scheduled tasks…")
        threading.Thread(target=self._read_automation_data, daemon=True).start()

    def _read_automation_data(self) -> None:
        script = r'''
$startup = @(Get-CimInstance Win32_StartupCommand | ForEach-Object {
  $program = if ($_.Command -match '^"([^"]+)"') { $Matches[1] } elseif ($_.Command -match '^([^ ]+)') { $Matches[1] } else { $_.Command }
  [pscustomobject]@{ Name=$_.Name; Source=$_.Location; User=$_.User; Program=$program }
})
$tasks = @(Get-ScheduledTask | Where-Object { $_.State -ne 'Disabled' } | ForEach-Object {
  $task = $_
  $starts = @($task.Triggers | ForEach-Object {
    $class = $_.CimClass.CimClassName
    if ($class -match 'Logon|Boot') { $class -replace '^MSFT_Task','' }
  } | Where-Object { $_ })
  if ($starts.Count -gt 0 -or $task.State -eq 'Running') {
    $program = @($task.Actions | ForEach-Object { $_.Execute } | Where-Object { $_ }) -join '; '
    [pscustomobject]@{
      Name=($task.TaskPath + $task.TaskName)
      State=[string]$task.State
      Starts=($starts -join ', ')
      Program=$program
    }
  }
})
[pscustomobject]@{ Startup=$startup; Tasks=$tasks } | ConvertTo-Json -Depth 5 -Compress
'''
        try:
            result = subprocess.run(
                ["powershell.exe", "-NoLogo", "-NoProfile", "-Command", script],
                capture_output=True,
                text=True,
                timeout=45,
                check=True,
            )
            payload = json.loads(result.stdout)
            startup_rows = payload.get("Startup") or []
            task_rows = payload.get("Tasks") or []
            if not isinstance(startup_rows, list):
                startup_rows = [startup_rows]
            if not isinstance(task_rows, list):
                task_rows = [task_rows]
            error = ""
        except Exception as exc:
            startup_rows, task_rows = [], []
            error = f"Could not read Windows startup data: {exc}"
        self.root.after(0, lambda: self._show_automation_data(startup_rows, task_rows, error))

    def _show_automation_data(
        self,
        startup_rows: list[dict[str, str]],
        task_rows: list[dict[str, str]],
        error: str,
    ) -> None:
        self.automation_loading = False
        for table in (self.startup_table, self.scheduled_table):
            for item in table.get_children():
                table.delete(item)
        for index, row in enumerate(startup_rows):
            self.startup_table.insert(
                "", "end", iid=f"startup-{index}",
                values=(row.get("Name", ""), row.get("Source", ""), row.get("User", ""), row.get("Program", "")),
            )
        for index, row in enumerate(task_rows):
            self.scheduled_table.insert(
                "", "end", iid=f"task-{index}",
                values=(row.get("Name", ""), row.get("State", ""), row.get("Starts", "Running now"), row.get("Program", "")),
            )
        if error:
            self.automation_status.configure(text=error)
        else:
            self.automation_status.configure(
                text=f"{len(startup_rows)} login entries; {len(task_rows)} logon/boot or currently running tasks."
            )

    def close_selected_window(self, _event: object | None = None) -> None:
        selected = self.windows_table.selection()
        if not selected:
            messagebox.showinfo("Select a window", "Choose a row in Open windows first.", parent=self.root)
            return
        window = self.window_rows.get(selected[0])
        if not window:
            self.refresh()
            return
        title = str(window["title"])
        if messagebox.askyesno(
            "Close this window?",
            f"Ask the app to close this window?\n\n{title}\n\nSave any work first.",
            parent=self.root,
        ):
            user32.PostMessageW(int(window["hwnd"]), WM_CLOSE, 0, 0)
            self.root.after(500, self.refresh)


def main() -> None:
    root = tk.Tk()
    ControlBoard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
