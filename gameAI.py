import sys
import copy

n = 10
board = [['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
         ['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
         ['.', '.', '0', '1', '.', '.', '.', '0', '1', '.'], \
         ['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
         ['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
         ['.', '.', '0', '1', '.', '.', '.', '0', '1', '.']]

def newBoard(board):
    boarder = ""

    ##add in the top border
    boarder += "$$  "
    for i in range(n*2+1):
        boarder += '-'
    boarder += '\n'

    ##add in row
    for row in range(n):
        boarder += "$$ | "
        for col in range(n):
            if board[row][col] == '1':
                boarder += u"\u25CF "
            elif board[row][col] == '0':
                boarder += u"\u25CB "
            else:
                boarder += ". "
        boarder += "|\n"

    ##add in the bottom border
    boarder += "$$  "
    for i in range(n*2+1):
        boarder += '-'
    boarder += '\n'
    print boarder

##creates a fresh board
def getNewBoard():
    pass

##change board state
makeMove(board, player, column):
    pass

def isValidMove(board, move):
    pass

def isBoardFull(board):
    pass

def isWinner(board, tile):
    pass

newBoard(board)

'''

##this is 0 
print u"\u25CB"

##this is 1
print u"\u25CF"

'''
