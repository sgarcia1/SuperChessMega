import numpy as np
import time


def rook_valid_moves_white(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0:  # run for all spaces above rook
        row_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7:  # run for all spaces below rook
        row_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check > 0:  # run for all spaces left of rook
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check < 7:  # run for all spaces right of rook
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def bishop_valid_moves_white(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
        row_check -= 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
        row_check -= 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
        row_check += 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
        row_check += 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def queen_valid_moves_white(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0:  # run for all spaces above
        row_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7:  # run for all spaces below
        row_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check > 0:  # run for all spaces to the left
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check < 7:  # run for all spaces to the right
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
        row_check -= 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
        row_check -= 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
        row_check += 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
        row_check += 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def knight_valid_moves_white(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    row_check -= 2
    col_check -= 1

    if row_check >= 0 and col_check >= 0:  # checking top left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 2
    col_check = col + 1

    if row_check >= 0 and col_check <= 7:  # checking top right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 2
    col_check = col - 1

    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 2
    col_check = col + 1

    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col - 2

    if row_check >= 0 and col_check >= 0:  # checking left upper spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col - 2

    if row_check <= 7 and col_check >= 0:  # checking left lower spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col + 2

    if row_check >= 0 and col_check <= 7:  # checking right upper spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col + 2

    if row_check <= 7 and col_check <= 7:  # checking right lower spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    # print(available)
    return available


def pawn_valid_moves_white(row, col, board):
    available = np.zeros((8, 8))

    row_check = row - 1
    col_check = col

    if row_check >= 0:  # checking one up spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1

    row_check = row - 2
    col_check = col

    if row_check >= 0 and row == 6:  # checking two up spot and that pawn has not moved yet
        check_value1 = board[row_check][col_check]
        check_value2 = board[row_check + 1][col_check]
        if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col - 1

    if row_check >= 0 and col_check >= 0:  # checking left attack spot
        check_value = board[row_check][col_check]
        if 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
        # add en passont

    row_check = row - 1
    col_check = col + 1

    if row_check >= 0 and col_check <= 7:  # checking right attack spot
        check_value = board[row_check][col_check]
        if 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1
        # add en passont

    return available


def king_valid_moves_white(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    row_check -= 1

    if row_check >= 0:  # checking top spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1

    if row_check <= 7:  # checking bottom spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row
    col_check = col - 1

    if col_check >= 0:  # checking left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    col_check = col + 1

    if col_check <= 7:  # checking right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col - 1

    if row_check >= 0 and col_check >= 0:  # checking top left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col - 1

    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col + 1

    if row_check >= 0 and col_check <= 7:  # checking top right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col + 1

    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 101 <= check_value <= 116:  # if space has enemy
            available[row_check, col_check] = 1

    # print(available)
    return available


def rook_valid_moves_black(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0:  # run for all spaces above rook
        row_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7:  # run for all spaces below rook
        row_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check > 0:  # run for all spaces left of rook
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check < 7:  # run for all spaces right of rook
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def bishop_valid_moves_black(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
        row_check -= 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
        row_check -= 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
        row_check += 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
        row_check += 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def queen_valid_moves_black(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    while row_check > 0:  # run for all spaces above
        row_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7:  # run for all spaces below
        row_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check > 0:  # run for all spaces to the left
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while col_check < 7:  # run for all spaces to the right
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
        row_check -= 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
        row_check -= 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
        row_check += 1
        col_check -= 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    row_check = row
    col_check = col

    while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
        row_check += 1
        col_check += 1
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
            break
        else:  # if your own piece is in the space
            break

    return available


def knight_valid_moves_black(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    row_check -= 2
    col_check -= 1

    if row_check >= 0 and col_check >= 0:  # checking top left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 2
    col_check = col + 1

    if row_check >= 0 and col_check <= 7:  # checking top right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 2
    col_check = col - 1

    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 2
    col_check = col + 1

    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col - 2

    if row_check >= 0 and col_check >= 0:  # checking left upper spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col - 2

    if row_check <= 7 and col_check >= 0:  # checking left lower spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col + 2

    if row_check >= 0 and col_check <= 7:  # checking right upper spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col + 2

    if row_check <= 7 and col_check <= 7:  # checking right lower spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    # print(available)
    return available


def pawn_valid_moves_black(row, col, board):
    available = np.zeros((8, 8))

    row_check = row + 1
    col_check = col

    if row_check <= 7:  # checking one up spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1

    row_check = row + 2
    col_check = col

    if row_check <= 7 and row == 1:  # checking two up spot and if have moved yet
        check_value1 = board[row_check][col_check]
        check_value2 = board[row_check - 1][col_check]
        if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col - 1

    if row_check <= 7 and col_check >= 0:  # checking left attack spot
        check_value = board[row_check][col_check]
        if 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
        # add en passont

    row_check = row + 1
    col_check = col + 1

    if row_check <= 7 and col_check <= 7:  # checking right attack spot
        check_value = board[row_check][col_check]
        if 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1
        # add en passont

    return available


def king_valid_moves_black(row, col, board):
    row_check = row
    col_check = col
    available = np.zeros((8, 8))

    row_check -= 1

    if row_check >= 0:  # checking top spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1

    if row_check <= 7:  # checking bottom spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row
    col_check = col - 1

    if col_check >= 0:  # checking left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    col_check = col + 1

    if col_check <= 7:  # checking right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col - 1

    if row_check >= 0 and col_check >= 0:  # checking top left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col - 1

    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row - 1
    col_check = col + 1

    if row_check >= 0 and col_check <= 7:  # checking top right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    row_check = row + 1
    col_check = col + 1

    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
        check_value = board[row_check][col_check]
        if check_value == 0:  # if space is empty
            available[row_check, col_check] = 1
        elif 1 <= check_value <= 16:  # if space has enemy
            available[row_check, col_check] = 1

    # print(available)
    return available


def check_valid_move_white(row, col, r, c, board):
    p = board[row][col]

    #  simple checks
    if row == r and col == c:  # check if not moved
        return False

    elif 1 <= board[r][c] <= 16:  # check if moving into white piece
        return False

    # elif move_puts_in_check(row, col, r, c):  # check if move puts you in check

    else:  # check valid moves for the specific type of piece

        if 1 <= p <= 8:  # pawn
            # print('pawn')
            available = pawn_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 9 or p == 16:  # rook
            # print('rook')
            if r != row and c != col:  # must move in a line
                return False
            else:  # check if moving spot is in set of all allowed piece moves
                available = rook_valid_moves_white(row, col, board)
                if available[r, c] == 1:
                    return True
                else:
                    return False

        elif p == 10 or p == 15:  # knight
            # print('knight')
            available = knight_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 11 or p == 14:  # bishop
            # print('bishop')
            if r == row or c == col:  # cant move in a straight line
                return False
            else:  # check if moving spot is in set of all allowed piece moves
                available = bishop_valid_moves_white(row, col, board)
                if available[r, c] == 1:
                    return True
                else:
                    return False

        elif p == 12:  # queen
            # print('queen')
            available = queen_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 13:  # king
            # print('king')
            available = king_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False


def check_valid_move_black(row, col, r, c, board):
    p = board[row][col]

    #  simple checks
    if row == r and col == c:  # check if not moved
        return False

    elif 101 <= board[r][c] <= 116:  # check if moving into black piece
        return False

    # elif move_puts_in_check(row, col, r, c):  # check if move puts you in check

    else:  # check valid moves for the specific type of piece

        if 109 <= p <= 116:  # pawn
            # print('pawn')
            available = pawn_valid_moves_black(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 101 or p == 108:  # rook
            # print('rook')
            if r != row and c != col:  # must move in a line
                return False
            else:  # check if moving spot is in set of all allowed piece moves
                available = rook_valid_moves_white(row, col, board)
                if available[r, c] == 1:
                    return True
                else:
                    return False

        elif p == 102 or p == 107:  # knight
            # print('knight')
            available = knight_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 103 or p == 106:  # bishop
            # print('bishop')
            if r == row or c == col:  # cant move in a straight line
                return False
            else:  # check if moving spot is in set of all allowed piece moves
                available = bishop_valid_moves_white(row, col, board)
                if available[r, c] == 1:
                    return True
                else:
                    return False

        elif p == 104:  # queen
            # print('queen')
            available = queen_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False

        elif p == 105:  # king
            # print('king')
            available = king_valid_moves_white(row, col, board)
            if available[r, c] == 1:
                return True
            else:
                return False


#def moves_black(board):
#    #  initialize all move lists
#    pawn_moves = []
#    rook_moves = []
#    knight_moves = []
#    bishop_moves = []
#    queen_moves = []
#    king_moves = []
#
#    # scan through board to get all available moves
#    for i in range(8):  # loop through rows
#        for j in range(8):  # loop through columns
#            p = board[i][j]
#
#            if 109 <= p <= 116:  # pawn
#                # print('pawn')
#                available = pawn_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            pawn_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 101 or p == 108:  # rook
#                # print('rook')
#                available = rook_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            rook_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 102 or p == 107:  # knight
#                # print('knight')
#                available = knight_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            knight_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 103 or p == 106:  # bishop
#                # print('bishop')
#                available = bishop_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            bishop_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 104:  # queen
#                # print('queen')
#                available = queen_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            queen_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 105:  # king
#                # print('king')
#                available = king_valid_moves_black(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            king_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#    moves = [pawn_moves, rook_moves, knight_moves, bishop_moves, queen_moves, king_moves]
#    # print(moves)
#    return moves


def boards_black(board, black_num_pieces):
    boards = []

    # counter = 0
    pieces_checked = 0
    outer_loop_must_break = False

    # scan through board to get all available moves
    for row in range(8):  # loop through rows
        for col in range(8):  # loop through columns
            if pieces_checked >= black_num_pieces:
                outer_loop_must_break = True
                break

            # time1 = time.time()
            p = board[row][col]
            # counter += 1

            if 109 <= p <= 116:  # pawn
                # print('pawn')
                pieces_checked += 1

                row_check = row + 1
                col_check = col

                if row_check <= 7:  # checking one up spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 2
                col_check = col

                if row_check <= 7 and row == 1:  # checking two up spot and if have moved yet
                    check_value1 = board[row_check][col_check]
                    check_value2 = board[row_check - 1][col_check]
                    if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col - 1

                if row_check <= 7 and col_check >= 0:  # checking left attack spot
                    check_value = board[row_check][col_check]
                    if 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    # add en passont

                row_check = row + 1
                col_check = col + 1

                if row_check <= 7 and col_check <= 7:  # checking right attack spot
                    check_value = board[row_check][col_check]
                    if 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    # add en passont

            elif p == 101 or p == 108:  # rook
                # print('rook')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0:  # run for all spaces above rook
                    row_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7:  # run for all spaces below rook
                    row_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check > 0:  # run for all spaces left of rook
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check < 7:  # run for all spaces right of rook
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 102 or p == 107:  # knight
                # print('knight')
                pieces_checked += 1

                row_check = row - 2
                col_check = col - 1

                if row_check >= 0 and col_check >= 0:  # checking top left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 2
                col_check = col + 1

                if row_check >= 0 and col_check <= 7:  # checking top right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 2
                col_check = col - 1

                if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 2
                col_check = col + 1

                if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col - 2

                if row_check >= 0 and col_check >= 0:  # checking left upper spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col - 2

                if row_check <= 7 and col_check >= 0:  # checking left lower spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col + 2

                if row_check >= 0 and col_check <= 7:  # checking right upper spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col + 2

                if row_check <= 7 and col_check <= 7:  # checking right lower spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

            elif p == 103 or p == 106:  # bishop
                # print('bishop')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
                    row_check -= 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
                    row_check -= 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
                    row_check += 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
                    row_check += 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 104:  # queen
                # print('queen')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0:  # run for all spaces above
                    row_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7:  # run for all spaces below
                    row_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check > 0:  # run for all spaces to the left
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check < 7:  # run for all spaces to the right
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
                    row_check -= 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
                    row_check -= 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
                    row_check += 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
                    row_check += 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 105:  # king
                # print('king')
                pieces_checked += 1

                row_check = row - 1
                col_check = col

                if row_check >= 0:  # checking top spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1

                if row_check <= 7:  # checking bottom spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row
                col_check = col - 1

                if col_check >= 0:  # checking left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                col_check = col + 1

                if col_check <= 7:  # checking right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col - 1

                if row_check >= 0 and col_check >= 0:  # checking top left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col - 1

                if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col + 1

                if row_check >= 0 and col_check <= 7:  # checking top right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col + 1

                if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 1 <= check_value <= 16:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

        if outer_loop_must_break:
            break

        # time2 = time.time()
        # print('loop time = ', time2)

    # end = time.time()

    # print('counter = ', counter)
    # print('pieces_checked = ', pieces_checked)

    # print('TOTAL TIME = ', end - start)
    # print(len(boards))
    return boards


def boards_white(board, white_num_pieces):
    boards = []

    # counter = 0
    pieces_checked = 0
    outer_loop_must_break = False

    # scan through board to get all available moves
    for row in range(8):  # loop through rows
        for col in range(8):  # loop through columns
            if pieces_checked >= white_num_pieces:
                outer_loop_must_break = True
                break

            p = board[row][col]

            if 1 <= p <= 8:  # pawn
                # print('pawn')
                pieces_checked += 1

                row_check = row - 1
                col_check = col

                if row_check >= 0:  # checking one up spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 2
                col_check = col

                if row_check >= 0 and row == 6:  # checking two up spot and that pawn has not moved yet
                    check_value1 = board[row_check][col_check]
                    check_value2 = board[row_check + 1][col_check]
                    if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col - 1

                if row_check >= 0 and col_check >= 0:  # checking left attack spot
                    check_value = board[row_check][col_check]
                    if 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    # add en passont

                row_check = row - 1
                col_check = col + 1

                if row_check >= 0 and col_check <= 7:  # checking right attack spot
                    check_value = board[row_check][col_check]
                    if 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    # add en passont

            elif p == 9 or p == 16:  # rook
                # print('rook')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0:  # run for all spaces above rook
                    row_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7:  # run for all spaces below rook
                    row_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check > 0:  # run for all spaces left of rook
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check < 7:  # run for all spaces right of rook
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 10 or p == 15:  # knight
                # print('knight')
                pieces_checked += 1

                row_check = row - 2
                col_check = col - 1

                if row_check >= 0 and col_check >= 0:  # checking top left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 2
                col_check = col + 1

                if row_check >= 0 and col_check <= 7:  # checking top right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 2
                col_check = col - 1

                if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 2
                col_check = col + 1

                if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col - 2

                if row_check >= 0 and col_check >= 0:  # checking left upper spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col - 2

                if row_check <= 7 and col_check >= 0:  # checking left lower spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col + 2

                if row_check >= 0 and col_check <= 7:  # checking right upper spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col + 2

                if row_check <= 7 and col_check <= 7:  # checking right lower spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

            elif p == 11 or p == 14:  # bishop
                # print('bishop')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
                    row_check -= 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
                    row_check -= 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
                    row_check += 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
                    row_check += 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 12:  # queen
                # print('queen')
                pieces_checked += 1

                row_check = row
                col_check = col

                while row_check > 0:  # run for all spaces above
                    row_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7:  # run for all spaces below
                    row_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check > 0:  # run for all spaces to the left
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while col_check < 7:  # run for all spaces to the right
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
                    row_check -= 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check > 0 and col_check < 7:  # run for all spaces in the top right direction
                    row_check -= 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check > 0:  # run for all spaces in the bottom left direction
                    row_check += 1
                    col_check -= 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

                row_check = row
                col_check = col

                while row_check < 7 and col_check < 7:  # run for all spaces in the bottom right direction
                    row_check += 1
                    col_check += 1
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                        break
                    else:  # if your own piece is in the space
                        break

            elif p == 13:  # king
                # print('king')
                pieces_checked += 1

                row_check = row - 1
                col_check = col

                if row_check >= 0:  # checking top spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1

                if row_check <= 7:  # checking bottom spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row
                col_check = col - 1

                if col_check >= 0:  # checking left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                col_check = col + 1

                if col_check <= 7:  # checking right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col - 1

                if row_check >= 0 and col_check >= 0:  # checking top left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col - 1

                if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row - 1
                col_check = col + 1

                if row_check >= 0 and col_check <= 7:  # checking top right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

                row_check = row + 1
                col_check = col + 1

                if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                    check_value = board[row_check][col_check]
                    if check_value == 0:  # if space is empty
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)
                    elif 101 <= check_value <= 116:  # if space has enemy
                        temp = [x[:] for x in board]
                        temp[row_check][col_check] = temp[row][col]
                        temp[row][col] = 0
                        boards.append(temp)

        if outer_loop_must_break:
            break

    return boards


#def moves_white(board):
#    #  initialize all move lists
#    pawn_moves = []
#    rook_moves = []
#    knight_moves = []
#    bishop_moves = []
#    queen_moves = []
#    king_moves = []
#
#    # scan through board to get all available moves
#    for i in range(8):  # loop through rows
#        for j in range(8):  # loop through columns
#            p = board[i][j]
#
#            if 1 <= p <= 8:  # pawn
#                # print('pawn')
#                available = pawn_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            pawn_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 9 or p == 16:  # rook
#                # print('rook')
#                available = rook_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            rook_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 10 or p == 15:  # knight
#                # print('knight')
#                available = knight_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            knight_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 11 or p == 14:  # bishop
#                # print('bishop')
#                available = bishop_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            bishop_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 12:  # queen
#                # print('queen')
#                available = queen_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            queen_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#            elif p == 13:  # king
#                # print('king')
#                available = king_valid_moves_white(i, j, board)
#                for ii in range(8):  # loop through rows of available
#                    for jj in range(8):  # loop through columns of available
#                        if available[ii, jj] == 1:
#                            king_moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#    moves = [pawn_moves, rook_moves, knight_moves, bishop_moves, queen_moves, king_moves]
#    # print(moves)
#    return moves


def get_boards(moves, board):
    boards = []
    # print('boards before = ', boards)

    for p in range(6):  # loop through amount of pieces
        if moves[p] != []:  # check if there are available moves
            for [row, col], [r, c] in moves[p]:  # loop through all available moves for piece
                # print('piece = ', p, 'piece loc = ', [row, col], 'moving loc = ', [r, c], 'counter = ', counter)
                temp = [x[:] for x in board]
                temp[r][c] = temp[row][col]
                temp[row][col] = 0
                boards.append(temp)
                # print('boards intermediate = ', boards)

    # print('boards after = ', boards)
    return boards


def iterate_through_boards(available_boards_black, depth, white_num_pieces, black_num_pieces):

    available_boards_white = []
    final_boards_white = []
    depth -= 1
    final_board_av = 1

    for b in range(len(available_boards_black)):  # generate all counter moves/boards for white for the first depth
        current_boards_black = [available_boards_black[b]]
        available_boards_white.extend(boards_white(current_boards_black[0], white_num_pieces))

    for b in range(len(available_boards_white)):  # iterate to get white counter moves at depth d
        current_boards_white = [available_boards_white[b]]

        # print('current_boards_black = ', current_boards_black)
        for d in range(depth):
            # time1 = time.time()
            current_boards_black = []

            # if final_board_av == 0:
            #     initial_board_av = sum_board_value(current_boards_white, white_num_pieces, black_num_pieces)
            # else:
            #     initial_board_av = final_board_av

            for y in range(len(current_boards_white)):
                a = boards_black(current_boards_white[y], black_num_pieces)
                if sum_board_value(a, white_num_pieces, black_num_pieces) >= 0:
                    current_boards_black.extend(a)
                else:
                    print('bad board')

                #if value != 0:
                #    print(value)

            # print('depth = ', d+2, 'amount of black moves', len(current_boards_black))

            current_boards_white = []

            for x in range(len(current_boards_black)):
                current_boards_white.extend(boards_white(current_boards_black[x], white_num_pieces))
                #if value != 0:
                #    print(value)

            # print('depth = ', d+2, 'amount of white moves = ', len(current_boards_white))

            # final_board_av = sum_board_value(current_boards_white, white_num_pieces, black_num_pieces)

            # if final_board_av < initial_board_av:
            #     print('abandon branch')
            #     break

            if d == depth-1:
                final_boards_white.extend(current_boards_white)



            # time2 = time.time()
            # print('length of each move check = ', time2 - time1)
    # final_board_av = 0

    return final_boards_white


def board_value(board, white_num_pieces, black_num_pieces):
    total_pieces_to_check = white_num_pieces + black_num_pieces
    value = 0

    outer_loop_must_break = False
    for i in range(8):
        for j in range(8):
            n = board[i][j]
            if total_pieces_to_check == 0:
                outer_loop_must_break = True
                break
            elif 1 <= n <= 16 or 101 <= n <= 116:
                total_pieces_to_check -= 1
                if 1 <= n <= 8:
                    value -= 1
                elif n == 9 or n == 16:
                    value -= 5
                elif n == 10 or n == 15:
                    value -= 3
                elif n == 11 or n == 14:
                    value -= 3
                elif n == 12:
                    value -= 9
                elif n == 13:
                    value -= 200
                elif 109 <= n <= 116:
                    value += 1
                elif n == 101 or n == 108:
                    value += 5
                elif n == 102 or n == 107:
                    value += 3
                elif n == 103 or n == 106:
                    value += 3
                elif n == 104:
                    value += 9
                elif n == 105:
                    value += 200
        if outer_loop_must_break:
            break

    return value


def sum_board_value(current_boards_white, white_num_pieces, black_num_pieces):
    tot_value = 0
    num_boards = len(current_boards_white)

    for i in range(num_boards):
        tot_value += board_value(current_boards_white[i], white_num_pieces, black_num_pieces)

    average = tot_value/num_boards

    return average


class AIBlackLoops:
    def __init__(self):
        # initialize any constants or anything here
        print('AI initializing')
        self.depth = 2  # move search depth

    def move(self, chess):
        print('AI moving...')
        board = chess.board_unique.tolist()  # use list version of board
        # print('board = ', board)
        depth = self.depth
        black_num_pieces = chess.black_num_pieces
        white_num_pieces = chess.white_num_pieces

        # get all initial black moves and board states
        #white_board_value = board_value(board, white_num_pieces, black_num_pieces)
        available_boards_black = boards_black(board, black_num_pieces)
        final_boards_white = iterate_through_boards(available_boards_black, depth, white_num_pieces, black_num_pieces)
        # final_board_valuation = sum_board_value(final_boards_white, white_num_pieces, black_num_pieces)
        # print('overall board valuation for black = ', final_board_valuation)

        #print('current_boards_white end = ', current_boards_white)
        print('length of final white boards = ', len(final_boards_white))

        # deep_white_boards = iterate_through_boards(available_boards_black, depth, white_num_pieces, black_num_pieces)
        # print('length of final white boards = ', len(deep_white_boards))
        # print('AI turn done')


        # # initialize current moves (maybe dont need)
        # current_moves_black = []
        # current_boards_black = []
        # current_moves_white = []
        # current_boards_white = []
#
        # # print('available_moves_black = ', available_moves_black)
        # # print('available_boards_black = ', available_boards_black)
#
        # for b in range(len(available_boards_black)):
        #     current_boards_black = [available_boards_black[b]]
#
        #     # print('current_boards_black = ', current_boards_black)
        #     for d in range(depth):
        #         time1 = time.time()
        #         # print(len(current_boards_black))
        #         for x in range(len(current_boards_black)):
        #             # current_moves_white = moves_white(current_boards_black[x])
        #             current_boards_white.extend(boards_white(current_boards_black[x], white_num_pieces))
        #             # print('current_moves_white = ', current_moves_white)
        #             # print('current_boards_white = ', current_boards_white)
#
        #         current_boards_black = []  # reset old black boards
        #         # print(len(current_boards_white))
#
        #         for y in range(len(current_boards_white)):
        #             # current_moves_black = moves_black(current_boards_white[y])
        #             current_boards_black.extend(boards_black(current_boards_white[y], black_num_pieces))
        #             # print('current_moves_black = ', current_moves_black)
        #             # print('current_boards_black = ', current_boards_black)
        #             # print(current_boards_black[-1])
#
        #         current_boards_white = []  # reset old white boards
#
        #         time2 = time.time()
        #         print('length of each move check = ', time2 - time1)
#
        # print('AI turn done')

