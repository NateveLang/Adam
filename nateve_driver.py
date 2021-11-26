try:
	from eggdriver import *
	from adam.types import *
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


def recibe_numero(prompt = '', default = ''):
	return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
	return bool(input(prompt, default))

def actualiza_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

imprime = print
recibe = input
matriz = matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie


def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])


def nentree(prompt = '', default = ''):
	return float(input(prompt, default))

def bentree(prompt = '', default = ''):
	return bool(input(prompt, default))

def reactualiser_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def inclure(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])

imprimer = print
entree = input

serie_sin = sin_serie
serie_cos = cos_serie

class example4():
	amo_Nateve=True
	if amo_Nateve==True:
		imprime("Yo amo Nateve!")
	
	else:
		imprime("Odio Nateve :c")
	
	if 1<3:
		print("Try Nateve!")
	
	else:
		print("NO")
	
	v="Bonjour"
	imprimer(v,"Nateve!")
	pass
try:
	example4()

except:
	pass



try:
	from eggdriver import *
	from adam.types import *
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


def recibe_numero(prompt = '', default = ''):
	return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
	return bool(input(prompt, default))

def actualiza_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

imprime = print
recibe = input
matriz = matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie

class example5():
	imprime("Nateve example 5")
	pass
try:
	example5()

except:
	pass



try:
	from eggdriver import *
	from adam.types import *
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


def recibe_numero(prompt = '', default = ''):
	return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
	return bool(input(prompt, default))

def actualiza_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

imprime = print
recibe = input
matriz = matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie


def nentree(prompt = '', default = ''):
	return float(input(prompt, default))

def bentree(prompt = '', default = ''):
	return bool(input(prompt, default))

def reactualiser_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def inclure(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])

imprimer = print
entree = input

serie_sin = sin_serie
serie_cos = cos_serie

class example6():
	a=matrix("""
| 1 5 |
| 0 2 |
""")
	b=matrix("""
|0 1|
|1 0|
""")
	imprime("a = ")
	imprime(a)
	imprime("b = ")
	imprime(b)
	c=a.dot(b)
	imprime("a * b =")
	imprime(c)
	imprime("a + b =")
	print(a.plus(b))
	d=vector([1, 2, 3, 4, 5])
	imprime(d)
	e=vector([0, 1, 0, 1, 0])
	imprime(e)
	f=d.dot(e)
	imprime(f)
	g=d.plus(e)
	imprime(g)
	def r(x,y,z):
		return matrix("""
|x|
|y|
|z|
""".replace('x', str(x)).replace('y', str(y)).replace('z', str(z)))
	
	x,y,z=1,5,3
	j=r(x,y,z)
	imprimer(j)
	k=matrix("""
|2 0 0|
|0 2 0|
|0 0 2|
""")
	imprimer(k.dot(j))
	pass
try:
	example6()

except:
	pass



