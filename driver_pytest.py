import subprocess

def build(*args):
    subprocess.call(["py", "-m", "nqa", "build"] + list(args))

def compile(*args):
    subprocess.call(["py", "-m", "nqa", "compile"] + list(args))

def run(*args):
    subprocess.call(["py", "-m", "nqa", "run"] + list(args))