"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    counter = 0
    for row in board:
        counter += row.count(EMPTY)

    if counter % 2 != 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    else:
        boardcopy = copy.deepcopy(board)
        boardcopy[action[0]][action[1]] = player(board)
        return boardcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Rows
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != EMPTY:
            return(row[0])
    #Columns
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    #Diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
            return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or not any (EMPTY in row for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def min_value(board):
    """
    Returns the minimum utility value for a given board.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    """
    Returns the maximum utility value for a given board.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    
    util = 0

    if player(board) == X:
        if board == initial_state():
            return (1,1)
        for action in actions(board):
            if min_value(result(board, action)) >= util:
                util = min_value(result(board, action))
                f_move = action
    else:
        for action in actions(board):
            if max_value(result(board, action)) <= util:
                util = max_value(result(board, action))
                f_move = action
    return f_move
