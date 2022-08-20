import random

names = input("Give me everybody's names, separated by a comma.\n").split(', ')

print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")