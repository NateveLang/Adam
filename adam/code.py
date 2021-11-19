import adam.grammar as gr

def join(code_line):

    if len(code_line) > 0:

        code = code_line[0]
        symbols = gr.operators + [":"]

        for i in range(1, len(code_line)):

            if code_line[i] not in symbols and code_line[i - 1] not in symbols:
                code += " " + code_line[i]
            else:
                code += code_line[i]

        return code

    else:
        return ""
