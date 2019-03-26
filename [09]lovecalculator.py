def isVowel(string):
    if string in 'aeiou':
        return True
    else:
        return False

def numOfVowels(string):
    string.lower()
    result = 0
    for i in string:
        if isVowel(i):
            result += 1
    return result

def main():
    name1 = input("Put your name here: ")
    name2 = input("Put your bae's name: ")
    name1 = name1.lower()
    name2 =name2.lower()
    cons1 = len(name1) - numOfVowels(name1)
    cons2 = len(name2) - numOfVowels(name2)
    pts = 0
    if len(name1) == len(name2):
        pts += 20
    if isVowel(name1[0]) and isVowel(name2[0]):
        pts += 10
    if not isVowel(name1[0]) and not isVowel(name2[0]):
        pts += 5
    if numOfVowels(name1) == numOfVowels(name2):
        pts += 12
    if cons1 == cons2 :
        pts += 12
    if ('l' or 'o' or 'v' or 'e') in name1 and name2:
        pts += 7
    print("You have: %d of 66 compatibility points" %pts)

if __name__ == "__main__":
    main()