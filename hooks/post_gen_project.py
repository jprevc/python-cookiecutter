import sys
import subprocess
import pathlib

subprocess.check_call([sys.executable, "-m", "venv", "venv"])

venv_python_path = pathlib.Path("venv") / "Scripts" / "python.exe"
subprocess.check_call([str(venv_python_path), "-m", "pip", "install", "-e", ".[dev]"])
