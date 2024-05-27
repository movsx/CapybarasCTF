import zlib
import sys

with open("1111.pdf", "rb") as f:
    content = f.read()
    print(zlib.decompress(content).decode())