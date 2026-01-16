#check to see if it matches anything in a text file of passwords


import argparse
MIN_LEN = 8
SPEC_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
WEAK_SCORE_MAX = 2
GOOD_SCORE_MAX = 4
STRONG_SCORE_MAX = 5

parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, help="Name of password list file")
parser.add_argument("-p", type=str, help="Your Password")
args = parser.parse_args()
fileName = args.f

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


def checkInFile(pswd: str, fName: str ) -> bool:

    file = open(fName, 'r')
    line = file.readline()
    while line != "":
        if line.strip() == pswd:
            file.close()
            return True
        line = file.readline()

    file.close()
    return False



def main(): 

    flags = {"minLen": 0, "upper": 0, "lower": 0, "num": 0, "specChar": 0}
    
    finalScore = 0


    password = args.p

    flags['minLen'] = checkMinLen(pswd=password)
    flags['upper'] = checkUpperCase(pswd=password)
    flags['lower'] =  checkLowerCase(pswd=password)
    flags['num'] = checkNums(pswd=password)
    flags['specChar'] = checkSpec(pswd=password)

    
    finalScore = flags['minLen'] + flags['upper'] + flags['lower'] + flags['num'] + flags['specChar']

    if finalScore <= WEAK_SCORE_MAX:
        print("Strength: Weak")
    elif finalScore > WEAK_SCORE_MAX and finalScore <= GOOD_SCORE_MAX:
        print("Strength: Good")
    elif finalScore == STRONG_SCORE_MAX:
        print("Strength: Strong")


    if checkInFile(pswd=password, fName=fileName):
        print(f"Your password {password} was found in file {fileName}")
    else:
        print(f"Your password {password} was NOT found in file {fileName}")







if __name__ == "__main__":
    main()