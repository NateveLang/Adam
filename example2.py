try:
	from eggdriver import *
	import sys, os, subprocess
except ImportError:
	print('ImportError')


def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])

def root():
	theta=pi/3
	print(sin(theta),cos(theta),tan(theta))
	p=sin_serie
	print(p.eval(theta))
	derive(p)
	print(p.eval(theta))
	import numpy as np
	x="hello"
	c=Matrix("""
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

