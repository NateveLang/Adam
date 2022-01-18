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

transpiler_name = "adam"

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

FLOAT = "flottant"
INT = "entier"
COMPLEX = "complexe"
STRING = "chaine"
DOCSTRING = "docchaine"
NULL = "nul"
MATRIX = "matrix"
VECTOR = "vector"

USE, INCLUDE = "utiliser", "inclure"
IMPORT, FROM, AS, PASS, IN = "inclure", "de", "comme", "passer", "dans"
IF, ELIF, ELSE = "si", "sinon", "defaut"
TRY, EXCEPT, WITH = "tenter", "except", "avec" 
WHILE, FOR, BREAK, CONTINUE = "tantque", "pour", "sauter", "continuer"
OPERATOR, RETURN = "definir", "retourner"
CLASS, SELF = "classe", "self"
AND, OR, NOT, TRUE, FALSE = "et", "ou", "non", "vrai", "faux"

embedding = 200
identifier = 300
eof = 400

traductions = """
imprimer = print
entree = input

serie_sin = sin_serie
serie_cos = cos_serie
"""

special_functions = f"""
def eentree(prompt = '', default = ''):
	return int(input(prompt, default))

def nentree(prompt = '', default = ''):
\treturn float(input(prompt, default))

def bentree(prompt = '', default = ''):
\treturn bool(input(prompt, default))

def reactualiser_std():
\tsubprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])
""" + traductions
