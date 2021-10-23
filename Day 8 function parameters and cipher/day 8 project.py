# # Caesar Cipher
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# completed = False
#
#
#     max_list = len(alphabet)
#
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         if new_position >= max_list:
#             new_position = (new_position - max_list) + 0
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#         else:
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")
#
#         ##HINT: How do you get the index of an item in a list:
#         # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#         ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
#
# def decrypt(text, amount):
#     max_list = len(alphabet)
#
#     decryption_cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         if new_position <= 0:
#             new_position = max_list - new_position
#             new_letter = alphabet[new_position]
#             decryption_cipher_text += new_letter
#         else:
#             new_letter = alphabet[new_position]
#             decryption_cipher_text += new_letter
#     print(f"The encoded text is {decryption_cipher_text}")

#
# if direction == "encode":
#     encrypt(text, shift)
#
# if direction == "decode":
#     decrypt(text, shift)
############################################################################

# improved caesar cipher
#
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction):
# # Static Variables:
#     cipher = ""
#     max_list = len(alphabet)
#
# # Function - Start:
#
#     for letter in cipher_text:
#         position = alphabet.index(letter)
# # decoding section:
#         if cipher_direction == "decode":
#             new_position = position - cipher_shift
#             if new_position <= 0:
#                 new_position = max_list + new_position
#                 if new_position == 26:
#                     new_position = 0
#                 new_letter = alphabet[new_position]
#                 cipher += new_letter
#             else:
#                 new_letter = alphabet[new_position]
#                 cipher += new_letter
# # encoding section:
#         if cipher_direction == "encode":
#             new_position = position + cipher_shift
#             if new_position >= max_list:
#                 new_position = (new_position - max_list) + 0
#                 new_letter = alphabet[new_position]
#                 cipher += new_letter
#             else:
#                 new_letter = alphabet[new_position]
#                 cipher += new_letter
#
#     print(f"This is your secured message {cipher}")
#
# # function call:
# caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction)

############################################################################

# lecturers code

from logo import logo

while True:
    print(logo)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))




    def ischar(n):
        if n.isalpha():
            return True
        else:
            return False



    def caesar(cipher_text, cipher_shift, cipher_direction):

        if cipher_shift >= 26:
            cipher_shift = cipher_shift % 25

        end_text = ""
        max_list = len(alphabet)

        if cipher_direction == "decode":
            cipher_shift *= -1
        for char in cipher_text:
            if ischar(n=char):
                position = alphabet.index(char)
                new_position = position + cipher_shift
                if new_position > 26:
                    new_position -= max_list
                elif new_position == 26:
                    new_position = 0
                end_text += alphabet[new_position]
            else:
                end_text += char

        print(f"Here's the {cipher_direction}d result: {end_text}")

    caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction)

    user = input("Do you wish to rerun the program? (y or n)\n".lower())
    if user == "y":
        continue
    else:
        break
