import string
from random import choice, shuffle

def randomPass():
    lowerChars = list(string.ascii_lowercase)
    upperChars = list(string.ascii_uppercase)
    digits = list(string.digits)

    allChars = lowerChars + upperChars + digits
    shuffle(allChars)

    passLength = int(input("How long is the password?: "))
    password = ""

    for i in range(passLength):
        password += choice(allChars)
    print(password)


randomPass()
