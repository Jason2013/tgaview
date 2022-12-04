# coding=utf-8

import os
import sys


def convert(in_file, out_file):
        data = in_file.read()
        n = 0
        for c in data:
            if n == 0:
                out_file.write("    ")
            out_file.write("0x{:02x},".format(c))
            n += 1
            if n == 8:
                out_file.write("\n")
                n = 0
            else:
                out_file.write(" ")
        out_file.write("0x00\n")


if __name__ == "__main__":
    print(sys.argv)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    output_file_basename = sys.argv[3]
    output_header_file = os.path.join(output_dir, output_file_basename + ".h")
    output_header_macro = "__%s_H__" % output_file_basename.upper()
    output_source_file = os.path.join(output_dir, output_file_basename + ".cpp")

    with open(output_header_file, "w", encoding="utf-8") as hf, open(output_source_file, "w", encoding="utf-8") as sf:
        hf.write("#ifndef %s\n" % output_header_macro)
        hf.write("#define %s\n\n" % output_header_macro)
        sf.write("#include \"%s\"\n" % (output_file_basename + ".h"))

        for i in range(4, len(sys.argv)):
            shader_file = sys.argv[i]
            input_shader_file = os.path.join(input_dir, shader_file)
            shader_var = shader_file.replace(".", "_")

            hf.write("extern const char %s_code[];\n" % shader_var)
            sf.write("\n// This variable '%s_code' is generate from file: '%s'\n" % (shader_var, os.path.normpath(input_shader_file)))
            sf.write("const char %s_code[] = {\n" % shader_var)

            with open(input_shader_file, "rb") as isf: 
                convert(isf, sf)
            sf.write("};\n")

        hf.write("\n#endif // %s\n" % output_header_macro)
