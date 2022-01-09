from eggdriver.resources.extensions import py

from nqs.developer.write import write

def run(name: str):
    write(name)
    py.execute(name)