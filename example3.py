try:
	from eggdriver import *
	import sys, os, subprocess
except ImportError:
	print('ImportError')


def recibe_numero(prompt = '', default = ''):
	return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
	return bool(input(prompt, default))

def actualiza_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

imprime = print
recibe = input
Matriz = Matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie

def root():
	theta=pi/3
	imprime(sen(theta),cos(theta),tan(theta))
	p=serie_sen
	imprime(p.eval(theta))
	deriva(p)
	print(p.eval(theta))
	import numpy as np
	x="hello"
	c=Matriz("""
| 1 1 2 3 4 |
| 0 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
""")
	c.display()
	a=Vector("[ 1 2 3 4 5 6 30 0 9]")
	a.display()
try:
	root()
except:
	pass

