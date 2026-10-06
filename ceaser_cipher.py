alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text, shift, direction):
       new_text = ""
       if direction == 'decode':
        shift *= -1
       for letter in text:
           if letter in alphabet:
               index = alphabet.index(letter)
               new_text += alphabet[(index + shift)]
           else:
               new_text += letter
       print(f'Your final message is: {new_text}')


end_program = True
while end_program:
    direction = input("type 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("Enter your message: ").lower()
    shift = int(input("Enter your shift number: "))
    shift = shift % 26
    ceaser(text, shift, direction)
    check = input("Do you want to continue? type 'yes' or 'no' ").lower()
    if check == 'no':
        end_program = False
        print("Goodbye!")

