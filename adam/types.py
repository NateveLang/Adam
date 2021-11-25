from eggdriver import Vector, Matrix
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
		a = int(2)

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
