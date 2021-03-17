# I am using the module for the sole purpose of
# saving the file to the program directory.
import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# dir = os.path.abspath(__file__)[:-8]
# Create an absolute path to the file.
filename = 'next_generation.txt'

with open(filename, "w") as f:
            for i in range(2000, 2042, 10):
                f.write(str(i) + "\n")