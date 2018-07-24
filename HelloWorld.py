#Fibonacci Sequence printer

seq = [1]
step = 0
i = 0

test = 1.5

def fib(fibLen):
    for i in range (0, fibLen):
        seq.append(seq[step] + seq[step-1])      #Adds previous and current numbers in sequence
        print(seq[step])
    
        step = step + 1     #Increases step.
        
capitalLetterA = """"
 _______________
/   _________   \ 
|  |         |  |
|  |_________|  |
|  |         |  |
|  |         |  |
|__|         |__|
"""

def round(myFloat):
    if (myFloat - int(myFloat) >= 0.5):
        myFloat = int(myFloat) + 1
    elif (myFloat - int(myFloat) <= 0.5):
        myFloat = int(myFloat)
    return float(myFloat)

print(test)
print(round(test))