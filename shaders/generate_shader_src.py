# coding=utf-8

import os
import sys

def convert(in_file, out_file):
    print(in_file)
    print(out_file)
    with open(out_file, "w", encoding="utf-8") as out_file, open(in_file, "rb") as in_file:
        data = in_file.read()
        n = 0
        for c in data:
            out_file.write("0x{:02x},".format(c))
            n += 1
            if n == 16:
                out_file.write("\n")
                n = 0
            else:
                out_file.write(" ")
        out_file.write("0x00\n")

if __name__ == "__main__":
    print(sys.argv)
    convert(os.path.join(sys.argv[1], "shaders", "4.1.texture.fs"), os.path.join(sys.argv[2], "4.1.texture.fs.h"))
    convert(os.path.join(sys.argv[1], "shaders", "4.1.texture.vs"), os.path.join(sys.argv[2], "4.1.texture.vs.h"))
