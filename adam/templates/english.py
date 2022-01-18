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
