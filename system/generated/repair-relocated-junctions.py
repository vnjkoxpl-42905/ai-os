"""Repair relocated Deno junctions; preserve originals and never traverse links."""
import ctypes
import json
import os
import struct
from pathlib import Path

ROOT = Path('C:/Users/Joshu/dev/ai-os-projects')
OLD = 'C:\\Users\\Joshu\\dev\\ai-os\\projects\\'
NEW = 'C:\\Users\\Joshu\\dev\\ai-os-projects\\'
kernel = ctypes.WinDLL('kernel32', use_last_error=True)
kernel.CreateFileW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p]
kernel.CreateFileW.restype = ctypes.c_void_p
kernel.DeviceIoControl.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.c_void_p]
kernel.CloseHandle.argtypes = [ctypes.c_void_p]

def junction(path, target):
    os.mkdir(path)
    substitute = ('\\??\\' + target.removeprefix('\\\\?\\')).encode('utf-16-le')
    printable = target.encode('utf-16-le')
    names = substitute + b'\0\0' + printable + b'\0\0'
    data = struct.pack('<IHHHHHH', 0xA0000003, len(names) + 8, 0, 0, len(substitute), len(substitute) + 2, len(printable)) + names
    handle = kernel.CreateFileW(str(path), 0x40000000, 0, None, 3, 0x02200000, None)
    if handle == ctypes.c_void_p(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        buffer = ctypes.create_string_buffer(data)
        count = ctypes.c_uint32()
        if not kernel.DeviceIoControl(handle, 0x900A4, buffer, len(data), None, 0, ctypes.byref(count), None):
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        kernel.CloseHandle(handle)

report = {'repaired': 0, 'links_checked': 0, 'remaining_old': [], 'missing_targets': 0, 'errors': []}
for project in ROOT.iterdir():
    deno = project / 'node_modules' / '.deno'
    if not deno.is_dir():
        continue
    queue = [deno]
    while queue:
        directory = queue.pop()
        for entry in os.scandir(directory):
            if entry.name.endswith('.pre-relocation-link'):
                continue
            if not entry.is_dir(follow_symlinks=False) and not entry.is_symlink():
                continue
            path = Path(entry.path)
            if entry.stat(follow_symlinks=False).st_file_attributes & 0x400:
                target = os.readlink(path)
                normalized = target.removeprefix('\\\\?\\').replace('/', '\\')
                report['links_checked'] += 1
                report['missing_targets'] += not os.path.exists(normalized)
                if not normalized.lower().startswith(OLD.lower()):
                    continue
                updated = NEW + normalized[len(OLD):]
                backup = path.with_name(path.name + '.pre-relocation-link')
                try:
                    if os.path.lexists(backup):
                        raise RuntimeError('Preserved-link collision')
                    path.rename(backup)
                    junction(path, updated)
                    report['repaired'] += 1
                except Exception as error:
                    report['errors'].append({'path': str(path), 'error': str(error)})
            elif directory == deno or entry.name == 'node_modules' or (directory.name == 'node_modules' and entry.name.startswith('@')):
                queue.append(path)
    print(project.name, report['repaired'], len(report['errors']), flush=True)
Path(__file__).with_name('relocation-junctions.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({k: v for k, v in report.items() if k != 'errors'}), flush=True)
