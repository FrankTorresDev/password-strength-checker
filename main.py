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

#checks for minimum length
def checkMinLen(pswd: str) -> int:
    if len(pswd) < MIN_LEN:
        return 0
    else:
        return 1
    
#checks for uppercase letters
def checkUpperCase(pswd: str) -> int:
    for char in pswd:
        if char.isupper():
            return 1
    return 0

#checks for lowercase letters
def checkLowerCase(pswd: str) -> int:
    for char in pswd:
        if char.islower():
            return 1
    return 0

#checks for numbers
def checkNums(pswd: str) -> int:
    for char in pswd:
        if char.isdigit():
            return 1
    return 0

#checks for special characters
def checkSpec(pswd: str) -> int:
    for char in pswd:
        if char in SPEC_CHARS:
            return 1
    return 0

#checks to see if password is in a file (good to check in things like rockyou.txt and other know password lists for bruteforce)
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


def finalMsgDisplay(minLen, upper, lower, num, specChar, inFile, pswd, fName, finalScore):

    if finalScore <= WEAK_SCORE_MAX:
            print("Strength: Weak")
    elif finalScore > WEAK_SCORE_MAX and finalScore <= GOOD_SCORE_MAX:
            print("Strength: Good")
    elif finalScore == STRONG_SCORE_MAX:
            print("Strength: Strong")

    if finalScore < STRONG_SCORE_MAX:
        print("MISSING:")
        if minLen == 0:
            print(f"Minumum Length of {MIN_LEN} not reached")
        if upper == 0:
            print("Upper case letter")
        if lower == 0:
            print("Lower case letter")
        if num == 0:
            print("A number")
        if specChar == 0:
             print(f"Special Character ex. {' '.join(SPEC_CHARS)}")

    if inFile:
            print(f"Your password {pswd} was found in file {fileName}")
    else:
            print(f"Your password {pswd} was NOT found in file {fileName}")
    return


def main(): 

    flags = {"minLen": 0, "upper": 0, "lower": 0, "num": 0, "specChar": 0}
    inFile = False
    finalScore = 0

    password = args.p

    flags['minLen'] = checkMinLen(pswd=password)
    flags['upper'] = checkUpperCase(pswd=password)
    flags['lower'] =  checkLowerCase(pswd=password)
    flags['num'] = checkNums(pswd=password)
    flags['specChar'] = checkSpec(pswd=password)

    
    finalScore = flags['minLen'] + flags['upper'] + flags['lower'] + flags['num'] + flags['specChar']
    inFile = checkInFile(pswd=password, fName=fileName)

    finalMsgDisplay(flags['minLen'], flags['upper'], flags['lower'], flags['num'], flags['specChar'], inFile, password, fileName, finalScore)
    

if __name__ == "__main__":
    main()