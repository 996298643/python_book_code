import fileinput
import sys

for line in fileinput.input("resource/PYTHON_STANDARD/2/sample.txt"):
    sys.stdout.write("->")
    sys.stdout.write(line)