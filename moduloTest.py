
for i in range (1, 100):
    if i % 3 == 0:
        print("(" + str(i) + ")" + "Fizz" , end="")
        if i % 5 == 0:
            print("",end="")
        else:
            print("",end="\n")
    if i % 5 == 0:
        print("Buzz" + "(" + str(i) + ")", end="")
        print("",end="\n")