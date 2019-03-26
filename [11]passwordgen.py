import os
import secrets

def makedirectory():
    try:
        os.mkdir("passwords")
        print("Directory passwords created")
    except FileExistsError:
        print("Directory passwords already exist")    

def password(num):
    data = ""
    availableSymbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=+[].,?"
    for _ in range(num):
        data += secrets.choice(availableSymbols)
    return data

def main():
    makedirectory()
    directory = os.getcwd()
    number = None

    while number is None:
        try:
            number = int(input("Input the number of symbols in password: "))
        except (ValueError, UnboundLocalError):
            print("Must be an integer number, try again!")

    label = input("Put a label for your password here(where it will be used): ")

    with open(directory+'/passwords/password.txt','a+') as f:
        data = password(number)
        f.write("Password for "+label+" is: "+data+"\n")
        f.close()
    print(data)
    print("Password also stored in "+directory+"/passwords")

if __name__ == "__main__":
    main()