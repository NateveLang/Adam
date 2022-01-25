
try:
    from eggdriver import *
except ImportError:
    print('ImportError: Failing to import eggdriver')

try:
    from adam.types import *
except ImportError:
    print('ImportError: Failing to import adam.types')

try:
    import sys
except ImportError:
    print('ImportError: Failing to import sys')

try:
    import os
except ImportError:
    print('ImportError: Failing to import os')

try:
    import subprocess
except ImportError:
    print('ImportError: Failing to import subprocess')

def iinput(prompt = '', default = ''):
	return int(input(prompt, default))

def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

class example01():
	print("",end="")
	update_std()
	for i in range(2):
		print(i)
	
	install("matplotlib")
	try:
		print(2/0)
	
	except:
		print("xd")
	
	pass
	print("",end="")
example01()




def iinput(prompt = '', default = ''):
	return int(input(prompt, default))

def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

class example01():
	print("",end="")
	update_std()
	for i in range(2):
		print(i)
	
	install("matplotlib")
	try:
		print(2/0)
	
	except:
		print("xd")
	
	pass
	print("",end="")
example01()



