#picking random link

import random as ran

def linkPick(x):
    intOflength = int(len(x))
    randomNum = ran.randint(0, intOflength - 1)
    return x[randomNum]
