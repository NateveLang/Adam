import nqs

_author = "Emmanuel Norambuena"

_required_data = None

def _build(code):
    text = code.symbol

    f = open("nateve_nqs_driver.nqa", "w")
    f.write(text)
    f.close()
    return nqs.compile("nateve_nqs_driver")
