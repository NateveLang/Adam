import subprocess, sys

py = sys.executable

def build(*args):
    subprocess.run([py, "-m", "adam", "build"] + list(args))

def compile(*args):
    subprocess.run([py, "-m", "adam", "compile"] + list(args))

def run(*args):
    subprocess.run([py, "-m", "adam", "run"] + list(args))

"""
py -m PyInstaller --onefile --name Adam C:\Users\Alumno\Adam\adam\__main__.py
"""