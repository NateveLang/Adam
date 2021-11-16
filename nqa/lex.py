import nqa.grammar as gr
import nqa.templates as tp
from nqa.utils import tostring
from nqa.error import *

T, F, e = True, False, ""

def get_token_ID(lexema):
    for token in gr.protected_tokens:
        if lexema == token[0]:
            return token[1]
    return gr.identifier

def get_token_Symbol(lexema):
    for token in gr.protected_tokens:
        if lexema == token[1]:
            return token[0]
    return str(gr.identifier)

class Token(list):
    def __init__(self, lexema, ID, line, position, relative_line = -1):
        self.append(lexema)
        self.append(ID)
        self.append(line)
        self.append(position)

        if relative_line == -1:
            self.append(line)
        else:
            self.append(relative_line)
    
    @property
    def symbol(self):
        return self[0]

    @property
    def name(self):
        return self[0]
    
    @property
    def ID(self):
        return self[1]
    
    @property
    def line(self):
        return self[2]

    @property
    def position(self):
        return self[3]

    @property
    def relative_line(self):
        return self[4]

    def is_expected(self, expected_types):
        if self.ID in expected_types:
            return True
        else:
            types = ""
            for i in range(len(expected_types)):
                if i > 0:
                    types += " or "
                types += tostring(expected_types[i])
            
            SyntaxError(f"{self.line}, column {self.position}", f"{types} expected")
            return False
    
    def is_protected(self):
        return (self.symbol in gr.protected) and (self.ID in gr.protected_indexes)

    def equal(self, symbol):
        return (self.symbol == symbol) and (self.ID == get_token_ID(symbol))

class Tokens(list):
    def __init__(self):
        super().__init__()
    
    def add(self, token, id, line, position, relative_line = -1):
        if relative_line == -1:
            relative_line = line
        self.append(Token(token, id, line, position, relative_line))
    
    def get_names(self):
        names = []
        for token in self:
            assert len(token) >= 2 
            if token[1] == gr.identifier and token[0] not in names:
                names.append(token[0])
        return names

    @property
    def last_line(self):
        assert self._last_line[0]
        return self._last_line[:]
    
    def set_last_line(self, line, pos):
        self._last_line = [line, pos]

class TokenType:
    def EOF(self, line, pos): # End Of File
        return Token("@EOF@", gr.eof, line, pos)
    def EOZ(self, line, pos): # End Of Zone
        return Token("@EOZ@", gr.eof, line, pos)

# Main code

def scanner(text, command = None):
    verbose = command in ["-v"]

    tokens = Tokens()
    commentary, string, name, number, float, operator, docstring =  F, F, F, F, F, F, 0
    lexema = e
    line = 1
    errors = 0
    pos = 1
    string_ch = ""

    text += "\n ~eof~ ~tokens~ ~for~ ~security~"

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
                float = T
        elif number and ch not in (gr.digits + gr.floating):
            if float:
                tokens.add(lexema + "0", gr.FLOAT, line, pos, last_line)
            else:
                tokens.add(lexema, gr.INT, line, pos, last_line)
            lexema = ""
            number, float = F, F
            i -= 1
            pos -= 1
        
        elif name and ch in gr.alphanum:
            lexema += ch
        elif name and ch not in gr.alphanum:
            name = F
            tokens.add(lexema, get_token_ID(lexema), line, pos)
            lexema = ""
            i -= 1
            pos -= 1
        
        elif operator and ch in gr.operators:
            lexema += ch
        elif operator and ch not in gr.operators:
            operator = F
            id = get_token_ID(lexema)
            if id == gr.identifier:
                for lex in lexema:
                    tokens.add(lex, get_token_ID(lex), line, pos, last_line)
            else:
                tokens.add(lexema, id, line, pos, last_line)
            lexema = ""
            i -= 1
            pos -= 1
            
        elif not commentary and ch in gr.commentaries:
            commentary = True
        elif not string and ch in gr.strings:
            string = T
            string_ch = ch
        elif not name and ch in gr.alphabet:
            name = T
            lexema += ch
        elif not name and not number and ch in gr.digits:
            number = T
            lexema += ch
        elif not name and not number and not operator and ch in gr.operators:
            operator = T
            lexema += ch
        elif ch not in gr.blanks:
            tokens.add(ch, ch, line, pos)
        i += 1
        pos += 1

    if errors > 0:
        print("Traceback:", tokens)

    tokens.set_last_line(line, pos)
    log = ""

    if verbose:
        log += f"Last line: {line} Last column: {pos}\n"
        log += f"Tokens detected: {len(tokens)}\n"
        names = tokens.get_names()
        string_of_names = tostring(names, ", ")
        log += f"Names detected ({len(names)}): {string_of_names}\n"

    return tokens, errors, log
