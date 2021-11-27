from nqs.core.kernel import compile

_author = "Emmanuel Norambuena"

_required_data = None

def _build(code):
    text = code.symbol
    
    f = open("nateve_nqs_driver.nqa", "w")
    f.write(text)
    f.close()

    return compile("nateve_nqs_driver")
