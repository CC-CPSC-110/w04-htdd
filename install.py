import subprocess
import sys

def install(package: str, *args) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, *args])

install("dataclasses")
