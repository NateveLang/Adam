transpiler_name = "adam"

mayusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = ["'", '"', '"""', "'''"]
matrices = "$"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}#@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "float"
INT = "int"
COMPLEX = "complex"
STRING = "string"
DOCSTRING = "docstring"
NULL = "none"
MATRIX = "matrix"

USE, WAIT, INCLUDE = "using", "wait", "include"
IMPORT, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
IF, ELIF, ELSE = "if", "elif", "else"
TRY, EXCEPT = "try", "except"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
OPERATOR, RETURN = "def", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

identifier = 300
eof = 400

types = """
class matrix(Matrix):
\tdef __init__(self, *args):
\t\tsuper().__init__(*args)
\tdef times(self, b):
\t\timport numpy as np
\t\ta = np.array(self)
\t\tb = np.array(b)
\t\tc = a @ b
\t\ttemp =[]
\t\tfor i in c:
\t\t\ttemp.append(Vector(i))
\t\treturn matrix(temp)
\tdef __str__(self):
\t\tself.display()
\t\treturn ""
"""

special_functions = types + f"""
def ninput(prompt = '', default = ''):
\treturn float(input(prompt, default))

def binput(prompt = '', default = ''):
\treturn bool(input(prompt, default))

def update_std():
\tsubprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
\tfile = file_name.split('.')[0]
\tsubprocess.call([sys.executable, '-m', '{transpiler_name}', 'build', file])
"""
