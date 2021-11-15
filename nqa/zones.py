import nqa.grammar as gr
import sys
from nqa.error import *

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
        else:
            arrow = "↳  "
        
        print(depth * "    " + arrow + f"{self.name} ({self.type})", file = file)

        for d in self.declaration:
            if type(d) == Zone:
                d.display(depth + 1)
            else:
                print((depth + 1) * "    " + "↳  " + f"{d.symbol} ({d.ID})", file = file)

        print((depth + 1) * "    " + "↳  " + 10 * "-", file = file)

        for s in self.statements:
            if type(s) == Zone:
                s.display(depth + 1)
            else:
                print((depth + 1) * "    " + "↳  " + f"{s.symbol} ({s.ID})", file = file)