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
	print("",end="")
	from user.index import Index
	from qiskit import QuantumCircuit, execute, Aer
	from qiskit.visualization import plot_histogram
	circuit = QuantumCircuit(2,2)
	circuit.x(1)
	circuit.h(-1)
	circuit.cx(-1,0)
	circuit.measure(-1,1)
	s=1024
	backend=Aer.get_backend('qasm_simulator')
	job=execute(circuit, backend, shots=s)
	result=job.result()
	counts=result.get_counts(circuit)
	plot_histogram(counts)
	circuit.draw('mpl')
	

	sleep(1000)
	pass
	print("",end="")
try:
	example7()

except:
	pass



