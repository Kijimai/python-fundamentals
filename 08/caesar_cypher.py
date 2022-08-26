from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Slow version
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         for a in range(len(alphabet)):
#             if alphabet[a] == letter:
#                 cipher_text += alphabet[a + shift_amount]
#     print(f"The encoded text is {cipher_text}.")


def caesar(some_text, shift_amount):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in some_text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index + shift_amount)
            output_text += alphabet[new_index]
        else:
            output_text += char
    print("**********************************")
    print(f"The encoded text is {output_text}")
    print("**********************************")


keep_going = True

while keep_going:
    direction_chosen = False
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)
    caesar(text, shift)
    decision = input(
        "Shall we keep going? Type 'yes' to continue, or anything else to quit. ").lower()
    if decision == "yes":
        keep_going = True
    else:
        keep_going = False
        print("See ya around!")
