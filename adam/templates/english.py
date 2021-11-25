transpiler_name = "adam"

mayusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = ["'", '"', '"""', "'''"]
matrices = "$"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}#@,."
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

identifier = 300
eof = 400

types = """
class vector(Vector):
	def __init__(self, *args):
		super().__init__(*args)

class matrix(Matrix):
	def __init__(self, *args):
		super().__init__(*args)
	def times(self, b):
		import numpy as np
		a = np.array(self)
		b2 = np.array(b)
		c = a @ b2
		temp =[]
		for i in c:
			temp.append(vector(i))
		return matrix(temp)
	def __str__(self):
		self.display()
		return ""
"""

special_functions = types + f"""
def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', '{transpiler_name}', 'build', file])
"""
