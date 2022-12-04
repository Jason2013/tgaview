# coding=utf-8

import os
import sys

def convert_old(in_file, out_file):
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

def convert(in_file, out_file):
    # print(in_file)
    # print(out_file)
    # with open(out_file, "w", encoding="utf-8") as out_file, open(in_file, "rb") as in_file:
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
    input_dir = os.path.join(sys.argv[1], "shaders")
    output_dir = sys.argv[2]
    output_file_basename = sys.argv[3]
    output_header_file = os.path.join(output_dir, output_file_basename + ".h")
    output_source_file = os.path.join(output_dir, output_file_basename + ".cpp")

    with open(output_header_file, "w", encoding="utf-8") as hf, open(output_source_file, "w", encoding="utf-8") as sf:
        for i in range(4, len(sys.argv)):
            shader_file = sys.argv[i]
            shader_var = shader_file.replace(".", "_")
            hf.write("extern unsigned char %s_code[];\n" % shader_var)
            sf.write("unsigned char %s_code[] = {\n" % shader_var)
            input_shader_file = os.path.join(input_dir, shader_file)
            with open(input_shader_file, "rb") as isf: 
                convert(isf, sf)
            sf.write("};\n")
                # hf.write hs
                # sf
# k


    # convert(os.path.join(sys.argv[1], "shaders", "4.1.texture.fs"), os.path.join(sys.argv[2], "4.1.texture.fs.h"))
    # convert(os.path.join(sys.argv[1], "shaders", "4.1.texture.vs"), os.path.join(sys.argv[2], "4.1.texture.vs.h"))
