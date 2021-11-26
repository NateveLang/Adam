def Error(line = None, message = "", type = ""):
    
    if line != None:
        print(f"{type}Error in line {line}: {message}")
    else:
        print(f"{type}Error: {message}")

    return 1

def LexicalError(line, message):
    return Error(line, message, "Lexical")

def SyntaxError(line, message):
    return Error(line, message, "Syntax")

def ArgumentError(line, message):
    return Error(line, message, "Argument")

def FileError(line, message):
    return Error(line, message, "File")

def ZoneError(line, message):
    return Error(line, message, "Zone")

def SemanticError(line, message):
    return Error(line, message, "Semantic")

def DeclarationError(line, message):
    return Error(line, message, "Declaration")

def RuntimeError(line, message):
    return Error(line, message, "Runtime")

def NotFoundError(line, message):
    return Error(line, message, "NotFound")

def ValueError(line, message):
	return Error(line, message, "Value")

def TemplateNotFoundError(line, message):
    return Error(line, message, "TemplateNotFound")
