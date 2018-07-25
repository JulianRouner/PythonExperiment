from time import sleep
import sys

NORMAL = "0"
BOLD   = "1"
FAINT  = "2"
ITALIC = "3"
UNDERLINE = "4"
SLOWBLINK  = "5"
RAPIDBLINK = "6"
REVERSE = "7"
STRIKE = "9"

BLACK = "30m"
RED   = "31m"  
GREEN = "32m"
YELLOW ="33m"
BLUE  = "34m"
MAGENTA = "35m"
CYAN  = "36m"
WHITE = "37m"
RESET = "\033[0;0m"
REVERSE_RESET = "27"

def colorPrint(rounerString, rounerColour, rounerEffects):
    rounerString = rounerColour + rounerString
    for effect in rounerEffects:
        rounerString = effect + ";" + rounerString
    rounerString = "\033[" + rounerString + RESET
    return rounerString
    
myInput = input("Enter a phrase: ")

def slowPrint(slowPrintString, slowPrintTime):
    for c in slowPrintString:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c == "!" or c == "." or c == "?":
            sleep(3 * slowPrintTime)
        else:
            sleep(slowPrintTime)
    print()


#slowPrint(colorPrint(myInput, MAGENTA, [BOLD, REVERSE]), 0.06)

#slowPrint(colorPrint("I am as I was before.", RED, [REVERSE_RESET, NORMAL]), 0.06)
#slowPrint(colorPrint("You have been gone for a long time. Much has changed.", RED, [BOLD]), 0.06)
