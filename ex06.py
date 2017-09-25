# Define the Types of People variable
types_of_people = 10

# Print first half of the joke
x = f"There are {types_of_people} types of people."

# Define needed variables for second half of the joke
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print the joke
print(x)
print(y)

# Repeat the joke printing the variables in a text string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set evaluation variables for the joke
hilarious = False
joke_evaluation = "Isn't that joke so funny ?! {}"

# print joke using variable.format(bool) method
print(joke_evaluation.format(hilarious))

# Set up 2 variables and combine them when printing them out
w = "This is the left side of..."
e = "a string with a right side"

print(w + e)