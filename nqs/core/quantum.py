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

import eggdriver as ed

T = "circuit."

def quantum(gate: str,n):
	t = ""
	global T
	N = ed.floor(n)
	n1 = str(N - 1)
	n2 = str(N)

	if len(gate) == 1:
		t = T + gate.lower() + "(" + n1 + ")\n"
	elif gate == ".---X":
		t = dualGate("X", n1, n2)
	elif gate == "X---.":
		t = dualGate("X", n2, n1)
	elif gate == ".---B1":
		t = dualGate("B1", n1, n2)
	elif gate == "B1---.":
		t = dualGate("B1", n2, n1)
	elif gate == ".---B2":
		t = dualGate("B2", n1, n2)
	elif gate=="B2---.":
		t = dualGate("B2", n2, n1)
	elif gate == ".---B3":
		t = dualGate("B3", n1, n2)
	elif gate == "B3---.":
		t = dualGate("B3", n2, n1)
	elif gate == ".---B4":
		t = dualGate("B4", n1, n2)
	elif gate == "B4---.":
		t = dualGate("B4", n2, n1)
	else:
		number = ""
		b = 0

		for i in gate:
    			
			if i != "c":
				number += i
			else:
				b = 1

		if b == 1:
			t = T + "measure(" + n1 + "," + number + ")\n"

	return t

def dualGate(type, a, b):
	global T
	
	if type == "X":
		return T + "cx(" + a + "," + b + ")\n"
	elif type == "B1":
		return T + "h(" + a + ")\n" + dualGate("X", a, b)
	elif type == "B2":
		return T + "x(" + b + ")\n" + dualGate("B1", a, b)
	elif type == "B3":
		return T + "x(" + a + ")\n" + dualGate("B1", a, b)
	elif type == "B4":
		return T + "x(" + a + ")\n" + dualGate("B2", a, b)
	