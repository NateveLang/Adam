author = "eanorambuena"
author_email = "eanorambuena@uc.cl"

#	MIT License
#	
#	Copyright (c) 2021 Emmanuel Norambuena Sepulveda
#	
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.

numbers = "0123456789."

def is_number(string: str):
	for char in string:
		if char not in numbers:
			return False
	
	return True

def is_numeric_list(raw_vector_content_lexema: str):
	raw_list = raw_vector_content_lexema.split(",")

	for element in raw_list:
		if not is_number(element):
			return False
		
	return True

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
