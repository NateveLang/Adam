import sys, subprocess

import adam.grammar as gr

def join(code_line):

    if len(code_line) > 0:

        _code = code_line[0]
        symbols = gr.operators + [":"]

        for i in range(1, len(code_line)):

            if code_line[i] not in symbols and code_line[i - 1] not in symbols:
                _code += " " + code_line[i]
            else:
                _code += code_line[i]

        return _code

    else:
        return ""

def run_python(code_lines = "", input = None):
    _code = "; ".join(code_lines.split("\n")) + "\n"

    subprocess.run([sys.executable, "-c", _code], input = input)
