from nqa.utils import tolist, tokenize

mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = ["'", '"', '"""', "'''"]
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}#$@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "float"
INT = "int"
COMPLEX = "complex"
STRING = "string"
DOCSTRING = "docstring"
NULL = "none"

USE, WAIT = "use", "wait"
INCLUDE, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
IF, ELIF, ELSE = "if", "elif", "else"
TRY, EXCEPT = "try", "except"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
OPERATOR, RETURN = "def", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

special_functions = """
def ninput(prompt = '', default = ''):
\treturn float(input(prompt, default))

def binput(prompt = '', default = ''):
\treturn bool(input(prompt, default))

def update_std():
\tsubprocess.call([sys.executable, "-m", "pip", "install", "eggdriver"])
"""


preprocess = [USE, WAIT]
process = [INCLUDE, FROM, AS, PASS, IN]
conditionals = [IF, ELIF, ELSE, TRY, EXCEPT]
loops = [WHILE, FOR, BREAK, CONTINUE]
functions = [OPERATOR, RETURN]
classes = [CLASS, SELF]
bools = [AND, OR, NOT, TRUE, FALSE]

primitives = [FLOAT, INT, COMPLEX, STRING, NULL]
std_funcs = preprocess + conditionals + loops + functions + classes + bools
operators = tolist(one_char_symbols) + two_char_symbols

protected = primitives + std_funcs + operators

protected_tokens = tokenize(protected)
protected_IDs = list(range(len(protected)))

identifier = 300
eof = 400
codes = [identifier, eof]

ALL = primitives + codes + protected_IDs