alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

from art import logo

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet) or new_position < (-1 *
                                                               len(alphabet)):
                new_position = (new_position) % len(alphabet)
                end_text += alphabet[new_position]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}\n")


play_on = True
while play_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    play_on_check = input(
        "Would you like to restart the cipher program? Type 'yes' to continue or 'no' to end the program.\n"
    )
    if play_on_check == "no":
        print("Thank you for using the program.")
        play_on = False

    continue

