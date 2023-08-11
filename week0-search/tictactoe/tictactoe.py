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
    x_count = 0
    for i in range(len(board)):
        for j in range(len(board(i))):
            if j == "X":
                x_count += 1

    if x_count % 2 == 0:
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
                print(i, j)
                action = (i, j)
                actions.add(action)

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # get player
    player = player(board)
    # get actions
    actions = actions(board)

    if action not in actions:
        raise ValueError

    # generate new board
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            # check above
            try:
                if board[i][j] == board[i-1][j] & board[i-2][j]:
                    return board[i][j]
            except IndexError:
                pass
            # check upper right diagonal
            try:
                if board[i][j] == board[i+1][j+1] & board[i+2][j+2]:
                    return board[i][j]
            except IndexError:
                pass
            # check right
            try:
                if board[i][j] == board[i][j+1] & board[i][j+2]:
                    return board[i][j]
            except IndexError:
                pass
            # check lower right diagonal
            try:
                if board[i][j] == board[i+1][j+1] & board[i+2][j+2]:
                    return board[i][j]
            except IndexError:
                pass
            # check below
            try:
                if board[i][j] == board[i+1][j] & board[i+2][j]:
                    return board[i][j]
            except IndexError:
                pass
            # check lower left diagonal
            try:
                if board[i][j] == board[i+1][j-1] & board[i+2][j-1]:
                    return board[i][j]
            except IndexError:
                pass
            # check left
            try:
                if board[i][j] == board[i-1][j] & board[i-2][j]:
                    return board[i][j]
            except IndexError:
                pass
            # check upper left diagonal
            try:
                if board[i][j] == board[i-1][j-1] & board[i-2][j-2]:
                    return board[i][j]
            except IndexError:
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
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
