import fileinput
import glob
import string
import sys

for line in fileinput.input(glob.glob("resource/PYTHON_STANDARD/2/*.txt")):
    if fileinput.isfirstline():
        sys.stdout.write("---------- read %s ----------\n"%fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) +" "+ line + "\n")