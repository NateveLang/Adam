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
