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
