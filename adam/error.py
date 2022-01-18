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

def Error(line = None, message = "", type = ""):
    
    if line != None:
        print(f"{type}Error in line {line}: {message}")
    else:
        print(f"{type}Error: {message}")

    return 1

def ArgumentError(line, message):
    return Error(line, message, "Argument")

def DeclarationError(line, message):
    return Error(line, message, "Declaration")

def FileError(line, message):
    return Error(line, message, "File")

def LexicalError(line, message):
    return Error(line, message, "Lexical")

def NotFoundError(line, message):
    return Error(line, message, "NotFound")

def NotSupportedLanguageError(line, message):
    return Error(line, message, "NotSupportedLanguage")

def RuntimeError(line, message):
    return Error(line, message, "Runtime")

def SemanticError(line, message):
    return Error(line, message, "Semantic")

def SyntaxError(line, message):
    return Error(line, message, "Syntax")

def TemplateNotFoundError(line, message):
    return Error(line, message, "TemplateNotFound")

def ValueError(line, message):
    return Error(line, message, "Value")

def ZoneError(line, message):
    return Error(line, message, "Zone")
