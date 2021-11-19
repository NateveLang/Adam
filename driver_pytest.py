import subprocess, sys

py = sys.executable

def build(*args):
    subprocess.run([py, "-m", "adam", "build"] + list(args))

def compile(*args):
    subprocess.run([py, "-m", "adam", "compile"] + list(args))

def run(*args):
    subprocess.run([py, "-m", "adam", "run"] + list(args))
