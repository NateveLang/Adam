import sys

from adam import lex, code
import adam.grammar as gr
from adam.error import SemanticError, DeclarationError
from adam.zones import Zone

def navigator(zone, depth = -1, line = 1, file = sys.stdout, errors = 0):
    last_line = line
    code_line = []
    tab = "\t"

    if zone.type == "function":
        code_line += [gr.OPERATOR]
    elif zone.type == "class":
        code_line += [gr.CLASS]

    code_line += [zone.name]

    for dec in range(len(zone.declaration)):
        d = zone.declaration[dec]
        
        if d.relative_line > last_line:
            content = depth * tab + code.join(code_line)
            print(content, file = file)

            last_line = d.relative_line
            code_line = []
        
        if type(d) == Zone:
            errors += SemanticError(d.line, "Declaring a zone into another a declaration")
            break
        elif d.name == zone.name:
            errors += DeclarationError(d.line, "Calling a name into its declaration sentence")
            break
        else:

            if d.ID == gr.STRING:
                code_line += [f'"{d.symbol}"']
            elif d.ID == gr.DOCSTRING:
                code_line += ['"""' + d.symbol + '"""']
            else:
                code_line += [d.symbol]
    
    depth_2 = depth + 1

    first_line = True

    for stat in range(len(zone.statements)):
        s = zone.statements[stat]
        
        if s.relative_line > last_line:

            if not first_line:
                content = (depth_2 + 1) * tab + code.join(code_line)
                print(content, file = file)
            else:
                content = depth_2 * tab + code.join(code_line)
                print(content, file = file)
            
            last_line = s.relative_line
            code_line = []

        if type(s) == Zone:
            errors = navigator(s, depth_2, last_line, file, errors)
        elif s.ID == gr.STRING:
            code_line += [f'"{s.symbol}"']
        elif s.ID == gr.DOCSTRING:
            code_line += ['"""' + s.symbol + '"""']
        else:
            code_line += [f"{s.symbol}"]
        
        if first_line:
            first_line = False

    return errors

# middle code generator
def generator(tree, file_name, errors, main = "root()", exceptions = "except:\n\tpass"):

    file_name = file_name + ".py"
    file = open(file_name, "w")

    if errors > 0:
        file.close()
        return errors

    init = """try:
\tfrom eggdriver import *
\timport sys, os, subprocess
except ImportError:
\tprint('ImportError')
"""

    close = f"""try:
\t{main}
{exceptions}
"""

    print(init, file = file)
    print(gr.special_functions, file = file)

    errors = navigator(tree, -1, 1, file, errors)

    print(close, file = file)

    file.close()
    return errors
