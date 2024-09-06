
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

adjective = input("write an adjective: ")
caveName = input("write a name for a cave: ")
shape = input("write a shape: ")
hostage = input("write someone you would like to rescue: ")
currency = input("write a currency: ")
yourName = input("write your name: ")

madlib = f"A {adjective} dragon is hidden deep in the cave called {caveName} in Scotland. Your duty as a knight of the {shape} table is to kill the dragon and rescue {hostage}. If you kill the dragon and rescue {hostage} you will get one million of {currency}. The force be with you my dear {yourName}."

print(madlib)
































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")