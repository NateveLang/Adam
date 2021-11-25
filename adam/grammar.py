from adam.utils import tolist, tokenize

transpiler_name = "adam"

mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = ["'", '"', '"""', "'''"]
matrices = "$"
vectors = "[]"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>(){}#@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "float"
INT = "int"
COMPLEX = "complex"
STRING = "string"
DOCSTRING = "docstring"
NULL = "none"
MATRIX = "matrix"
VECTOR = "vector"

USE, WAIT, INCLUDE = "using", "wait", "include"
IMPORT, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
IF, ELIF, ELSE = "if", "elif", "else"
TRY, EXCEPT, WITH = "try", "except", "with"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
OPERATOR, RETURN = "def", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

special_functions = f"""
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

preprocess = [USE, WAIT, INCLUDE]
process = [IMPORT, FROM, AS, PASS, IN]
conditionals = [IF, ELIF, ELSE, TRY, EXCEPT, WITH]
loops = [WHILE, FOR, BREAK, CONTINUE]
functions = [OPERATOR, RETURN]
classes = [CLASS, SELF]
bools = [AND, OR, NOT, TRUE, FALSE]

primitives = [FLOAT, INT, COMPLEX, MATRIX, VECTOR, STRING, NULL]
std_funcs = preprocess + process + conditionals + loops + functions + classes + bools
operators = tolist(one_char_symbols) + two_char_symbols

protected = primitives + std_funcs + operators

protected_tokens = tokenize(protected)
protected_IDs = list(range(len(protected)))

identifier = 300
eof = 400
codes = [identifier, eof]

ALL = primitives + codes + protected_IDs
