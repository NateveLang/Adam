import os

from nqs.core.kernel import compile

_driver_file = "nateve_nqs_driver"

_author = "Emmanuel Norambuena"

_required_data = None

def _build(code):
    
    f = open(_driver_file + ".nqa", "w")
    f.write(code)
    f.close()
    
    result = compile(_driver_file)

    if os.path.exists(_driver_file + ".nqa"):
        os.remove(_driver_file + ".nqa")

    return result
