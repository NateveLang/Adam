try:
	from eggdriver import *
	import sys, os
except ImportError:
	print('ImportError')


def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

def root():
	update_std()
	for i in range(2):
		print(i)
	
	install('matplotlib')
	try:
		print(2/0)
	
	except:
		print('xd')
	
try:
	root()
except:
	pass

