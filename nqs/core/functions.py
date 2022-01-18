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

from eggdriver.resources.extensions import py

class Func():
			
	def __init__(self, name: str, params, actions, index_file: str, definitions_file: str):
		self.name = name
		self.params = params
		self.actions = actions
		self.indexfile = index_file
		self.definitionsfile = definitions_file

	def index(self):
		lines = py.read(self.indexfile).split("\n")
		lines.pop()
		newline = f"\'{self.name}\': Definition.{self.name}, "
		lines.append(newline)
		lines.append("}")
		text = ""

		for i in lines:
			text += i + "\n"

		py.write(text, self.indexfile)

	def define(self):
		T = "\tdef {self.name}("
		last = self.params[-1]
		j = self.params
		j.pop()

		for i in j:
			T += i + ","

		T += last + "):\n"

		for i in self.actions:
			T += "\t\t{i}\n"

		py.append(T, self.definitionsfile)

	def add(self):
		self.define()
		self.index()

def clear(param: str):

	if param == "all":
		t1 = "from user.definitions import Definition\n"
		t1 += "Index = { \n"
		t1 += "\'__init__\': Definition.__init__,  # Do not remove this function, Index must not be void\n"
		t1 += "}\n"
		py.write(t1, "user/index")
		
		t2 = "class Definition():\n"
		t2 += "\tdef __init__(): # Do not remove this function, Definition must not be void\n"
		t2 += "\t\treturn \"done\""
		py.write(t2, "user/definitions")
