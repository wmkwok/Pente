import sys
import copy
import timeit

prevMove = None
n = 10
bcaptures = 0
wcaptures = 0

'''
A game board looks like this
'''
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


'''--------------------------------------------AI Functions------------------------------------'''

def getComputerMove(board, tile):
    pass

'''
def getComputerMove(board, tile):
    global prevMove
    prevMove = AlphaBeta(board, 3, tile)
    return prevMove

    for x in range(n):
        for y in range(n):
            if isValidMove(board, (x, y)):
                prevMove = (x, y)
                return (x, y)
'''


# generate the set of next possible states
def generateChildren(board, tile):
    pass

'''
def generateChildren(board, player):
    ##keeps a list of children
    cstates = []

    for i in range(n):
        for j in range(n):
            if isValidMove(board, (i, j)):
                cstates.append((copy.deepcopy(board), (i, j)))
                makeMove(cstates[-1][0], player, cstates[-1][1])
    return cstates
'''

# AlphaBeta function to calculate best move
def alphaBeta(board, depth, tile):
    pass

'''
def AlphaBeta(board, depth, player):
    tik=timeit.default_timer()
    m = minValue((board, -1), depth, player, (float("-inf"), -1), (float("inf"), -1))
    tok=timeit.default_timer()
    print "Processing time: ", tok-tik
    return m[1]
'''

# maxValue for ab
def MaxValue(board, depth, tile, alpha, beta):
    pass

'''
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
            return (heuristic(board[0]) * -1, board[1])
    ##for each children find next
    for succ in generateChildren(board[0], player):
        m = minValue(succ, depth-1, unplayer, alpha, beta)
        if m[0] > alpha[0]:
            alpha = m
        if alpha[0] >= beta[0]:
            return alpha
    return alpha
'''

#minValue for ab
def minValue(board, depth, tile, alpha, beta):
    pass

'''
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
            return (heuristic(board[0]) * -1, board[1])
    ##for each children find next
    for succ in generateChildren(board[0], player):
        m = maxValue(succ, depth-1 , unplayer, alpha, beta)
        if m[0] < beta[0]:
            beta = m
        if alpha[0] >= beta[0]:
            return beta
    return beta
'''

'''------------------------------------------------------Heurisitic III--------------------------------------------'''
##determine the value of a state, taking advantage of capturing as many as can be to win.
def heuristic(board):
    capture_count = 0
    ncapture_count = 0
    
    tile = '1'
    untile = '0'

    #check horizontal
    for y in range(n):
        for x in range(n-3):
            if (board[x][y] == tile and board[x+1][y] == untile and \
               board[x+2][y] == '.') or \
            (board[x][y] == '.' and board[x+1][y] == untile and \
               board[x+2][y] == tile):
                capture_count += 1

            if (board[x][y] == tile and board[x+1][y] == untile and \
               board[x+2][y] == untile) or \
               (board[x+1][y] == untile and \
               board[x+2][y] == untile and board[x+3][y] == tile):
                capture_count += 2

            if (board[x][y] == untile and board[x+1][y] == tile and \
               board[x+2][y] == '.') or \
            (board[x][y] == '.' and board[x+1][y] == tile and \
               board[x+2][y] == untile):
                ncapture_count += 1

            if (board[x][y] == untile and board[x+1][y] == tile and \
               board[x+2][y] == tile) or \
               (board[x+1][y] == tile and \
               board[x+2][y] == tile and board[x+3][y] == untile):
                ncapture_count += 2
                
    #check vertical
    for x in range(n):
        for y in range(n-2):
            if (board[x][y] == tile and board[x][y+1] == untile and \
               board[x][y+1] == '.') or \
            (board[x][y] == '.' and board[x][y+1] == untile and \
               board[x][y+1] == tile):
                capture_count += 1

            if (board[x][y] == tile and board[x][y+1] == untile and \
               board[x][y+2] == untile) or \
               (board[x][y] == untile and \
               board[x][y+1] == untile and board[x][y+2] == tile):
                capture_count += 2

            if (board[x][y] == untile and board[x][y+1] == tile and \
               board[x][y+2] == '.') or \
            (board[x][y] == '.' and board[x][y+1] == tile and \
               board[x][y+2] == untile):
                ncapture_count += 1

            if (board[x][y] == untile and board[x][y+1] == tile and \
               board[x][y+2] == tile) or \
               (board[x][y] == tile and \
               board[x][y+1] == tile and board[x][y+2] == untile):
                ncapture_count += 2
    #diagonal /
    for x in range(n - 2):
        for y in range(2, n):
            if (board[x][y] == tile and board[x+1][y-1] == untile and \
               board[x+2][y-2] == '.') or \
            (board[x][y] == '.' and board[x+1][y-1] == untile and \
               board[x+2][y-2] == tile):
                capture_count += 1

            if (board[x][y] == tile and board[x+1][y-1] == untile and \
               board[x+2][y-2] == untile) or \
               (board[x][y] == untile and \
               board[x+1][y-1] == untile and board[x+2][y-2] == tile):
                capture_count += 2

            if (board[x][y] == untile and board[x+1][y-1] == tile and \
               board[x+2][y-2] == '.') or \
            (board[x][y] == '.' and board[x+1][y-1] == tile and \
               board[x+2][y-2] == untile):
                ncapture_count += 1

            if (board[x][y] == untile and board[x+1][y-1] == tile and \
               board[x+2][y-2] == tile) or \
               (board[x][y] == tile and \
               board[x+1][y-1] == tile and board[x+2][y-2] == untile):
                ncapture_count += 2

    #diagonal \
    for x in range(n - 4):
        for y in range(n - 4):
            if (board[x][y] == tile and board[x+1][y-1] == untile and \
               board[x+2][y+2] == '.') or \
            (board[x][y] == '.' and board[x+1][y-1] == untile and \
               board[x+2][y+2] == tile):
                capture_count += 1

            if (board[x][y] == tile and board[x+1][y-1] == untile and \
               board[x+2][y+2] == untile) or \
               (board[x][y] == untile and \
               board[x+1][y-1] == untile and board[x+2][y+2] == tile):
                capture_count += 2

            if (board[x][y] == untile and board[x+1][y-1] == tile and \
               board[x+2][y+2] == '.') or \
            (board[x][y] == '.' and board[x+1][y-1] == tile and \
               board[x+2][y+2] == untile):
                ncapture_count += 1

            if (board[x][y] == untile and board[x+1][y-1] == tile and \
               board[x+2][y+2] == tile) or \
               (board[x][y] == tile and \
               board[x+1][y-1] == tile and board[x+2][y+2] == untile):
                ncapture_count += 2

    return capture_count - ncapture_count


'''----------------------------------------------------Heuristic II----------------------------'''

##determine the value of a state, based on whether the next available state allows for Trias, or block Trias.
def heuristic2(board):
    tria_count = 0
    ntria_count = 0

    tile = '1'
    untile = '0'

    #check horizontal spaces for 2 in a rows or block 3 in a rows
    for y in range(n):
        for x in range(n-4):
            if (board[x][y] == '.') and (board[x+1][y] == tile) and \
               (board[x+2][y] == '.'):
                tria_count += 1

            if (board[x][y] == '.') and (board[x+1][y] == tile) and \
               (board[x+2][y] == tile and board[x+3][y] == '.'):
                tria_count += 2

            if (board[x][y] == '.') and (board[x+1][y] == tile) and \
               (board[x+2][y] == tile and board[x+3][y] == tile) and \
               board[x+4][y] == '.':
                tria_count += 3

            if (board[x][y] == '.') and (board[x+1][y] == untile) and \
               (board[x+2][y] == '.'):
                ntria_count += 1

            if (board[x][y] == '.') and (board[x+1][y] == untile) and \
               (board[x+2][y] == untile and board[x+3][y] == '.'):
                ntria_count += 2

            if (board[x][y] == '.') and (board[x+1][y] == untile) and \
               (board[x+2][y] == untile and board[x+3][y] == untile) and \
               board[x+4][y] == '.':
                ntria_count += 3

    #check vertical spaces for 2 in a rows or block 3 in a rows
    for x in range(n):
        for y in range(n-4):
            if (board[x][y] == '.' and board[x][y+1] == tile) and \
               (board[x][y+2] == '.'):
                tria_count += 1

            if (board[x][y] == '.' and board[x][y+1] == tile) and \
               (board[x][y+2] == tile and board[x][y+3] == '.'):
                tria_count += 2

            if (board[x][y] == '.' and board[x][y+1] == tile) and \
               (board[x][y+2] == tile and board[x][y+3] == tile) and \
               (board[x][y+4] == '.'):
                tria_count += 3

            if (board[x][y] == '.' and board[x][y+1] == untile) and \
               (board[x][y+2] == '.'):
                ntria_count += 1

            if (board[x][y] == '.' and board[x][y+1] == untile) and \
               (board[x][y+2] == untile and board[x][y+3] == '.'):
                ntria_count += 2

            if (board[x][y] == '.' and board[x][y+1] == untile) and \
               (board[x][y+2] == untile and board[x][y+3] == untile) and \
               (board[x][y+4] == '.'):
                ntria_count += 3

    #check diagonal /
    for x in range(n - 4):
        for y in range(4, n):
            if (board[x][y] == '.' and board[x][y] == tile) and \
               (board[x+1][y-1] == '.'):
                tria_count += 1

            if (board[x][y] == '.' and board[x][y] == tile) and \
               (board[x+1][y-1] == tile and board[x+2][y-2] == '.'):
                tria_count += 2

            if (board[x][y] == '.' and board[x][y] == tile) and \
               (board[x+1][y-1] == tile and board[x+2][y-2] == tile) and \
               (board[x+3][y-3] == '.'):
                tria_count += 3

            if (board[x][y] == '.' and board[x][y] == untile) and \
               (board[x+1][y-1] == '.'):
                ntria_count += 1

            if (board[x][y] == '.' and board[x][y] == untile) and \
               (board[x+1][y-1] == untile and board[x+2][y-2] == '.'):
                ntria_count += 2

            if (board[x][y] == '.' and board[x][y] == untile) and \
               (board[x+1][y-1] == untile and board[x+2][y-2] == untile) and \
               (board[x+3][y-3] == '.'):
                ntria_count += 3

    #check diagonal \
    for x in range(n - 4):
        for y in range(n - 4):
            if (board[x][y] == '.' and board[x+1][y+1] == tile) and \
               (board[x+2][y+2] == '.'):
                tria_count += 1

            if (board[x][y] == '.' and board[x+1][y+1] == tile) and \
               (board[x+2][y+2] == tile and  board[x+3][y+3] == '.'):
                tria_count += 2

            if (board[x][y] == '.' and board[x+1][y+1] == tile) and \
               (board[x+2][y+2] == tile and  board[x+3][y+3] == tile) and \
               (board[x+4][y+4] == '.'):
                tria_count += 3

            if (board[x][y] == '.' and board[x+1][y+1] == untile) and \
               (board[x+2][y+2] == '.'):
                ntria_count += 1

            if (board[x][y] == '.' and board[x+1][y+1] == untile) and \
               (board[x+2][y+2] == untile and  board[x+3][y+3] == '.'):
                ntria_count += 2

            if (board[x][y] == '.' and board[x+1][y+1] == untile) and \
               (board[x+2][y+2] == untile and  board[x+3][y+3] == untile) and \
               (board[x+4][y+4] == '.'):
                ntria_count += 3

    return tria_count - ntria_count


'''-------------------------------------------Heuristic I -----------------------------------------------'''

##determine the value of a state, based on number of availble 5-row win states.
def heuristic1(board):
    ##looks at the isWinner function to find # of possible MAX wins - # of possible MIN wins
    win_count = 0
    lose_count = 0

    tile = '1'
    untile = '0'

    # check horizontal spaces
    for y in range(n):
        for x in range(n-4):
            if (board[x][y] == tile or board[x][y] == '.') and \
               (board[x+1][y] == tile or board[x+1][y] == '.') and \
               (board[x+2][y] == tile or board[x+2][y] == '.') and \
               (board[x+3][y] == tile or board[x+3][y] == '.') and \
               (board[x+4][y] == tile or board[x+4][y] == '.'):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == '.') and \
               (board[x+1][y] == untile or board[x+1][y] == '.') and \
               (board[x+2][y] == untile or board[x+2][y] == '.') and \
               (board[x+3][y] == untile or board[x+3][y] == '.') and \
               (board[x+4][y] == untile or board[x+4][y] == '.'):
                lose_count += 1

    # check vertical spaces
    for x in range(n):
        for y in range(n-4):
            if (board[x][y] == tile or board[x][y] == '.') and \
               (board[x][y+1] == tile or board[x][y+1] == '.') and \
               (board[x][y+2] == tile or board[x][y+2] == '.') and \
               (board[x][y+3] == tile or board[x][y+3] == '.') and \
               (board[x][y+4] == tile or board[x][y+4] == '.'):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == '.') and\
               (board[x][y+1] == untile or board[x][y+1] == '.') and \
               (board[x][y+2] == untile or board[x][y+2] == '.') and \
               (board[x][y+3] == untile or board[x][y+3] == '.') and \
               (board[x][y+4] == untile or board[x][y+4] == '.'):
                lose_count += 1

    # check / diagonal spaces
    for x in range(n - 4):
        for y in range(4, n):
            if (board[x][y] == tile or board[x][y] == '.') and \
               (board[x+1][y-1] == tile or board[x+1][y-1] == '.') and \
               (board[x+2][y-2] == tile or board[x+2][y-2] == '.') and \
               (board[x+3][y-3] == tile or board[x+3][y-3] == '.') and \
               (board[x+4][y-4] == tile or board[x+4][y-4] == '.'):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == '.') and \
               (board[x+1][y-1] == untile or board[x+1][y-1] == '.') and \
               (board[x+2][y-2] == untile or board[x+2][y-2] == '.') and \
               (board[x+3][y-3] == untile or board[x+3][y-3] == '.') and \
               (board[x+4][y-4] == untile or board[x+4][y-4] == '.'):
                lose_count += 1

    # check \ diagonal spaces
    for x in range(n - 4):
        for y in range(n - 4):
            if (board[x][y] == tile or board[x][y] == '.') and \
               (board[x+1][y+1] == tile or board[x+1][y+1] ==  '.') and \
               (board[x+2][y+2] == tile or board[x+2][y+2] == '.') and \
               (board[x+3][y+3] == tile or board[x+3][y+3] == '.') and \
               (board[x+4][y+4] == tile or board[x+3][y+4] == '.'):
                win_count += 1

            if (board[x][y] == untile or board[x][y] == '.') and \
               (board[x+1][y+1] == untile or board[x+1][y+1] ==  '.') and \
               (board[x+2][y+2] == untile or board[x+2][y+2] == '.') and \
               (board[x+3][y+3] == untile or board[x+3][y+3] == '.') and \
               (board[x+4][y+4] == untile or board[x+4][y+4] == '.'):
                lose_count += 1

##    print "heuristic: ", win_count, lose_count, win_count - lose_count
    return win_count - lose_count


'''------------------------------------------------Game Functions----------------------------------------'''

def drawBoard(board):
    pass

'''
def drawBoard(board):
    boarder = ""

    ##add in the top border
    boarder += "$$   "
    for i in range(n*2+1):
        boarder += '-'
    boarder += '\n'

    ##add in row
    for row in range(n):
        if row >= 9:
            boarder += "$$%d| " %(row+1)
        else:
            boarder += "$$%d | " %(row+1)
        for col in range(n):
            if board[row][col] == '1':
                boarder += u"\u25CF "
            elif board[row][col] == '0':
                boarder += u"\u25CB "
            else:
                boarder += ". "
        boarder += "|\n"

    ##add in the bottom border
    boarder += "$$   "
    for i in range(n*2+1):
        boarder += '-'
    boarder += '\n'
    print boarder
'''

def getNewBoard():
    # creates a fresh board
    pass

'''
def getNewBoard():
    newBoard = []
    theRow = []
    for i in range(n):
        theRow.append('.')
    for j in range(n):
        newBoard.append(copy.deepcopy(theRow))
    return newBoard
'''

def isValidMove(board, move):
    # determines is the move is a valid one
    pass

'''
def isValidMove(board, move):
    if move[0] >= 0 and move[0] < n and move[1] >= 0 and move[1] < n:
        return (board[move[0]][move[1]] == '.')
    return False
'''


def isCapturedMove(board, tile, move):
    # check if the move creates a capture
    pass

'''
def isCaptureMove(board, player, move):
    ##check to see if the move made is going to capture
    ccount = 0
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
        ccount += 1
        
    if (move[1] < n-3 and \
            board[move[0]][move[1]+1] == unplayer and \
            board[move[0]][move[1]+2] == unplayer and \
            board[move[0]][move[1]+3] == player):
        board[move[0]][move[1]+1] = '.'
        board[move[0]][move[1]+2] = '.'
        ccount += 1
        
    ##check vertical captures
    if (move[0] > 2 and \
            board[move[0]-1][move[1]] == unplayer and \
            board[move[0]-2][move[1]] == unplayer and \
            board[move[0]-3][move[1]] == player):
        board[move[0]-1][move[1]] = '.'
        board[move[0]-2][move[1]] = '.'
        ccount += 1
        
    if (move[0] < n-3 and \
            board[move[0]+1][move[1]] == unplayer and \
            board[move[0]+2][move[1]] == unplayer and \
            board[move[0]+3][move[1]] == player):
        board[move[0]+1][move[1]] = '.'
        board[move[0]+2][move[1]] = '.'
        ccount += 1

    ##check diagonal cpatures
    if (move[0] > 2 and move[1] > 2 and\
            board[move[0]-1][move[1]-1] == unplayer and \
            board[move[0]-2][move[1]-2] == unplayer and \
            board[move[0]-3][move[1]-3] == player):
        board[move[0]-1][move[1]-1] = '.'
        board[move[0]-2][move[1]-2] = '.'
        ccount += 1
        
    if (move[0] < n-3 and move[1] < n-3 and\
            board[move[0]+1][move[1]+1] == unplayer and \
            board[move[0]+2][move[1]+2] == unplayer and \
            board[move[0]+3][move[1]+3] == player):
        board[move[0]+1][move[1]+1] = '.'
        board[move[0]+2][move[1]+2] = '.'
        ccount += 1
        
    ##check other diagonal captures
    if (move[0] > 2 and move[1] < n-3 and\
            board[move[0]-1][move[1]+1] == unplayer and \
            board[move[0]-2][move[1]+2] == unplayer and \
            board[move[0]-3][move[1]+3] == player):
        board[move[0]-1][move[1]+1] = '.'
        board[move[0]-2][move[1]+2] = '.'
        ccount += 1
        
    if (move[0] < n-3 and move[1] < n-3 and\
            board[move[0]+1][move[1]-1] == unplayer and \
            board[move[0]+2][move[1]-2] == unplayer and \
            board[move[0]+3][move[1]-3] == player):
        board[move[0]+1][move[1]-1] = '.'
        board[move[0]+2][move[1]-2] = '.'
        ccount += 1

    return ccount
'''

def makeMove(board, tile, move):
    # changes the board state
    pass

'''
    global wcaptures, bcaptures
    captures = isCaptureMove(board, player, move)
    board[move[0]][move[1]] = player
'''

'''

def makeCMove(board, player, move):
    global wcaptures, bcaptures
    captures = isCaptureMove(board, player, move)
    board[move[0]][move[1]] = player
    if captures != 0:
        if player == '0':
            wcaptures += captures
        else:
            bcaptures += captures
    print bcaptures, wcaptures
'''

def getPrevMove():
    #just returns the global previous move
    return prevMove

def isBoardFull(board):
    # check is the board is filled up
    pass

'''
def isBoardFull(board):
    for row in range(n):
        for col in range(n):
            if board[row][col] == '.':
                return False
    return True
'''

def isWinner(board, tile):
    #check if the player has won
    pass

'''
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
    if tile == '1':
        if wcaptures >= 5:
            return True
    else:
        if bcaptures >= 5:
            return True
    return False
'''

'''----------------------------Test area----------------------------------'''

'''
##this is 0 
print u"\u25CB"
##this is 1
print u"\u25CF"
'''
