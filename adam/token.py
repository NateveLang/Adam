import adam.grammar as gr
from adam.utils import tostring

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

def get_token_ID(lexema, module = gr):

    for token in module.protected_tokens:

        if lexema == token[0]:
            return token[1]

    return module.identifier

def get_token_Symbol(lexema, module = gr):

    for token in module.protected_tokens:

        if lexema == token[1]:
            return token[0]
    
    return str(module.identifier)
