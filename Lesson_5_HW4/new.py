alhpabet = "abcdefghijklmnopqrstuvwxyz"
shifted_abc = "klmnopqrstuvwxyzabcdefghij"
alhpabet_len = len(alhpabet)

def encode(text, shift):
    char = text[0]
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            idx = alhpabet.index(char)
            new_idx = (idx + shift)% alhpabet_len
            result += alhpabet[new_idx]
    return result


def decode(text, shift):
    char = text[0]
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            idx = alhpabet.index(char)
            new_idx = (idx - shift) % alhpabet_len
            result += alhpabet[new_idx]
    return result


def main():
    user_text = input("введить текст:")
    shift = int(input("введить сдвиг:"))
    encrypted_text = encode(user_text, shift)
    print("Encrypted text is:", encrypted_text)
    print("Decrypted text is:", decode(encrypted_text, shift))

main()