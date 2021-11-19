from adam.utils import tolist, tokenize

from adam.templates.spanish import *

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

codes = [identifier, eof]

ALL = primitives + codes + protected_IDs