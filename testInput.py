from time import sleep
from rounerColors import *
import sys

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


slowPrint(colorPrint(myInput, MAGENTA, [BOLD, REVERSE]), 0.06)

slowPrint(colorPrint("I am as I was before.", RED, [REVERSE_RESET, NORMAL]), 0.06)
slowPrint(colorPrint("You have been gone for a long time. Much has changed.", RED, [BOLD]), 0.06)
