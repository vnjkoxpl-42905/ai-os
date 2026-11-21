"""Wait for the already-running hidden capture using a Windows process handle."""
import argparse, ctypes, json, subprocess, sys
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('--pid',type=int,required=True); p.add_argument('--log',required=True)
a=p.parse_args()
kernel=ctypes.WinDLL('kernel32',use_last_error=True)
kernel.OpenProcess.restype=ctypes.c_void_p
kernel.WaitForSingleObject.argtypes=[ctypes.c_void_p,ctypes.c_ulong]
kernel.CloseHandle.argtypes=[ctypes.c_void_p]
handle=kernel.OpenProcess(0x00100000,False,a.pid)
if handle:
    result=kernel.WaitForSingleObject(handle,3600000); kernel.CloseHandle(handle)
    if result!=0: raise SystemExit('Capture wait failed or exceeded one hour')
lines=Path(a.log).read_text().splitlines()
if not lines: raise SystemExit('Capture produced no completion summary')
summary=json.loads(lines[-1])
if summary.get('errors')!=0: raise SystemExit('Capture errors; no cloud success claimed')
subprocess.run([sys.executable,str(Path(__file__).with_name('new-machine-cloud.py')),'--generation',summary['generation']],check=True)
