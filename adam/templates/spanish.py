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
one_char_symbols = "+-*/%=<>()[]{}@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "decimal"
INT = "entero"
COMPLEX = "complejo"
STRING = "cadena"
DOCSTRING = "documentacion"
NULL = "nada"
MATRIX = "matriz"
VECTOR = "vector"

USE, INCLUDE = "usando", "incluye"
IMPORT, FROM, AS, PASS, IN = "importa", "desde", "como", "pasa", "en"
IF, ELIF, ELSE = "si", "sino", "delocontrario"
TRY, EXCEPT, WITH = "intenta", "excepto", "con"
WHILE, FOR, BREAK, CONTINUE = "mientras", "para", "rompe", "sigue"
OPERATOR, RETURN = "define", "retorna"
CLASS, SELF = "clase", "esto"
AND, OR, NOT, TRUE, FALSE = "y", "o", "no", "verdadero", "falso"

embedding = 200
identifier = 300
eof = 400

traducciones = """
imprime = print
recibe = input
matriz = matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie
"""

special_functions = """
def recibe_entero(prompt = '', default = ''):
	return int(input(prompt, default))

def recibe_numero(prompt = '', default = ''):
    return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
    return bool(input(prompt, default))

def actualiza_std():
    subprocess.call(["py", "-m", "pip", "install", "eggdriver"])
""" + traducciones
