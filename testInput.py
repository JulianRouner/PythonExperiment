from time import sleep
from rounerColors import *
import sys

myInput = input("Enter a phrase: ")

def slowPrint(slowPrintString, slowPrintTime):
    for c in slowPrintString:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c == "!" or c == "." or c == "?":
            sleep(2.8 * slowPrintTime)
        else:
            sleep(slowPrintTime)
    print()

    slowPrint(colorPrint(myInput, RED), 0.06)