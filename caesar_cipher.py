def caesar(text, shift, encrypt=True ):

    if not isinstance(shift , int):
        return "Shift must be an integer value."
    if  shift<1 or shift>25 :
        return"Shift must be an integer between 1 and 25."

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() , shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

decrypted_text = 'World is not as monotonous as I thought.'
encrypted_text = encrypt( decrypted_text , 13)
print('Encrypted text :', encrypted_text)

encrypted_text_1 = 'Jbeyq vf abg nf zbabgbabhf nf V gubhtug.'
decrypted_text_1 = decrypt(encrypted_text_1 , 13)
print('Decrypted text :', decrypted_text_1)

