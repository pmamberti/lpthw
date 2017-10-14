from sys import argv

script, increment = argv

print("Insert your limit: ")
limit = input('> ')

i = 0
numbers = []

# Review increment is broken

for i in range(0, int(limit)):
    print(f"At the top is {i}")
    numbers.append(i)

    i = i + int(increment)
    print("Numbers now:", numbers)

    print(f"At the bottom i is {i}")

for num in numbers:
    print("* -> ", num)
