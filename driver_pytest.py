import subprocess, sys

py = sys.executable

def build(*args):
    subprocess.run([py, "-m", "nqa", "build"] + list(args))

def compile(*args):
    subprocess.run([py, "-m", "nqa", "compile"] + list(args))

def run(*args):
    subprocess.run([py, "-m", "nqa", "run"] + list(args))