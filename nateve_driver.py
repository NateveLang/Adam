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


def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

class main():
	print("",end="")
	with 3 as a:
		print(a+4)
	
	pass
	print("",end="")
try:
	main()

except:
	pass



