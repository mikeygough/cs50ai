"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    move_count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                move_count += 1
    if move_count % 2 == 1:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                # print(i, j)
                action = (i, j)
                actions.add(action)

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # get player
    p = player(board)
    # get actions
    a = actions(board)

    if action not in a:
        raise ValueError

    # generate new board
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = p

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            # vertical win
            try:
                if board[i][j] != None and board[i][j] == board[i+1][j] == board[i+2][j]:
                    return board[i][j]
            except (TypeError, IndexError):
                pass
            # horizontal win
            try:
                if board[i][j] != None and board[i][j] == board[i][j+1] == board[i][j+2]:
                    return board[i][j]
            except (TypeError, IndexError):
                pass
            # diagonal must pass through the center 
            if i-1 < 0 or j-1 < 0:
                pass
            else:
                # left diagonal
                try:
                    if board[i][j] != None and board[i][j] == board[i-1][j-1] == board[i+1][j+1]:
                        return board[i][j]
                except (TypeError, IndexError):
                    pass
                # right diagonal
                try:
                    if board[i][j] != None and board[i][j] == board[i+1][j-1] == board[i-1][j+1]:
                        return board[i][j]
                except (TypeError, IndexError):
                    pass
                
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None

    val_move = {}
    if player(board) == "X":
        for action in actions(board):
            val_move[action] = min_value(result(board, action))
        return max(val_move, key=lambda k: val_move[k])

    elif player(board) == "O":
        for action in actions(board):
            val_move[action] = max_value(result(board, action))
        return min(val_move, key=lambda k: val_move[k])

    # test random move
    # if terminal(board):
    #     return None
    # else:
    #     # test generate random action
    #     return random.choice(list(actions(board)))

    
