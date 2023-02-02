import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


checkImports = False
while not checkImports:
    try:
        # paste here your imports, ex. import pandas
        import pandas

        checkImports = True
    except ImportError:
        # paste here your install libraries function if they not exist, ex. install('pandas')
        install('pandas')

# paste here your code
