from adam.assembly import *

module = Module("example4.nateve")
print(module.content)

a = Assembler("example4.nateve")
a.add_module("example5.nateve")
a.assemble()