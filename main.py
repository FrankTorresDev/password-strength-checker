import sys
MIN_LEN = 8
##things to check for
"""Minimum length (e.g., 8 characters)

Contains uppercase letters

Contains lowercase letters

Contains numbers

Contains special characters

$ python passcheck.py hello
Password strength: WEAK
Missing:
- uppercase letter
- number
- special character
- minimum length (8)"""



def checkMinLen(pswd: str) -> int:
    if len(pswd) < MIN_LEN:
        return 0
    else:
        return 1
    

def checkUpperCase(pswd: str) -> int:
    for char in pswd:
        if char == char.upper():
            return 1
    return 0

def checkNums(pswd: str) -> int:
    for char in pswd:
        if char.isdigit():
            return 1
    return 0

def checkSpec(pswd: str) -> int:
    ##use regex for this 
    return 


def main(): 

    minLenFlag = 0
    upperFlag = 0
    lowerFlag = 0
    numFlag = 0
    specChar = 0

    password = sys.argv[1]

    minLenFlag = checkMinLen(pswd=password)
    upperFlag = checkUpperCase(pswd=password)
    numFlag = checkNums(pswd=password)


    print(upperFlag)








if __name__ == "__main__":
    main()