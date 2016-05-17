# Pente 
# By Wendy Kwok and Yangjun Liu

import random
import copy
import sys
import os
import timeit
from gameAI import *

def main():
    print ("Pente")
    
    # main loop
    while True:
        #decide which player uses which tile and who goes first
        turn = whoGoesFirst()
        # 0 is back and 1 is white, white always goes first
        if turn == 'computer':
            humanTile, computerTile = ('0', '1')
        else:
            humanTile, comptuerTile = ('1', '0')
        print "%s goes first" %turn
        gameBoard = getNewBoard()
        humanCaptures = 0
        computerCaptures = 0
        drawBoard(gameBoard)

        # loop for turns
        while True:
            if turn == 'computer':
                print "Computer is thinking..."
                move = getComputerMove(gameBoard, computerTile)
                while move is None:
                    print 'Move is none type error'
                    return
                    
                # check if the move is valid
                if isValidMove(gameBoard, move):
                    makeMove(gameBoard, computerTile, move)
                    drawBoard(gameBoard)
                else:
                    print "move chosen was invalid"
                    continue
                if isWinner(gameBoard, computerTile):
                    winner = 'computer'
                    break
                turn = 'human'

            else:
                print "It's your turn"
                move = getHumanMove(gameBoard, humanTile)
                
                # check if the move is valid
                if isValidMove(gameboard, move):
                    makeMove(gameBoard, humanTile, move)
                    drawBoard(gameBoard)
                else:
                    print "move chosen was invalid"
                    continue
                if isWinner(gameBoard, humanTile):
                    winner = 'human'
                    break
                turn = 'computer'

            if isBoardFull(gameBoard):
                winner = 'tie'
                break
        drawBoard(gameBoard)
        if winner == 'tie':
            print "There is a tie"
        else:
            print "the winner is %s" %winner
        
        # ask if they want to play again
        if not playAgain():
            break
        sys.exit()

def playAgain():
    print("would you like to play again? (yes or no)")
    return raw_input().lower().startswith('y')

def whoGoesFirst():
    # chooses a random player to be white
    if random,randint(0,1) == 0:
        return 'computer'
    else:
        return 'human'

def getHumanMove(board, tile):
    # asks the player to make a move
    while True:
        if getPrevMove() == None:
            print "no previous computer move, you're the first!"
        else:
            print "Computer's move: ", getPrevMove()[0]+1, getPrevMove()[1]+1
        if tile == '0':
            print "your color is black"
        else:
            print "your color is white"
        try:
            (moveX, moveY) = raw_input("Please make a move or <q q> to quit(ex 1 2)"):
        except ValueError:
            print "invalid input"
            continue
        if moveX.lower().startswith('q'):
            print 'exiting game...'
        else:
            moveX = int(moveX) - 1
            moveY = int(moveY) - 1
            print "Your move is (%s, %s)" %(moveX, moveY)
            if isValidMove(board, (moveX, moveY)):
                return (moveX, moveY)


if __name__ == '__main__':
    main()
