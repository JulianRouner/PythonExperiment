from time import sleep
import sys

myInput = input("Enter a phrase ")

def slowPrint(slowPrintString, slowPrintTime):
    for c in slowPrintString:
        sys.stdout.write(c)
        sys.stdout.flush
        if c == "." ||
        sleep(slowPrintTime)
    print()
    
slowPrint(myInput, 0.05)