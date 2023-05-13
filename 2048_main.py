import numpy
from utilities import generate_piece, print_board
DEV_MODE = False


def game_begin(board):  # Initialize board
    for i in range(2):
        rand_value = generate_piece(board)
        board[rand_value["row"]][rand_value["column"]] = rand_value["value"]
    print_board(board)
    return board


def rand_num(board):  # Add random num
    rand_value = generate_piece(board)
    board[rand_value["row"]][rand_value["column"]] = rand_value["value"]
    return (board)


def check_zero(one_row):  # Check if it's zero, shift left
    for j in range(3):
        for i in range(3, 0, -1):
            if one_row[i - 1] == 0:
                one_row[i], one_row[i - 1] = 0, one_row[i]
    return one_row


def move_left_row(r):  # Check if it's identical value, add left
    check_zero(r)
    for i in range(3):
        if r[i] == r[i + 1]:
            r[i] = r[i] * 2
            r[i + 1] = 0
    check_zero(r)
    return r


def move_left_whole(board):  # merge left
    board[0] = move_left_row(board[0])
    board[1] = move_left_row(board[1])
    board[2] = move_left_row(board[2])
    board[3] = move_left_row(board[3])
    return board


def reverse(board):
    board = numpy.fliplr(board)
    return board


def move_right_whole(board):  # merge right
    board = reverse(board)
    board = move_left_whole(board)
    board = reverse(board)
    return board


def transpose(board):  # Switch position of column and rows
    board = numpy.transpose(board)
    return board


def move_up_whole(board):  # Merge up
    board = transpose(board)  # Transpose
    board = move_left_whole(board)  # merge
    board = transpose(board)  # Transpose again to original
    return board


def move_down_whole(board):  # Merge down
    board = transpose(board)
    board = move_right_whole(board)
    board = transpose(board)
    return board


def main(game_board):

    command = ["A", "a", "W", "w", "S", "s", "D", "d", "Q", "q"]
    game_begin(game_board)
    while game_over(game_board) != True:
        control = input("Press a/w/s/d:")
        status = False
        before = game_board[:]
        if control == command[0] or control == command[1]:
            game_board = move_left_whole(game_board)
        elif control == command[2] or control == command[3]:
            game_board = move_up_whole(game_board)
        elif control == command[4] or control == command[5]:
            game_board = move_down_whole(game_board)
        elif control == command[6] or control == command[7]:
            game_board = move_right_whole(game_board)
        elif control == command[8] or command[9]:
            print("Exit Game")
            break
        elif control not in command:
            return False
        rand_num(game_board)
        print_board(game_board)
    return game_board


def game_over(game_board):
    statusF = False
    statisT = True
    for i in game_board:
        if 2048 in i:
            return statisT
        elif 0 in i:
            return statusF
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == game_board[i][j+1]:
                return statusF
            elif game_board[i][j] == game_board[i+1][j]:
                return statusF
    for i in range(3):
        if game_board[i][-1] == game_board[i+1][-1]:
            return statusF
        elif game_board[-1][i] == game_board[-1][i+1]:
            return statusF
    return statisT


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
