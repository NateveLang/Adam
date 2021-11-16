from nqa.file import  read_module
from nqa.lex import scanner
from nqa.syntax import parser
from nqa.semantic import generator
from nqa.error import *

import sys, subprocess, time

# Functions

driver_file = "nateve_driver"

def build(file, arg,  main = "root()", exceptions = "except:\n\tpass", driver = ""):

    start = time.time()

    module = read_module(file)
    file = file.split(".")[0]

    start_compilation = time.time()

    tokens, errors, lex_log = scanner(module, arg)
    tree, tokens, errors = parser(tokens, errors)
    errors = generator(tree, file, errors, main, exceptions)

    now = time.time()
    compilation_time = now - start_compilation

    log = lex_log

    if errors != 0:
        stat = -1
    else:
        stat = 0

    print(f"Compilation finished with status {stat}")
    
    print(log, end = "")

    if arg == "-v":
        print(tokens)
        tree.display()

    now = time.time()
    runtime = now - start
    
    f = open("nqa/nateve_vars")
    miliseconds = f.read().strip()
    f.close()
    if miliseconds == "True":
        print(f"Runtime: {1000 * runtime} miliseconds")
        print(f"Compilation time: {1000 * compilation_time} miliseconds\n")
    else:
        print(f"Runtime: {runtime} seconds")
        print(f"Compilation time: {compilation_time} seconds\n")
    
    f = open(driver_file + ".py", "w")
    f.write(driver.format(file))
    f.close()

    return file

def execute_driver():

    try:
        subprocess.call([sys.executable, "-m", driver_file])
    except:
        subprocess.call([sys.executable, "-m", driver_file + ".py"])

def get_argument(position):
    try:
        return sys.argv[position]
    except:
        return None

# Main code

params = sys.argv[:]

if len(params) >= 2:
    if len(params) >= 3:
        try:
            file = sys.argv[2]

            arg = get_argument(3)

            # Switch command
            
            command = params[1]

            if command == "set-time-unit":
                if file == "ms":
                    miliseconds = True
                elif file == "s":
                    miliseconds = False
                else:
                    miliseconds = True
                f = open("nqa/nateve_vars", "w")
                print(miliseconds, file = f)
                f.close()
            
            elif command == "build":
                file = build(file, arg)
            
            elif command == "run":
                file = build(file, arg, driver = "import {}")
                execute_driver()
            
            elif command == "compile":
                if len(params) >= 4:

                    arg2 = get_argument(4)

                    file = build(file, arg2, driver = "import {}")
                    subprocess.call([sys.executable, "-m", "PyInstaller", "--onefile", "--name", f'{arg}', f'{file}.py'])
                else:
                    ArgumentError(None, "no executable file name specified")

            elif command == "run-init-loop":
                if len(params) >= 4:

                    arg2 = get_argument(4)

                    file = build(file, arg2)
                    file2 = build(arg, arg2, driver = "import " + file + "\nwhile True:\n\timport {}")

                    execute_driver()

                else:
                    ArgumentError(None, "no loop file specified")

        except ZeroDivisionError:
            RuntimeError(None, "Error in compilation")
    else:
        FileError(None, "no file or argument specified")
else:
    ArgumentError(None, "no arguments specified")