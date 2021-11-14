mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = "\"\'"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}#$@,."
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "decimal"
INT = "entero"
COMPLEX = "complejo"
STRING = "cadena"
NULL = "nada"

USE, INSTALL, WAIT = "usa", "instala", "espera"
INCLUDE, FROM, AS, PASS, IN = "importa", "desde", "como", "pasa", "en"
IF, ELIF, ELSE = "si", "sino", "sifalso"
WHILE, FOR, BREAK, CONTINUE = "mientras", "para", "rompe", "sigue"
OPERATOR, RETURN = "define", "retorna"
CLASS, SELF = "clase", "esto"
AND, OR, NOT, TRUE, FALSE = "y", "o", "no", "verdadero", "falso"

identifier = 300
eof = 400

