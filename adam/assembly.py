import math, os, subprocess, sys

from adam.build import build
from adam.run import execute_driver, driver_file

class Module():
    
    def __init__(self, name, args = ["none"]):
        self.name = name

        file_name, self.modules_names = build(name, args, driver = "import {}")
        file = open(file_name + ".py", "r")

        self.content = file.read() + "\n"

        file.close()

    def __str__(self):
        return f"Module {self.name}"

class Assembler():

    def __init__(self, root_module, args = ["none"]):
        self.root = root_module
        self.modules = []
        self.args = args
        self.add_module(self.root)

    def add_module(self, module_name):
        module = Module(module_name, self.args)
        self.modules.append(module)

        for module_name in module.modules_names:
            self.add_module(module_name)

    def __str__(self):
        result = ""

        for module in self.modules:
            result += module.__str__() + "\n"

        return result

    def assemble(self):
        file = open(driver_file + ".py", "w")
        
        text = ""

        n = math.floor(len(self.modules) / 2)

        for i in range(n):
            temp = self.modules[i]
            self.modules[i] = self.modules[-(i + 1)]
            self.modules[-(i + 1)] = temp

        for module in self.modules:
            text += module.content + "\n"
        
        file.write(text)

        file.close()

    def compile(self, name):
        self.assemble()
        subprocess.call([sys.executable, "-m", "PyInstaller", "--onefile", "--name", f'{name}', f'{self.file}.py'])

    def run(self):
        self.assemble()
        execute_driver()

        if os.path.exists(driver_file + ".py"):
            os.remove(driver_file + ".py")
    