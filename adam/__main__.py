import sys, subprocess

from adam.run import execute_driver
from adam.build import build
from adam.error import RuntimeError, FileError, ArgumentError

def get_argument(position, plural = False):

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
                file = build(file, arg)
            
            elif command == "run":
                file = build(file, args, driver = "import {}")
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

        except IndexError:
            RuntimeError(None, "Error in compilation")

    else:
        FileError(None, "no file or argument specified")

else:
    ArgumentError(None, "no arguments specified")
