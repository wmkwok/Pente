import sys
import copy

prevMove = None
n = 10

'''
A game board looks like this
[['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
['.', '.', '0', '1', '.', '.', '.', '0', '1', '.'], \
['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'], \
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
['1', '.', '0', '.', '.', '1', '.', '0', '.', '.'], \
['.', '.', '.', '.', '0', '.', '.', '.', '.', '0'], \
['.', '.', '0', '1', '.', '.', '.', '0', '1', '.']]
'''
##UNCHECKED:
##gen child
##minValue
##maxValue
##AlphaBeta

##UNIMPLEMENTED
##captured pairs count
## win when 5 capture pairs
##counter to keep track of pieces of stones left
##heuristic <-- this should be last last part

'''---------------------------------------------------AI functions-------------------------------------------------'''
##These functions are going to be part of what determines which moves to be made by the computer

##dummy move so far
def getComputerMove(board, tile):
    global prevMove
    prevMove = AlphaBeta(board, 3, tile)
    return prevMove
'''
    for x in range(n):
        for y in range(n):
            if isValidMove(board, (x, y)):
                prevMove = (x, y)
                return (x, y)
'''


##generate the next set of possible states
def generateChildren(board, player):
    ##keeps a list of children
    cstates = []

    for i in range(n):
        for j in range(n):
            if isValidMove(board, (i, j)):
                cstates.append((copy.deepcopy(board), (i, j)))
                makeMove(cstates[-1][0], player, cstates[-1][1])
    return cstates

##I think we should take out depth at the end.
## also, would it be nice to do another search alg? or is AB always good?
def AlphaBeta(board, depth, player):
    m = minValue((board, -1), depth, player, (float("-inf"), -1), (float("inf"), -1))
    return m[1]

def maxValue(board, depth, player, alpha, beta):
    ##figure the opposite tile
    if player == '1':
        unplayer = '0'
    else:
        unplayer = '1'

    ##return heuristic if leaf
    if depth == 0:
        if player == '1':
            return (heuristic(board[0]), board[1])
        else:
            return (heuristic(board[0]), board[1])
    ##for each children find next
    for succ in generateChildren(board[0], player):
        m = minValue(succ, depth-1, unplayer, alpha, beta)
        if m[0] > alpha[0]:
            alpha = m
        if alpha[0] >= beta[0]:
            return alpha
    return alpha
    

def minValue(board, depth, player, alpha, beta):
    ##figure the opposite tile
    if player == '1':
        unplayer = '0'
    else:
        unplayer = '1'

    ##return heuristic if leaf
    if depth == 0:
        if player == '1':
            return (heuristic(board[0]), board[1])
        else:
            return (heuristic(board[0]), board[1])
    ##for each children find next
    for succ in generateChildren(board[0], player):
        m = maxValue(succ, depth-1 , unplayer, alpha, beta)
        if m[0] < beta[0]:
            beta = m
        if alpha[0] >= beta[0]:
            return beta
    return beta

##determine the value of a state
def heuristic(board):
    ##looks at the isWinner function to find # of possible MAX wins - # of possible MIN wins
    win_count = 0
    lose_count = 0

    tile = '1'
    untile = '0'

    # check horizontal spaces
    for y in range(n):
        for x in range(n):
            if (board[x][y] == tile or board[x][y] == ' ') and \
               (board[x+1][y] == tile or board[x+1][y] == ' ') and \
               (board[x+2][y] == tile or board[x+2][y] == ' ') and \
               (board[x+3][y] == tile or board[x+3][y] == ' '):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == ' ') and \
               (board[x+1][y] == untile or board[x+1][y] == ' ') and \
               (board[x+2][y] == untile or board[x+2][y] == ' ') and \
               (board[x+3][y] == untile or board[x+3][y] == ' '):
                lose_count += 1

    # check vertical spaces
    for x in range(n):
        for y in range(n):
            if (board[x][y] == tile or board[x][y] == ' ') and \
               (board[x][y+1] == tile or board[x][y+1] == ' ') and \
               (board[x][y+2] == tile or board[x][y+2] == ' ') and \
               (board[x][y+3] == tile or board[x][y+3] == ' '):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == ' ') and\
               (board[x][y+1] == untile or board[x][y+1] == ' ') and \
               (board[x][y+2] == untile or board[x][y+2] == ' ') and \
               (board[x][y+3] == untile or board[x][y+3] == ' '):
                lose_count += 1

    # check / diagonal spaces
    for x in range(n - 3):
        for y in range(3, n):
            if (board[x][y] == tile or board[x][y] == ' ') and \
               (board[x+1][y-1] == tile or board[x+1][y-1] == ' ') and \
               (board[x+2][y-2] == tile or board[x+2][y-2] == ' ') and \
               (board[x+3][y-3] == tile or board[x+3][y-3] == ' '):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == ' ') and \
               (board[x+1][y-1] == untile or board[x+1][y-1] == ' ') and \
               (board[x+2][y-2] == untile or board[x+2][y-2] == ' ') and \
               (board[x+3][y-3] == untile or board[x+3][y-3] == ' '):
                lose_count += 1

    # check \ diagonal spaces
    for x in range(n - 3):
        for y in range(n - 3):
            if (board[x][y] == tile or board[x][y] == ' ') and \
               (board[x+1][y+1] == tile or board[x+1][y+1] ==  ' ') and \
               (board[x+2][y+2] == tile or board[x+2][y+2] == ' ') and \
               (board[x+3][y+3] == tile or board[x+3][y+3] == ' '):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == ' ') and \
               (board[x+1][y+1] == untile or board[x+1][y+1] ==  ' ') and \
               (board[x+2][y+2] == untile or board[x+2][y+2] == ' ') and \
               (board[x+3][y+3] == untile or board[x+3][y+3] == ' '):
                lose_count += 1

    return win_count - lose_count
    #Given a board, returns the value of that board when evaluated with a heuristic
'''-----------------------------------------------------Game Functions-----------------------------------------------'''
##These game functions are the essential functions that help the game do move and detect winnings

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
        if (move[0] > 2 and move[1] < n-3 and\
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
