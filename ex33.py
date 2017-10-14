from sys import argv

script, increment = argv

print("Insert your limit: ")
limit = input('> ')

def while_loop(j):
    i = 0
    while i < int(limit):
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + int(j)
        print("Numbers now:", numbers)

        print(f"At the bottom i is {i}")

    return numbers

numbers = []
while_loop(increment)

for num in numbers:
    print("* -> ", num)
