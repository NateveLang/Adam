from adam.build import build
from adam.run import driver_file

assembler_file = "nateve_assembler.py"

class Assembler():

    def __init__(self, root_module):
        self.root = root_module
        self.modules = []

    def add_module(self, module_name):
        self.modules.append(module_name)

    def assemble(self):
        file = open(driver_file, "a")
        
        for module_name in self.modules:
            m = Module(module_name)
            text = m.content + "file_name = root\n"
            file.write(text)

        file.close()

class Module():

    def __init__(self, name):
        self.name = name

        file_name = build(name, "none", driver = "import {}")
        file = open(file_name, "r")

        self.content = file.read() + "\n"

        file.close()
