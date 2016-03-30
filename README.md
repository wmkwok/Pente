# Pente
Implemention of PENTE board game with AI components

###Rules of the game
The objective of the game is to either get 5 consecutive pieces on a board, or capture 5 pairs of the opponent's pieces. Players are free to place their pieces wherever on any unoccupied board spot. Some rules to keep in mind:

1. A pair of the opponent's pieces mean two consecutive pieces that belong to the opponent
2. To capture, the player must place a piece which makes a pair bracketed by the player's. For example, in a certain row [a, b, b, a]
3. A player cannot cause themselves to be capture. For example, placing a 'b' where the row is [a, _, b, a]


###Game files
1. Pente.py
2. gameAI.py


###Pente.py functions
1. main(): the main function controls the flow of the game, turns of the player, and collecting the moves from players. It also keeps track of winning or not, although those functions are implemented in the game file.

2. playAgain(): The function determines if user wants to play again after a win/loss game

3. whoGoesFirst(): The function decides using randint whether the computer goes first or the human player.

4. getHumanMove(board, tile): asks the human player to move, displays the computer's last move, and make sure the move entered is valid in format


###gameAI.py functions
1. getComputerMove(board, tile): this calls all the necessary functions to calculate which move the computer will make. Returns a tuple

2. generateChildren(board, player): this creates a list of possible next game states.

3. AlphaBeta(board, depth, player): computes AlphaBeta algorithm with a cutoff depth.

4. maxValue(board, depth, player, alpha, beta): helper function of AlphaBeta to compute the max level selections

5. minValue(board, depth, player, alpha, beta): helper function of AlphaBeta to computer the min level selections

6. heuristic(board): where all the magical things happen and a magical prediction of best move will come up. Returns a number.

7. drawBoard(board): draws the board in a text format, visualization of the board for the player

8. getNewBoard(): creates a new board with all blank points

9. isValidMove(board, move): determines if a move on a board state is ok.

10. isCaptureMove(board, player, move):	counts pairs that are captured by this move as well as remove those captured pieces.

11. makeMove(board, player, move): makes a certain move, calls isCaptureMove to remove tiles and count captured pairs.

12. getPrevMove(): just returns the previous move of computer

13. isBoardFull(board): determines if a board is filled. returns a boolean

14. isWinner(board, tile): determines if a player has won. returns a boolean



