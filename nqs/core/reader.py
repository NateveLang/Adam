from eggdriver.library import nqsCommands, eggConsoleCommands
from nqs.core.functions import Func, clear
from eggdriver.resources.console import sleep

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
    t = "graph=plot_histogram(counts)\n"
    t += "display(graph)\n"
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