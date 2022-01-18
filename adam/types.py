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

from eggdriver import Matrix, Vector

from adam.error import ValueError
	
class vector(Vector):
	"""x = vector("[1 2 3]") -> vector

Convert a number, polynomial, matrix, vector, or string to a vector.
If x is a number, return [x]

Eg:
input:				output:
y = [3, 5]			[3 5]
print(y)
"""

	def __init__(self, *args):
		super().__init__(*args)

class matrix(Matrix):
	"""x = matrix('''
| 1 0 |
| 2 3 |
''') -> matrix

Convert a number, polynomial, matrix, vector, or string to a matrix.
If [x y] is a vector, return
| x |
| y |

Eg:
input:		  		output:
y = $		  		| 1 0 |
|1 0|				| 2 3 |
|0 1|
$
print(y)
"""

	def __init__(self, *args):
		args = list(args)

		if type(args[0]) == str:
			args[0] = args[0].strip("\n")

		super().__init__(*args)

	def dot(self, b):
		import numpy as np
		a = np.array(self)
		b2 = np.array(b)
		c = a @ b2
		temp =[]

		for i in c:
			temp.append(vector(i))
		
		return matrix(temp)
	
	def plus(self, b):
			
		if self.n != b.n or self.m != b.m:
			ValueError(None, "Matrices must be of equal dimensions to add")
			return None

		temp = []

		for i in range(len(self)):
			u = vector(self[i])
			v = vector(b[i])
			temp.append(u.plus(v))
			
		return matrix(temp)

	def __str__(self):
		self.display()
		return ""
