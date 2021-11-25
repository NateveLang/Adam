try:
	from eggdriver import *
	import sys, os, subprocess
except ImportError:
	print('ImportError')


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

def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])

class example1():
	update_std()
	for i in range(2):
		print(i)
	
	install("matplotlib")
	try:
		print(2/0)
	
	except:
		print("xd")
	
	pass
try:
	example1()

except:
	pass



