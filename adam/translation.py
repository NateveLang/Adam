import adam.grammar as gr
from adam.error import NotFoundError
from adam.token import get_token_ID

def translate(lexema, errors, tp):

    if get_token_ID(lexema, tp) == tp.identifier:
        return lexema, errors

    elif lexema in tp.protected:
        index = tp.protected.index(lexema)
        return gr.protected[index], errors

    else:
        errors += NotFoundError(None, "Not found name: " + lexema)
        return "404", errors
