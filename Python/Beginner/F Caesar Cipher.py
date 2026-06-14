alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer="yes"
while answer=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(original_text,shift_amount):
        encoded=""
        for letter in original_text:
            if letter in alphabet:
                i=alphabet.index(letter)
                while i+shift_amount>=len(alphabet):
                    shift_amount-=len(alphabet)
                encoded+=alphabet[i+shift_amount]
            else:
                encoded+=letter
        print(encoded)

    def decrypt(original_text,shift_amount):
        decoded=""
        for letter in original_text:
            if letter in alphabet:
                i=alphabet.index(letter)
                while i+shift_amount>=len(alphabet):
                    shift_amount-=len(alphabet)
                decoded+=alphabet[i-shift_amount]
            else:
                decoded+=letter
        print(decoded)

    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)
    else:
        print("Encoding and decoding are the only available functions.")
    answer=input("Would you like to try again? Type 'yes' or 'no'\n")



