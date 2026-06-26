

def caesar_cipher(message, shift, mode):
    result = ""
    for ch in message:

        # process only alphabet letters
        if ch.isalpha():
            base = 65 if ch.isupper() else 97

            #Encrypt the message
            if mode == "e":
                result += chr((ord(ch) - base + shift) % 26 + base)
            #Decrypt the message
            else:
                result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result

message = input("Enter message: ")
shift = int(input("Enter shift number: "))
choice = input("Encrypt or Decrypt? (e/d): ").lower()

print("Result:", caesar_cipher(message, shift, choice))