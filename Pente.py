##Pente
## By Wendy Kwok and Liu Yangjun
# A texted based version of Pente board game

import random
import copy
import sys
from A3 import *

def main():
    print('PENTE')


def playAgain():
    print("Would you like to play again? (yes or no)")
    return raw_input().lower().startswith('y')

##allows the user to enter which tile they want to be, probably not going to be used
def enterHumanTile():
    pass

def whoGoesFirst():
    ##chooses a random player
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'

def gerHumanMove(board):
    ##asks the player to make a move
    while True:
        (moveX, moveY) = raw_input("Please make a move(x, y) or q to quit: ")
        if move.lower().startswith('q'):
            sys.exit()
        if (not moveX.isdigit() or (not moveY.isdigit()):
            continue
        moveX = int(moveX) - 1
        moveY = int(moveY) - 1
        if isValidMove(board, moveX, moveY):
            return (moveX, moveY)
 
if __name__ == '__main__':
    main()
