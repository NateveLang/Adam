from eggdriver.resources.extensions import py

from nqs.core.kernel import compile

def write(name: str):
	T = compile(name)
	py.write(T, name)