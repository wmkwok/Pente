import sys
import copy

prevMove = None
n = 10
tboard = [['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
         ['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
         ['.', '.', '0', '1', '.', '.', '.', '0', '1', '.'], \
         ['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
         ['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
         ['.', '.', '0', '1', '.', '.', '.', '0', '1', '.']]
print tboard[0][1]

def getComputerMove(board, tile):
    global prevMove
    for x in range(n):
        for y in range(n):
            if isValidMove(board, (x, y)):
                prevMove = (x, y)
                return (x, y)

def drawBoard(board):
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
    newBoard = []
    theRow = []
    for i in range(n):
        theRow.append('.')
    for j in range(n):
        newBoard.append(copy.deepcopy(theRow))
    return newBoard

def isValidMove(board, move):
    return (board[move[0]][move[1]] == '.')

##change board state, move is tuple(x, y)
def makeMove(board, player, move):
    board[move[0]][move[1]] = player

def getPrevMove():
    return prevMove

def isBoardFull(board):
    for row in range(n):
        for col in range(n):
            if board[row][col] == '.':
                return False
    return True

def isWinner(board, tile):
    return False


'''

##this is 0 
print u"\u25CB"

##this is 1
print u"\u25CF"

'''
