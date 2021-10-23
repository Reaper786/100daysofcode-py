alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")text = input("Type your message:\n").lower()shift = int(input("Type the shift number:\n"))

def encode(Text, Shift): encoded_text = [] for n_T in range(0, len(Text)): for n_A in range(0, len(alphabet)): if Text[n_T] == alphabet[n_A]: if n_A + Shift >= len(alphabet): Shift1 = Shift - (len(alphabet) - n_A) n_A1 = 0 encoded_text += alphabet[n_A1 + Shift1] else: encoded_text += alphabet[n_A + Shift] print(f"{color.white}Your encrypted message is {''.join(encoded_text)}{color.end}")

if direction == "encode": encode(Text = text, Shift = shift)