from nqs.core.kernel import compile
from eggdriver.resources.extensions import py

def write(name: str):
	T = compile(name)
	py.write(T, name)