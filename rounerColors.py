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