compiler_name = "adam"

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

USE, WAIT = "using", "wait"
INCLUDE, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
IF, ELIF, ELSE = "if", "elif", "else"
TRY, EXCEPT = "try", "except"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
OPERATOR, RETURN = "def", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

identifier = 300
eof = 400

special_functions = f"""
def ninput(prompt = '', default = ''):
\treturn float(input(prompt, default))

def binput(prompt = '', default = ''):
\treturn bool(input(prompt, default))

def update_std():
\tsubprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
\tfile = file_name.split('.')[0]
\tsubprocess.call([sys.executable, '-m', '{compiler_name}', 'build', file])
"""
