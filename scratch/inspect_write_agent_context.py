import os

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

# search for the function name or package name preceding offset 51211715
target_pos = 51211715
chunk = data[target_pos - 1500 : target_pos + 1500]

# find all strings in chunk
import re
strings = re.findall(rb"[a-zA-Z0-9_\.\-\/ :%]{4,}", chunk)
for s in strings:
    try:
        dec = s.decode('utf-8')
        if any(k in dec.lower() for k in ["agent", "custom", "format", "write", "parse", "proto", "cortex", "md"]):
            print(" ", dec)
    except:
        pass

