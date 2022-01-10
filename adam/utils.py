def tokenize(lexemas):
	tokens = []

	for i in range(len(lexemas)):
		tokens.append([lexemas[i], i])
		
	return tokens

def tolist(string):
	arr = []

	for i in string:
		arr.append(i)

	return arr

def tostring(array, separator = ""):
	s = ""

	if type(array) == tuple:
		array = list(array)

	elif type(array) not in [list, tuple]:
		array = [str(array)]
		
	for i in range(len(array)):
		s += array[i]

		if i != len(array) - 1:
			s += separator

	return s
