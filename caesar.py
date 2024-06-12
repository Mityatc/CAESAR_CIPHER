alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_count,cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_count *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_count)%26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d is {end_text}")
from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_count=shift,cipher_direction=direction)
    result = input("Type 'yes' if you want to do it again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("GoodBye")




