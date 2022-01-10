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
