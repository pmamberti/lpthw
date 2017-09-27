from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do this two on one line, how?
indata = open(from_file).read()

# in_file = open(from_file)
# indata = in_file.read()

# Study Drill 1 remove features

# print(f"The input file is {len(indata)} bytes long")
#
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit Return to continue, CTRL-C to abort.")
# input('> ')

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# out_file.close()
# in_file.close()
