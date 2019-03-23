way = input("what would you do: encrypt or decrypt(e/d):")

if way == "e":
    string = input("input string to encrypt: ")
    string = string.lower()
    encrypted = ""
    for char in string:
        if "x" <= char <= "z":
            encrypted += chr(ord(char)-23)
        elif char == " ":
            encrypted += " "
        else:
            encrypted += chr(ord(char)+3) 
    print(encrypted)
elif way == "d":
    string = input("input string to decrypt: ")
    decrypted = ""
    for char in string:
        if "a" <= char <= "c":
            decrypted += chr(ord(char)+23)
        elif char == " ":
            decrypted += " "
        else:
            decrypted += chr(ord(char)-3)     
    print(decrypted)
else:
    print("no actions allowed")