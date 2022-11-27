def encrypt(text,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char)+shift-65) % 26 + 65)
        else:
            result += chr((ord(char)+shift-97) % 26 + 97)
    return result


def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char)-shift-65) % 26 + 65)
        else:
            result += chr((ord(char)-shift-97) % 26 + 97)
    return result


text = input()
shift = int(input())

# Encryption for the Original String
encrypted = encrypt(text,shift)
print(encrypted)

# Decryption for the encrypted String
print(decrypt(encrypted,shift))