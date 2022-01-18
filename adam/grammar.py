author = "eanorambuena"
author_email = "eanorambuena@uc.cl"

#	MIT License
#	
#	Copyright (c) 2021 Emmanuel Norambuena Sepulveda
#	
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.

from adam.utils import tokenize, tolist

transpiler_name = "adam"

mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
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
one_char_symbols = "+-*/%=<>(){}@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "float"
INT = "int"
COMPLEX = "complex"
STRING = "string"
DOCSTRING = "docstring"
NULL = "none"
MATRIX = "matrix"
VECTOR = "vector"

USE, INCLUDE = "using", "include"
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
"""

preprocess = [USE, INCLUDE]
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

embedding = 200
identifier = 300
eof = 400
codes = [embedding, identifier, eof]

ALL = primitives + codes + protected_IDs
