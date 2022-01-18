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

from eggdriver.resources.console    import display, get, sleep
from eggdriver.resources.constants  import *
from eggdriver.resources.extensions import nqa

from nqs.core.kernel import   compile
from nqs.developer.run import run

def developerDisplay(name: str):
    content = nqa.read(name)
    display(content)

def developerConsole(condition: bool = True):
  print(white + "Developer Console is now running")
  while condition:
    i = get("nqs")
    name = "temp_compile"
    if i == "$display":
      content = nqa.read(name)
      print(white + content)
    elif i == "$compile":
      compile(name)
    elif i == "$save":
      print(white + "Save as:")
      adress = get("nqs")
      content = nqa.read(name)
      nqa.write(content, adress)
    elif i == "$run":
      run(name)
    elif i == "$delay":
      print(white + "How many milliseconds?")
      delta = get("nqs")
      sleep(int(delta))
    elif i == "$end":
      try:
        nqa.delete(name)
      except:
        pass
      print(white + "Developer Console stopped running")
      return "done"
    else:
    	nqa.append(i + "\n", name)