try:
	import eggdriver as std
	import sys
except ImportError:
	print('ImportError')

def root():
	for i in range(2):
		print(i)
	
	try:
		print(2/0)
	
	except:
		print('xd')
	
try:
	root()
except:
	pass

