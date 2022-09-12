# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('./Input/Names/invited_names.txt', mode="r") as file:
    names = file.readlines()
    # print(names)

for name in names:
    with open('./Input/Letters/starting_letter.txt', mode="r") as file:
        contents = file.read()
        stripped_name = name.strip()
        new_letter = contents.replace('[name]', stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="x") as complete_letter:
            complete_letter.write(new_letter)
