import zlib
import sys

with open("Examples/1111.pdf", "rb") as f:
    content = f.read()
    print(zlib.decompress(content).decode())