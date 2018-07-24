NORMAL = "0"
BOLD   = "1"
FAINT  = "2"
ITALIC = "3"
UNDERLINE = "4"
SLOW_BLINK  = "5"
RAPID_BLINK = "6"
REVERSE= "7"


BLACK = "\033[1;30m"
RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
YELLOW ="\033[0;33m"
BLUE  = "\033[1;34m"
MAGENTA = "\033[0;35m"
CYAN  = "\033[1;36m"
WHITE = "\033[0;37m"
RESET = "\033[0;0m"


def colorPrint(rounerString, rounerColour, rounerEffects):
    rounerString = "\033" + rounerEffects + rounerColour + rounerString + RESET
    return rounerString