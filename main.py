import sys
MIN_LEN = 8
SPEC_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
WEAK_SCORE_MAX = 2
GOOD_SCORE_MAX = 4
STRONG_SCORE_MAX = 5



def checkMinLen(pswd: str) -> int:
    if len(pswd) < MIN_LEN:
        return 0
    else:
        return 1
    

def checkUpperCase(pswd: str) -> int:
    for char in pswd:
        if char.isupper():
            return 1
    return 0

def checkLowerCase(pswd: str) -> int:
    for char in pswd:
        if char.islower():
            return 1
    return 0


def checkNums(pswd: str) -> int:
    for char in pswd:
        if char.isdigit():
            return 1
    return 0


def checkSpec(pswd: str) -> int:
    for char in pswd:
        if char in SPEC_CHARS:
            return 1
    return 0



def main(): 

    minLenFlag = 0
    upperFlag = 0
    lowerFlag = 0
    numFlag = 0
    specCharFlag = 0
    finalScore = 0

    password = sys.argv[1]

    minLenFlag = checkMinLen(pswd=password)
    upperFlag = checkUpperCase(pswd=password)
    lowerFlag =  checkLowerCase(pswd=password)
    numFlag = checkNums(pswd=password)
    specCharFlag = checkSpec(pswd=password)


    print(f"Upper flag: {upperFlag}")
    print(f"Lower flag: {lowerFlag}")
    print(f"Min len flag: {minLenFlag}")
    print(f"num flag: {numFlag}")
    print(f"spec char flag: {specCharFlag}")

    
    finalScore = minLenFlag + upperFlag + lowerFlag + numFlag + specCharFlag

    if finalScore <= WEAK_SCORE_MAX:
        print("Strength: Weak")
    elif finalScore > WEAK_SCORE_MAX and finalScore <= GOOD_SCORE_MAX:
        print("Strength: Good")
    elif finalScore == STRONG_SCORE_MAX:
        print("Strength: Strong")








if __name__ == "__main__":
    main()