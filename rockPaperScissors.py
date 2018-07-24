from random import seed
from random import randint

seed(1)

var playerOne = 0
var playerTwo = 0
score = [0,0]
#usage = [0, 0, 0, 0, 0]

#1 = rock; 2 = paper; 3 = scissors; 4 = lizard; 5 = Spock.

#Scissors (3) cuts Paper (2)
#Paper (2) covers Rock (1)
#Rock (1) crushes Lizard (4)
#Lizard (4) poisons Spock (5)
#Spock (5) smashes Scissors (2)
#Scissors (3) decapitate Lizard (4)
#Lizard (4) eats Paper (2)
#Paper (2) disproves Spock (5)
#Spock (5) vaporizes Rock (1)
#Rock (1) crushes Scissors (3)

def turn:
    playerOne = str(randint(1, 5))
    playerTwo = str(randint(1, 5))
    
    if playerOne + playerTwo == "32": #Scissors (3) cuts Paper (2)
        score[0] = score[0] + 1
        usage[2] = usage[2] + 1
        usage[0] = usage[0] + 1
    elif playerOne + playerTwo = "23"
        score[1] = score[1] + 1
        #usage[2] = usage[2] + 1
        #usage[0] = usage[0] + 1
        
    if playerOne + playerTwo == "21": #Paper (2) covers Rock (1)
        score[0] = score[0] + 1
        usage[2] = usage[2] + 1
        #usage[0] = usage[0] + 1
    elif playerOne + playerTwo = "12"
        score[1] = score[1] + 1

        #usage[2] = usage[2] + 1
        #usage[0] = usage[0] + 1