# Encryption of a plaintext
def encrypt(plaintext, key):
    
    key_length = len(key)

    key_as_int = [ord(i)for i in key]

    plaintext_int = [ord(i) for i in plaintext]

    ciphertext = ""

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i]+key_as_int[ i % key_length]) % 26
        ciphertext += chr(value + 65)

    return ciphertext.upper()

# Decryphertext using encryot
def decrypt(ciphertext,key):
    key_length = len(key)

    key_as_int = [ord(i) for i in key]

    ciphertext_int = [ord(i) for i in ciphertext]

    plaintext = ""

    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26

        plaintext += chr(value + 65)

    return plaintext.upper()

while True:
#input plaintext
    print("hello what you wanna convert type 1 plaintext to ciphertext or 2 for ciphertext to plaintext")
    a = int(input())

    if a==1:
        plaintext = input("enter the PLAINTEXT:")
        key = input("Enter the key:")
        print("Encrypted message",encrypt(plaintext, key))
    elif a==2:
        ciphertext = input("enter the CIPHERTEXT:")
        key = input("Enter the key:")
        print("Decrypted message", decrypt(ciphertext,key))
    else:
        print("sorry unable to code")
