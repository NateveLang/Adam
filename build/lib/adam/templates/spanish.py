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
