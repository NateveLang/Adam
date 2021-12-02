"""
__main__.py

The entry point of the program. It drives the program, and allows to
use the program in console.
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

import sys

from adam.assembly import   Assembler
from adam.error import      ArgumentError, FileError, RuntimeError
from adam.run import        execute_driver

def get_argument(position, plural = False):
    """
Get an argument from command line, with a specific position.
You can get more than one argument, if you set 'plural' to True.

It receives the following arguments:
    position: The position of the argument in the command line.
    plural:   If you want to get more than one argument, set it to True.
"""

    if plural:

        try:
            return sys.argv[position:]
        except:
            return ["none"]

    try:
        return sys.argv[position]
    except:
        return "none"

# Main code

params = sys.argv[:]

if len(params) >= 2:

    if len(params) >= 3:

        try:
            file = sys.argv[2]

            arg = get_argument(3)
            args = get_argument(3, True)

            # Switch command
            
            command = params[1]

            if command == "set-time-unit":

                if file == "ms":
                    miliseconds = True
                elif file == "s":
                    miliseconds = False
                else:
                    miliseconds = True

                f = open("adam/nateve_vars", "w")
                print(miliseconds, file = f)
                f.close()
            
            elif command == "build":
                assembler = Assembler(file, [arg])
                assembler.assemble()
            
            elif command == "run":
                assembler = Assembler(file, [arg])
                assembler.run()
            
            elif command == "compile":

                if len(params) >= 4:

                    arg2 = get_argument(4)

                    assembler = Assembler(file, [arg2])
                    assembler.compile(arg)
                
                else:
                    ArgumentError(None, "no executable file name specified")

            elif command == "run-init-loop":

                if len(params) >= 4:

                    arg2 = get_argument(4)
                    """
                    file, modules = build(file, arg2)
                    file2, modules = build(arg, arg2, driver = "import " + file + "\nwhile True:\n\timport {}")
                    """
                    execute_driver()

                else:
                    ArgumentError(None, "no loop file specified")

        except IndexError:
            RuntimeError(None, "Error in compilation")

    else:
        FileError(None, "no file or argument specified")

else:
    ArgumentError(None, "no arguments specified")
