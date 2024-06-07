import zlib
import os
from os.path import join, getsize
start = "c:\\Users\\movsx\\Downloads\\caesar\\caesar\\.git\\objects\\"
for root, dirs, files in os.walk(start):
    for name in files:
        print(root + "\\" + name)
        with open(root + "\\" + name, "rb") as f:
            try:
                content = f.read()
                print(zlib.decompress(content).decode())
            except:
                pass