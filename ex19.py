def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drill

def silly_function(silly1, silly2):
    print("--------------------------------\n This is a terribly simple story:\n--------------------------------\n")
    print(f"{silly1} is a guy and {silly2} is a girl")
    print("They like each other and get married.")
    print("----> End of story. [/insert sad trombone here].")

silly_function("lol", "lulz")

silly_function("lol" + input('Name 1 > '), input('Name 2 > '))
