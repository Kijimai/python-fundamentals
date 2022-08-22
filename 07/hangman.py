import random
from hangman_art import stages, logo
from hangman_words import word_list


lives = 6
chosen_word = random.choice(word_list)
display = []
end_of_game = False

# This can also be done as well as using .append()
# This expression adds each individual string character as a single element in the list -- 'aaa' == ['a','a','a']
for l in chosen_word:
    display += '_'

print("Welcome to...")
print(logo)

while not end_of_game:
    print(display)
    guess_letter = input("Guess a letter:\n")
    if len(guess_letter) > 1:
        print("Please type only one letter!")
    if guess_letter in display:
        print("You already guessed this!")
    for position in range(len(chosen_word)):
        if guess_letter == chosen_word[position]:
            display[position] = guess_letter
        if(''.join(display) == chosen_word):
            end_of_game = True
        if position == len(chosen_word) - 1 and not guess_letter in chosen_word:
            print("Incorrect Guess!")
            lives -= 1
            print(f"You only have {lives} lives left!")
            print(stages[lives])
            if lives == 0:
                end_of_game = True

if lives > 0 and end_of_game:
    print(f"Thats right! The word was {chosen_word}.")
    print("You win!")
else:
    print(''.join(display))
    print(f"The word was {chosen_word}.")
    print("You lose!")
    print(stages[0])
