import sys

from    adam import             code
from    adam.embedding import   Language
from    adam.error import       SemanticError, DeclarationError
import  adam.grammar as         gr
import  adam.templates as       temp
from    adam.zones import       Zone


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
            
            if file != None:
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
            
            if d.ID == gr.embedding:
                words = d.symbol
                lines = words.split("\n")
                lang = lines[2]
                new_lines = lines[3:]
                words = "\n".join(new_lines)
                embedded_language = Language(lang)
                generated_code = embedded_language.build(words)
                gc = generated_code.split("\n")
                content = ""

                for gc_line in gc:
                    content += (depth + 2) * tab + gc_line + "\n"

                if file != None:
                    print(content, file = file)

            elif d.ID == gr.STRING:
                code_line += [f'"{d.symbol}"']

            elif d.ID == gr.DOCSTRING:
                code_line += ['"""' + d.symbol + '"""']

            elif d.ID == gr.MATRIX:
                replacements = ""
                lexema = ""
                name = False

                for ch in d.symbol:
                        
                    if not name and ch in gr.alphabet:
                        lexema = ch
                        name = True

                    elif name and ch not in gr.alphanum:
                        replacements += f".replace('{lexema}', str({lexema}))"
                        lexema = ""
                        name = False

                    elif name and ch in gr.alphanum:
                        lexema += ch

                code_line += ['matrix("""' + d.symbol + '""")' + replacements]

            elif d.ID == gr.VECTOR:
                code_line += ['vector(' + d.symbol + ')']

            else:
                code_line += [d.symbol]
    
    depth_2 = depth + 1

    first_line = True

    for stat in range(len(zone.statements)):
        s = zone.statements[stat]
        
        if s.relative_line > last_line:

            if not first_line:
                content = (depth_2 + 1) * tab + code.join(code_line)

                if file != None:
                    print(content, file = file)

            else:
                content = depth_2 * tab + code.join(code_line)

                if file != None:
                    print(content, file = file)
            
            last_line = s.relative_line
            code_line = []

        if type(s) == Zone:
            errors = navigator(s, depth_2, last_line, file, errors)

        elif s.ID == gr.embedding:
            words = s.symbol
            lines = words.split("\n")
            lang = lines[2]
            new_lines = lines[3:]
            words = "\n".join(new_lines)
            embedded_language = Language(lang)
            generated_code = embedded_language.build(words)
            gc = generated_code.split("\n")
            content = ""

            for gc_line in gc:
                content += (depth + 2) * tab + gc_line + "\n"

            if file != None:
                print(content, file = file)

        elif s.ID == gr.STRING:
            code_line += [f'"{s.symbol}"']

        elif s.ID == gr.DOCSTRING:
            code_line += [f'"""{s.symbol}"""']

        elif s.ID == gr.MATRIX:
            replacements = ""
            lexema = ""
            name = False

            for ch in s.symbol:
                    
                if not name and ch in gr.alphabet:
                    lexema = ch
                    name = True

                elif name and ch not in gr.alphanum:
                    replacements += f".replace('{lexema}', str({lexema}))"
                    lexema = ""
                    name = False

                elif name and ch in gr.alphanum:
                    lexema += ch
                        
            code_line += ['matrix("""' + s.symbol + '"""' + replacements + ')']

        elif s.ID == gr.VECTOR:
            code_line += ['vector(' + s.symbol + ')']	

        else:
            code_line += [f"{s.symbol}"]
        
        if first_line:
            first_line = False

    return errors

# middle code generator
def generator(tree, file_name, errors, main = "", exceptions = "\tpass", args = ["none"], templates = [temp.Template("english")]):
    direct_run_mode = "direct" in args

    if errors > 0:
        return errors

    init = """try:
\tfrom eggdriver import *
except ImportError:
\tprint('ImportError: Failing to import eggdriver')

try:
\tfrom adam.types import *
except ImportError:
\tprint('ImportError: Failing to import adam.types')

try:
\timport sys
except ImportError:
\tprint('ImportError: Failing to import sys')

try:
\timport os
except ImportError:
\tprint('ImportError: Failing to import os')

try:
\timport subprocess
except ImportError:
\tprint('ImportError: Failing to import subprocess')
"""
    
    file_name = file_name.split("/")[-1]
    
    close = f"""try:
\t{file_name}()
{main}
except:
{exceptions}
"""

    if direct_run_mode:
        code.run_python(init)

        for tp in templates:
            code.run_python(tp.special_functions)

        errors = navigator(tree, -1, 1, None, errors)

        code.run_python(close)

    else:
        file_name = file_name + ".py"
        file = open(file_name, "w")

        print(init, file = file)
        
        for tp in templates:
            print(tp.special_functions, file = file)

        errors = navigator(tree, -1, 1, file, errors)
        
        if "moduled" not in args:
            print(close, file = file)

        file.close()

    return errors
