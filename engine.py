import math, numpy as np
from .board import is_square_open


player = 1

#Chooses AI based on Player (X or O)
def define_ai(player):
    return 2 / player

#Initial Starting Position
def initial_state():
    return np.zeros((3,3))

def player(board):
    count_1 = 0
    count_2 = 0
    for row in board:
        for col in board:
            if board[row][col] == 1:
                count_1 += 1
            elif board[row][col] == 2:
                count_2 += 1
            else:
                continue
    if count_1 == count_2:
        return 1
    else:
        return 2

def actions(board):
    avaliable_moves = set()
    for row in board:
        for col in board:
            if is_square_open(board[row][col]):
                avaliable_moves.add((row, col))

def result(board, action):
    pass
