import subprocess, sys

from adam.assembly import Assembler

py = sys.executable

def build(*args):
    try:
        assembler = Assembler(args[0])
        assembler.assemble()
        return True
    except:
        return False

def compile(*args):
    try:
        assembler = Assembler(args[0])
        assembler.compile(args[1])
        return True
    except:
        return False

def run(*args):
    try:
        assembler = Assembler(args[0])
        assembler.run()
        return True
    except:
        return False
