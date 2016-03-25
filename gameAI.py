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
    if move[0] >= 0 and move[0] < n and move[1] >= 0 and move[1] < n:
        return (board[move[0]][move[1]] == '.')
    return False

def isCaptureMove(board, player, move):
    ##check to see if the move made is going to capture
    if player == '0':
        unplayer = '1'
    else:
        unplayer = '0'
        
    ##check horizontal captures
        if (move[1] > 2 and \
                board[move[0]][move[1]-1] == unplayer and \
                board[move[0]][move[1]-2] == unplayer and \
                board[move[0]][move[1]-3] == player):
            board[move[0]][move[1]-1] = '.'
            board[move[0]][move[1]-2] = '.'
            return True
        
        if (move[1] < n-3 and \
                board[move[0]][move[1]+1] == unplayer and \
                board[move[0]][move[1]+2] == unplayer and \
                board[move[0]][move[1]+3] == player):
            board[move[0]][move[1]+1] = '.'
            board[move[0]][move[1]+2] = '.'
            return True
        
    ##check vertical captures
        if (move[0] > 2 and \
                board[move[0]-1][move[1]] == unplayer and \
                board[move[0]-2][move[1]] == unplayer and \
                board[move[0]-3][move[1]] == player):
            board[move[0]-1][move[1]] = '.'
            board[move[0]-2][move[1]] = '.'

        if (move[0] < n-3 and \
                board[move[0]+1][move[1]] == unplayer and \
                board[move[0]+2][move[1]] == unplayer and \
                board[move[0]+3][move[1]] == player):
            board[move[0]+1][move[1]] = '.'
            board[move[0]+2][move[1]] = '.'

    ##check diagonal cpatures
        if (move[0] > 2 and move[1] > 2 and\
                board[move[0]-1][move[1]-1] == unplayer and \
                board[move[0]-2][move[1]-2] == unplayer and \
                board[move[0]-3][move[1]-3] == player):
            board[move[0]-1][move[1]-1] = '.'
            board[move[0]-2][move[1]-2] = '.'
        
        if (move[0] < n-3 and move[1] < n-3 and\
                board[move[0]+1][move[1]+1] == unplayer and \
                board[move[0]+2][move[1]+2] == unplayer and \
                board[move[0]+3][move[1]+3] == player):
            board[move[0]+1][move[1]+1] = '.'
            board[move[0]+2][move[1]+2] = '.'
        
    ##check other diagonal captures
        if (move[0] > 2 and move[1] > 2 and\
                board[move[0]-1][move[1]+1] == unplayer and \
                board[move[0]-2][move[1]+2] == unplayer and \
                board[move[0]-3][move[1]+3] == player):
            board[move[0]-1][move[1]+1] = '.'
            board[move[0]-2][move[1]+2] = '.'
        
        if (move[0] < n-3 and move[1] < n-3 and\
                board[move[0]+1][move[1]-1] == unplayer and \
                board[move[0]+2][move[1]-2] == unplayer and \
                board[move[0]+3][move[1]-3] == player):
            board[move[0]+1][move[1]-1] = '.'
            board[move[0]+2][move[1]-2] = '.'
        

##change board state, move is tuple(x, y)
def makeMove(board, player, move):
    isCaptureMove(board, player, move)
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
    ##checking horizontal spaces
    for y in range(n):
        for x in range(n - 4):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile and board[x+4][y] == tile:
                return True

    ##checking for vertical spaces
    for x in range(n):
        for y in range(n - 4):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile and board[x][y+4] == tile:
                return True

    ##checking for diagonal spaces
    for x in range(n - 4):
        for y in range(4, n):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile and board[x+4][y-4] == tile:
                return True

    ##check other diagonal spaces
    for x in range(n - 4):
        for y in range(n - 4):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile and board[x+4][y+4] == tile:
                return True

    ##checking capture pairs

    return False


'''

##this is 0 
print u"\u25CB"

##this is 1
print u"\u25CF"

'''
