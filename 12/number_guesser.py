import random


def set_difficulty():
    levels = {
        "easy": 20,
        "medium": 15,
        "hard": 10
    }
    difficulty = input(
        "Choose a difficulty.\n Type 'easy', 'medium' or 'hard'.\n").lower()
    attempts = levels[difficulty]
    return attempts

def compare_numbers(guess, answer):
    if guess > answer:
        print("Too High.")
        return False
    elif guess < answer:
        print("Too Low.")
        return False
    else:
        print(f"You guessed correctly! the number was {answer}")

def start_game():
  the_number = random.randint(1, 100)
  print(the_number)
  attempts = set_difficulty()
  guessed = False
  while attempts > 0 and not guessed:
      user_guess = int(input("Guess a number between 1 and 100.\n"))
      result = compare_numbers(user_guess, the_number)
      if result:
          guessed = True
      else:
          attempts -= 1
          print(f"You have {attempts} left.")
  if attempts == 0:
      try_again = input("Game Over! Try again?\n Type 'y' or 'n'\n").lower()
      if try_again == 'y':
          guessed = False
          the_number = random.randint(1, 100)
          attempts = set_difficulty()
      else:
          print("Goodbye!")

start_game()        
# the_number = random.randint(1, 100)
# guessed = False

# levels = {
#     "easy": 20,
#     "medium": 15,
#     "hard": 10
# }


# def initalize():
#     difficulty = input(
#         "Choose a difficulty.\n Type 'easy', 'medium' or 'hard'.\n")
#     attempts = levels[difficulty]
#     return attempts


# attempts = initalize()

# while attempts > 0 and not guessed:
#     user_guess = int(input("Make a guess.\n"))
#     if user_guess == the_number:
#         print(f"You guessed correct! The number was {the_number}.")
#         guessed = True
#     elif user_guess < the_number:
#         print("Too low.")
#         attempts -= 1
#     elif user_guess > the_number:
#         print("Too High.")
#         attempts -= 1
#     print(f"You have {attempts} remaining.")
