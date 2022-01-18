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

import  sys

from    adam.error import   ZoneError
import  adam.grammar as     gr

class Zone():
    def __init__(self, name: str, line: int, type: str = "auto", parent = None):
        self.name = name
        self.line = line
        self.relative_line = line
        self.parent = parent

        if type == "auto":

            if name in gr.conditionals:
                self.type = "conditional"
            elif name in [gr.WHILE, gr.FOR]:
                self.type = "loop"
            elif name == "root":
                self.type = "root"
            else:
                ZoneError(line, f"Unknown zone type for zone '{name}'")
            
        else:
            self.type = type
        
        self.declaration = []
        self.statements = []

    def display(self, depth = 0, file = sys.stdout):
        
        if self.name == "root":
            arrow = ""

        elif file != sys.stdout:
            arrow = "->  " # Because python files do not support ↳ character

        else:
            arrow = "↳  " 
        
        print(depth * "    " + arrow + f"{self.name} ({self.type})", file = file)

        for d in self.declaration:

            if type(d) == Zone:
                d.display(depth + 1)
            else:
                print((depth + 1) * "    " + arrow + f"{d.symbol} ({d.ID})", file = file)

        print((depth + 1) * "    " + arrow + 10 * "-", file = file)

        for s in self.statements:

            if type(s) == Zone:
                s.display(depth + 1)
            else:
                print((depth + 1) * "    " + arrow + f"{s.symbol} ({s.ID})", file = file)
                