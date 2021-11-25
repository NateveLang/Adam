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
		print("YES")
	
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
Matriz = Matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie

class example5():
	print("a")
	imprime("Hola")
	pass
try:
	example5()

except:
	pass



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

class example6():
	imprime("Nateve example 6")
	m=Matrix("""
| 1 0 |
| 0 1 |
""")
	m.display()
	pass
try:
	example6()

except:
	pass



