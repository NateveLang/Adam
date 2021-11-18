import nqa.grammar as gr
import nqa.templates as tp
from nqa.token import Tokens, get_token_ID
from nqa.error import LexicalError
from nqa.utils import tostring

F = False

# Main code

def scanner(text, command = None):
    dev_mode = command in ["dev"]

    commentary, string, name, number, float, operator, docstring =  F, F, F, F, F, F, 0

    tokens = Tokens()
    errors = 0
    line, pos = 1, 1

    lexema = ""
    string_ch = ""

    text += "\n ~eof tokens for security~ ~including the \n, DO NOT REMOVE THE EXTRA \n~"

    i = 0
    while i < len(text):

        ch = text[i]

        tokens_num = len(tokens)

        if tokens_num > 0:
            last_line = tokens[tokens_num - 1][4]

        if docstring > 0 and ch != string_ch:
            lexema += ch
        
        elif ch == "\n":

            if string:
                tokens.add(lexema, gr.STRING, line, pos)
                string = F
            
            elif number:
                if float:
                    tokens.add(lexema + "0", gr.FLOAT, line, pos, last_line)
                else:
                    tokens.add(lexema, gr.INT, line, pos, last_line)
                number = F
                float = F
            
            elif name:
                tokens.add(lexema, get_token_ID(lexema), line, pos)
                name = F
            
            elif operator:
                id = get_token_ID(lexema)

                if id == gr.identifier:
                    for lex in lexema:
                        tokens.add(lex, get_token_ID(lex), line, pos, last_line)
                else:
                    tokens.add(lexema, id, line, pos, last_line)
                
                operator = F
            
            lexema = ""
            line += 1
            pos = 1

        elif docstring > 0 and ch == string_ch:
            docstring -= 1

            if docstring == 0:
                tokens.add(lexema, gr.DOCSTRING, line, pos)
                string_ch = ""
                lexema = ""

        elif commentary and ch not in gr.commentaries:
            pass

        elif commentary and ch in gr.commentaries:
            commentary = F
        
        elif string and ch not in gr.strings:
            lexema += ch

        elif string and ch == string_ch:

            if text[i + 1] == string_ch:
                docstring = 3
                i += 1
            else:
                tokens.add(lexema, gr.STRING, line, pos)
                lexema = ""
                string_ch = ""
            
            string = F
        
        elif float and ch in gr.digits:
            lexema += ch

        elif float and ch in gr.floating:
            errors += LexicalError(line, f"two {gr.floating} in float definition")
            break

        elif number and not float and ch in (gr.digits + gr.floating):
            lexema += ch

            if ch in gr.floating:
                float = True

        elif number and ch not in (gr.digits + gr.floating):

            if float:
                tokens.add(lexema + "0", gr.FLOAT, line, pos, last_line)
            else:
                tokens.add(lexema, gr.INT, line, pos, last_line)

            lexema = ""
            i -= 1
            pos -= 1
            number, float = F, F
        
        elif name and ch in gr.alphanum:
            lexema += ch

        elif name and ch not in gr.alphanum:
            tokens.add(lexema, get_token_ID(lexema), line, pos)
            lexema = ""
            i -= 1
            pos -= 1
            name = F
        
        elif operator and ch in gr.operators:
            lexema += ch

        elif operator and ch not in gr.operators:
            id = get_token_ID(lexema)

            if id == gr.identifier:
                for lex in lexema:
                    tokens.add(lex, get_token_ID(lex), line, pos, last_line)
            else:
                tokens.add(lexema, id, line, pos, last_line)

            lexema = ""
            i -= 1
            pos -= 1
            operator = F

        elif not commentary and ch in gr.commentaries:
            commentary = True

        elif not string and ch in gr.strings:
            string = True
            string_ch = ch

        elif not name and ch in gr.alphabet:
            name = True
            lexema += ch

        elif not name and not number and ch in gr.digits:
            number = True
            lexema += ch

        elif not name and not number and not operator and ch in gr.operators:
            operator = True
            lexema += ch

        elif ch not in gr.blanks:
            tokens.add(ch, ch, line, pos)

        i += 1
        pos += 1

    if errors > 0:
        print("Traceback:", tokens)

    tokens.set_last_line(line, pos)

    log = ""

    if dev_mode:
        log += f"Last line: {line} Last column: {pos}\n"
        log += f"Tokens detected: {len(tokens)}\n"

        names = tokens.get_names()
        string_of_names = tostring(names, ", ")
        log += f"Names detected ({len(names)}): {string_of_names}\n"

    return tokens, errors, log
