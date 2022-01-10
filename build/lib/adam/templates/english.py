# The name of the transpiler. This line is required. Do not change it.
transpiler_name = "adam"

"""
The following code is the translation of the code.
You can write your code here and modify the content of the variables.
Do not change the name of the variables.
"""

# All the symbols that the transpiler uses.
mayusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = ["'", '"', '"""', "'''"]
matrices = "$"
vectors = "[]"
embedded = "#"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}@,."
two_char_symbols = ["//", "==", "<=", ">="]

# All the data types that the transpiler uses.
FLOAT = "float"
INT = "int"
COMPLEX = "complex"
STRING = "string"
DOCSTRING = "docstring"
NULL = "none"
MATRIX = "matrix"
VECTOR = "vector"

# All the keywords that the transpiler uses.
USE, INCLUDE = "using", "include"
IMPORT, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
IF, ELIF, ELSE = "if", "elif", "else"
TRY, EXCEPT, WITH = "try", "except", "with"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
OPERATOR, RETURN = "def", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

# All the status codes that the transpiler uses.
embedding = 200
identifier = 300
eof = 400

# All extra functions that the transpiler uses. Feel free to add your own functions.
# The string special_functions is used to write these functions.
# You can use variables in it using the fstring notation.
special_functions = f"""
def iinput(prompt = '', default = ''):
	return int(input(prompt, default))

def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])
"""
