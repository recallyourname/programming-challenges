import os
import secrets

def password(num):
    data = ""
    availableSymbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[].,?"
    for i in range(num):
        data += secrets.choice(availableSymbols)
    return data


def main():
    try:
        os.mkdir("passwords")
        print("Directory passwords created")
    except FileExistsError:
        print("Directory passwords already exist")

    directory = os.getcwd()
    n = int(input("Input the number of symbols in password: "))
    with open(directory+'/passwords/password.txt','w+') as f:
        data = password(n)
        f.write(data+"\n")
        f.close()
    print(data)
    print("Password also stored in /filedirectory/passwords")

if __name__ == "__main__":
    main()