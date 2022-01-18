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

from eggdriver.library import   eggConsoleCommands, nqsCommands
from eggdriver.resources import sleep

from nqs.core.functions import clear, Func

def settings(command: str, param):
  t = ""
  if command == "host":
    t = "s=1024\nbackend=Aer.get_backend('" + param + "')\n"
    t += "job=execute(circuit, backend, shots=s)\n"
    t += "result=job.result()\n"
    t += "counts=result.get_counts(circuit)\n"
  elif command == "shots":
    t = "s=" + param
  elif command == "hist":
    t = "plot_histogram(counts)\n"
  elif command == "draw":
    t = "circuit.draw('mpl')\n"
  elif command == "inject":
    t = param+"\n"
  elif command == "function":
    p = Parameter(param)
    if p.name in nqsCommands or p.name in eggConsoleCommands:
      print("Error: " + p.name + " is protected.")
      return t
    f = Func(p.name, p.params, p.actions, "user/index", "user/definitions")
    f.add()
  elif command == "clear":
    clear(param)
  elif command == "delay":
    sleep(int(param))
  else:
    params = param.split(",")
    t = executeFunction(command, params)
  return t

class Parameter():
  def __init__(self, param: str):
    arr = param.split("|")
    self.name = arr[0]
    paramsBeforeSplit = arr[1]
    self.params = paramsBeforeSplit.split(",")
    actionsBeforeSplit = arr[2]
    self.actions = actionsBeforeSplit.split(",")

def executeFunction(command, params):
  t = "try:\n"
  t += "\tIndex[\""+command+"\"]("
  last = params[-1]
  params.pop()
  for i in params:
    t += "\"" + i + "\","
  t += "\"" + last + "\")\n"
  t += "except:\n"
  t += "\tprint(\"Error: " + command + " is not defined or is inaccessible\")\n"
  return t