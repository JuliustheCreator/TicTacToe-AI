import pygame, sys, math
import numpy as np

pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 1000
LINE_WIDTH = 20
CIRCLE_WIDTH = 20
CROSS_WIDTH = 40
CIRCLE_RADIUS = 80
SPACE = 90

DARK_GRAY = ('#242222')
GRAY = ('#36393f')
WHITE = ('#F0FFF0')

BOARD_ROWS = 3
BOARD_COLS = 3

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe with AI')
screen.fill(GRAY)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)
def draw_lines():
    #Horizontal Lines
    pygame.draw.line(screen, DARK_GRAY, (0, 333), (1000,333), LINE_WIDTH)
    pygame.draw.line(screen, DARK_GRAY, (0, 666), (1000,666), LINE_WIDTH)

    #Vertical Lines
    pygame.draw.line(screen, DARK_GRAY, (333, 0), (333,1000), LINE_WIDTH)
    pygame.draw.line(screen, DARK_GRAY, (666, 0), (666,1000), LINE_WIDTH)

def mark_move(row, col, player):
    board[row][col] = player

def is_square_open(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle(screen, WHITE, (int(col * 333 + 166), int(row * 333 + 166)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 1:
                pygame.draw.line(screen, WHITE, (col * 333 + SPACE, row * 333 + 333 - SPACE), (col * 333 + 333 - SPACE, row * 333 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, WHITE, (col * 333 + SPACE, row * 333 + SPACE), (col * 333 + 333 - SPACE, row * 333 + 333 - SPACE), CROSS_WIDTH)

player = 1

draw_lines()
# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickX = event.pos[0]
            clickY = event.pos[1]
            clicked_row = math.floor(int(clickY/333))
            clicked_col = math.floor(int(clickX/333))
            if is_square_open(clicked_row,clicked_col):
                mark_move(clicked_row,clicked_col, player)
                if player == 1:
                    player = 2
                else:
                    player = 1
            draw_figures()

    pygame.display.update()