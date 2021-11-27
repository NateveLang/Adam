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

class example7():
	from user.index import Index
	

	print([ 2,3 ])matrix("""
~.nqa file code~

q0  q1
    X
H
.---X
c1
host qasm_simulator
""".replace('nqa', str(nqa)).replace('file', str(file)).replace('code', str(code)).replace('q0', str(q0)).replace('q1', str(q1)).replace('X', str(X)).replace('H', str(H)).replace('X', str(X)).replace('c1', str(c1)).replace('host', str(host)).replace('qasm_simulator', str(qasm_simulator)))
try:
	example7()

except:
	pass



