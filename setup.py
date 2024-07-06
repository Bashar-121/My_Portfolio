import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import google.generativeai
except ImportError:
    install("google-generativeai")
