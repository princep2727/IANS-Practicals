def Additive(string,shift):
    cipher=""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher= cipher + chr((ord(char) + s - 65) % 26 + 97)
        else:
            cipher= cipher + chr((ord(char) + s - 97) % 26 + 97)
    return cipher

string = input("Enter strings:")
s = int(input("enter the shift you want:"))
print("orignal string:",string)
for s in range(s):
    print("after enycryption:", Additive(string,"s"))
