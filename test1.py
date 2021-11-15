try:
	import eggdriver as std
	import sys
except ImportError:
	print('ImportError')

def root():
	for i in range(2):
		print(i)
	
	server=std.Server()
	server.ngrok()
	try:
		print(2/0)
	
	except:
		print('xd')
	
try:
	root()
except:
	pass

