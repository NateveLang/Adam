from nqa.file import  read_module
from nqa.lex import scanner
from nqa.syntax import parser
from nqa.semantic import generator
from nqa.error import *

import sys, subprocess, time

# Functions

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
    
    f = open("nqa/nqa_vars")
    miliseconds = f.read().strip()
    f.close()
    if miliseconds == "True":
        print(f"Runtime: {1000 * runtime} miliseconds")
        print(f"Compilation time: {1000 * compilation_time} miliseconds\n")
    else:
        print(f"Runtime: {runtime} seconds")
        print(f"Compilation time: {compilation_time} seconds\n")
    
    f = open("nqa_driver.py", "w")
    f.write(driver.format(file))
    f.close()

    return file

# Main code

params = sys.argv[:]

if len(params) >= 2:
    if len(params) >= 3:
        try:
            file = sys.argv[2]

            if len(params) == 3:
                arg = None
            elif len(params) >= 4:
                arg = sys.argv[3]

            # Switch command
            
            command = params[1]

            if command == "set-time-unit":
                if file == "ms":
                    miliseconds = True
                elif file == "s":
                    miliseconds = False
                else:
                    miliseconds = True
                f = open("nqa/nqa_vars", "w")
                print(miliseconds, file=f)
                f.close()
            
            elif command == "build":
                file = build(file, arg)
            
            elif command == "run":
                file = build(file, arg, driver = "import {}")
                try:
                    subprocess.call(["py", "-m", "nqa_driver"])
                except:
                    subprocess.call(["py", "-m", "nqa_driver.py"])
            
            elif command == "compile":
                if len(params) >= 4:
                    if len(params) == 4:
                        arg2 = None
                    elif len(params) >= 5:
                        arg2 = sys.argv[4]

                    file = build(file, arg2, driver = "import {}")
                    subprocess.call(["py", "-m", "PyInstaller", "--onefile", "--name", f'{arg}', f'{file}.py'])
                else:
                    ArgumentError(None, "no executable file name specified")

            elif command == "run-init-loop":
                if len(params) >= 4:
                    if len(params) == 4:
                        arg2 = None
                    elif len(params) >= 5:
                        arg2 = sys.argv[4]

                    file = build(file, arg2)
                    file2 = build(arg, arg2, driver = "import " + file + "\nwhile True:\n\timport {}")

                    try:
                        subprocess.call(["py", "-m", "nqa_driver"])
                    except:
                        subprocess.call(["py", "-m", "nqa_driver.py"])
                else:
                    ArgumentError(None, "no loop file specified")

        except:
            RuntimeError("Error in compilation")
    else:
        FileError(None, "no file or argument specified")
else:
    ArgumentError(None, "no arguments specified")