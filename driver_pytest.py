import subprocess

def build(*args):
    subprocess.call(["py", "-m", "nqa", "build"] + args)

def compile(*args):
    subprocess.call(["py", "-m", "nqa", "compile"] + args)

def run(*args):
    subprocess.call(["py", "-m", "nqa", "run"] + args)