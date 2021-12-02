"""
build.py

This module is responsible for building the source code.

It contains the following functions:
    build: builds the source code.
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

import time

from adam.file import       read_module
from adam.lex import        scanner
from adam.run import        driver_file
from adam.semantic import   generator
from adam.syntax import     parser

vars_file = "adam/nateve_vars"

def build(file, args = ["none"],  main = "", exceptions = "\tpass", driver = ""):
    """
This function builds the source code.

It takes the following arguments:
    file: the name of the file to be built.
    args: the arguments used to build the source code.
    main: the main argument passed to the generator.
    exceptions: the exceptions argument passed to the generator.
    driver: the driver used to format the generated code.
"""

    dev_mode = "dev" in args
    verbose_mode = ("-v" in args) or ("--verbose" in args)
    display_status_mode = verbose_mode or dev_mode

    start = time.time()

    text = read_module(file)
    file = file.split(".")[0]

    if text == None:
        text = ""

    start_compilation = time.time()

    tokens, errors, lex_log, templates, modules = scanner(text, args)
    tree, tokens, errors = parser(tokens, file, errors)
    errors = generator(tree, file, errors, main, exceptions, args, templates)

    if display_status_mode:
        now = time.time()
        compilation_time = now - start_compilation

        log = lex_log

        if errors != 0:
            stat = -1
            
        else:
            stat = 0

        print(f"Compilation finished with status {stat}")
        
        print(log, end = "")

    if dev_mode:
        print(tokens)
        tree.display()

    if display_status_mode:
        now = time.time()
        runtime = now - start
    
        try:
            f = open(vars_file)
            miliseconds = f.read().strip()
            f.close()

        except:
            miliseconds = "True"

        if miliseconds == "True":
            print(f"Machine time: {1000 * runtime} miliseconds")
            print(f"Compilation time: {1000 * compilation_time} miliseconds\n")

        else:
            print(f"Machine time: {runtime} seconds")
            print(f"Compilation time: {compilation_time} seconds\n")
    
    f = open(driver_file + ".py", "w")
    f.write(driver.format(file))
    f.close()

    return file, modules
