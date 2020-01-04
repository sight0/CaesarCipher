import string
import bcolors

shift = 3

def encrypt(text, shift):
    alphabet = list(string.ascii_lowercase)
    plain_text = []
    encrypted_text = []
    for char in text:
        plain_text.append(char)
    for x in plain_text:
        for y in alphabet:
            if(x==y):
                index = alphabet.index(x)
                if(index + shift < len(alphabet)):
                    encrypted_text.append(alphabet[index+shift])
                else:
                    encrypted_text.append(alphabet[index+shift - 26])
    print("\nEncrypted text is: " + bcolors.HEADER + (''.join(encrypted_text)) + bcolors.ENDC)

print(encrypt(input("\nPlain text to encrypt: "), int(input("\nShift: "))))
