import subprocess, sys

driver_file = "nateve_driver"

def execute_driver():
    
    try:
        subprocess.call([sys.executable, "-m", driver_file])
    except:
        subprocess.call([sys.executable, "-m", driver_file + ".py"])
