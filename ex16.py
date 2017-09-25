from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("if you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit Return.")

input('?')

print("Opening the file...")
target = open (filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

# Study Drill 3 - consolidate these in 1 line
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

# Study drill 2

txt = open(filename)

print("----- Your new File -----")
print(txt.read())

# moving this down for sanity
