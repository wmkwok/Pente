##Pente
## By Wendy Kwok and Liu Yangjun
# A texted based version of Pente board game

import random
import copy
import sys
import os
from gameAI import *

def main():
    print('PENTE')
    
    ##game loop
    while True:
        ##figure out who goes first
        turn = whoGoesFirst()
        ##0 is black and 1 is white, white always goes first
        if turn == 'computer':
            humanTile, computerTile = ('0', '1')
        else:
            humanTile, computerTile = ('1', '0')
        print "%s goes first" %turn
        gameBoard = getNewBoard()
        
        ##loop for turns
        while True:
            if turn == 'computer':
                os.system('clear')
                drawBoard(gameBoard)
                move = getComputerMove(gameBoard, computerTile)
                while move is None:
                    print 'Move is None type error.'
                    return
                if isValidMove(gameBoard, move):
                    makeMove(gameBoard, computerTile, move)
                if isWinner(gameBoard, computerTile):
                    winner = 'computer'
                    break
                turn = 'human'
                
            else:
                os.system('clear')
                drawBoard(gameBoard)
                move = getHumanMove(gameBoard, humanTile)
                if isValidMove(gameBoard, move):
                    makeMove(gameBoard, humanTile, move)
                if isWinner(gameBoard, humanTile):
                    winner = 'human'
                    break
                turn = 'computer'
            
            if isBoardFull(gameBoard):
                winner = 'tie'
                break
            
        drawBoard(gameBoard)
        if winner == 'tie':
            print "There is a tie."
        else:
            print "The winner is: ", winner
        if not playAgain():
            break
        sys.exit()

def playAgain():
    print("Would you like to play again? (yes or no)")
    return raw_input().lower().startswith('y')

def whoGoesFirst():
    ##chooses a random player
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'

def getHumanMove(board, tile):
    ##asks the player to make a move
    while True:
        if getPrevMove() == None:
            print "No previous computer move, You're the first!"
        else:
            print "Computer's move: ", getPrevMove()[0]+1, getPrevMove()[1]+1
        if tile == '0':
            print "Your color is Black"
        else:
            print "Your color is White"
        try:
            (moveX, moveY) = raw_input("Please make a move or <q q> to quit(ex 1 2): ").split()
        except ValueError:
            continue
        if moveX.lower().startswith('q'):
            print "exiting game..."
            sys.exit()
        if (not moveX.isdigit()) or (not moveY.isdigit()):
            continue
        else:
            moveX = int(moveX) - 1
            moveY = int(moveY) - 1
            print moveX, moveY
            if isValidMove(board, (moveX, moveY)):
                return (moveX, moveY)
 
if __name__ == '__main__':
    main()
