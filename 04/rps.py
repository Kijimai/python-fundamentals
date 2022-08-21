import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = ["rock", "paper", "scissors"]
rng = random.randint(0, len(choices) - 1)
player_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
cpu_choice = choices[rng]
if player_choice == 0:
    print(rock)
    print("Computer chose:")
    if cpu_choice == "scissors":
        print(scissors)
        print("You win!")
    if cpu_choice == "paper":
        print(paper)
        print("You lose!")
    if cpu_choice == "rock":
        print(rock)
        print("It was a tie!")
elif player_choice == 1:
    print(paper)
    print("Computer chose:")
    if cpu_choice == "scissors":
        print(scissors)
        print("You lose!")
    if cpu_choice == "paper":
        print(paper)
        print("It was a tie!")
    if cpu_choice == "rock":
        print(rock)
        print("It was a tie!")
elif player_choice == 2:
    print(scissors)
    print("Computer chose:")
    if cpu_choice == "scissors":
        print(scissors)
        print("It was a tie!")
    if cpu_choice == "paper":
        print(paper)
        print("You win!")
    if cpu_choice == "rock":
        print(rock)
        print("You lose!")
# if player_choice == "rock":
#   if cpu_choice == "paper":
