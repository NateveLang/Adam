"""
assembly.py

This module contains the following classes:
    Assembler
        This class is used to assemble the Nateve source code into a final python file.
    Module
        This class is used to represent a module in the assembly process.
"""

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

import math, os, subprocess, sys

from adam.build import build
from adam.run import execute_driver, driver_file

class Assembler():
    """
This class is used to assemble the Nateve source code into a final python file.

It has the following attributes:
    root: The name of the root module.
    modules: The modules to be assembled.
    args: The arguments to be passed to the modules.

It has the following methods:
    add_module: This method is used to add a module to the assembly process.
    assemble: This method is used to assemble the modules into a final python file.
    compile: This method is used to compile the root module into an executable.
    run: This method is used to run the root module.
"""

    def __init__(self, root_module, args = ["none"]):
        """
This method is used to initialize the Assembler class.
It takes the following arguments:
    root_module: The name of the root module.
    args: The arguments to be passed to the root module.    
"""
    
        self.root = root_module
        self.modules = []
        self.args = args
        self.add_module(self.root)

    def add_module(self, module_name):
        """
This method is used to add a module to the assembly process.
It takes the following arguments:
    module_name: The name of the module to be added.
"""
    
        self.modules.append(Module(module_name))

        module = Module(module_name, self.args)
        self.modules.append(module)

        for module_name in module.modules_names:
            self.add_module(module_name)

    def __str__(self):
        """
This method returns a string representation of the Assembler class.
"""

        result = ""

        for module in self.modules:
            result += module.__str__() + "\n"

        return result

    def assemble(self):
        """
This method is used to assemble the modules into a final python file.
"""
    
        file = open(driver_file + ".py", "w")
        
        text = ""

        n = math.floor(len(self.modules) / 2)

        for i in range(n):
            temp = self.modules[i]
            self.modules[i] = self.modules[-(i + 1)]
            self.modules[-(i + 1)] = temp

        for module in self.modules:
            text += module.content + "\n"

        n_text = math.floor(len(text) / 2) # Skip modules double-counting 
        
        file.write(text[:n_text])

        file.close()

    def compile(self, name):
        """
This method is used to compile the root module into an executable.
It takes the following arguments:
    name: The name of the executable.
"""
    
        build(name)

        self.assemble()
        subprocess.call([sys.executable, "-m", "PyInstaller", "--onefile", "--name", f'{name}', f'{self.file}.py'])

    def run(self):
        """
This method is used to run the root module.
"""

        self.assemble()
        execute_driver()

        if os.path.exists(driver_file + ".py"):
            os.remove(driver_file + ".py")

class Module():
    """
This class is used to represent a module in the assembly process.

It has the following attributes:
    name: The name of the module.
    modules_names: The names of the modules imported by the module.
    content: The content of the module.
"""
    def __init__(self, name, args = ["none"]):
        """
This method is used to initialize the Module class.

It takes the following arguments:
    name: The name of the module.
    args: The arguments to be passed to the module.
"""

        self.name = name

        file_name, self.modules_names = build(name, args, driver = "import {}")
        file = open(file_name + ".py", "r")

        self.content = file.read() + "\n"

        file.close()

    def __str__(self):
        """
This method returns a string representation of the Module class.
"""

        return f"Module {self.name}"

