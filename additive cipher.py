def Ceasar(string,shift):
    cipher=""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher= cipher + chr((ord(char) + 3 - 65) % 26 + 97)
        else:
            cipher= cipher + chr((ord(char) + 3 - 97) % 26 + 97)
    return cipher

string = input("Enter strings:")

print("orignal string:",string)
print("after enycryption:", Ceasar(string,3))