from tkinter import *
from Chess import Chess
from AIBlackLoops import AIBlackLoops
from AIMinimaxAlphaBeta import AIMinimaxAlphaBeta
import cProfile


# create global variables
chess = Chess()
# AI = AIBlackLoops()
AI = AIMinimaxAlphaBeta()
row = 1  # row of where you last clicked
col = 1  # col of where you last clicked


def click(event):
    x, y = event.x, event.y
    global row
    global col
    r, c = x_y_to_row_col(x, y)
    row = r
    col = c
    draw_piece_white(x, y, chess.board_unique[row, col])


def holding(event):
    x, y = event.x, event.y
    draw_piece_white(x, y, chess.board_unique[row, col])


def release(event):
    global chess
    global AI
    global row
    global col
    n = chess.board_unique[row, col]
    if 1 <= n <= 16:
        x, y = event.x, event.y
        r, c = x_y_to_row_col(x, y)

        # check if valid move
        #print(chess.white_pawns_moved)
        valid = chess.check_valid_move_white(row, col, r, c)
        #print(chess.white_pawns_moved)

        #valid = True

        if not valid:
            x = col*79+40
            y = row*79+40
            draw_piece_white(x, y, chess.board_unique[row, col])
        else:
            x = c * 79 + 40
            y = r * 79 + 40
            unique_piece = chess.board_unique[row, col]

            # move piece
            n, previous_values = chess.update_board([[row, col], [r, c]])
            draw_piece_white(x, y, unique_piece)
            delete_piece_black(chess, n)
            # print(chess.board_unique)

            if 1 <= unique_piece <= 8:  # pawn was moved
                if not chess.white_pawns_moved[unique_piece - 1]:  # pawn has moved for the first time CHANGE TO STARTING ROW
                    chess.white_pawns_moved[unique_piece-1] = True # can just see if on original row # DELETE

                elif r == 0:  # pawn has reached end, assume it turns to queen
                    print('turn pawn into queen')
                    # update pawn to queen, add new unique numbers to queen checks

            # check state (checkmate, check, stalemate) # can run ai for checkmate/stalemate?, rerun it for if in check

            # opponent move
            chess.white_move = False
            # cProfile.run('AI.move(chess)')
            AI_move = AI.move(chess)
            row = AI_move[0][0]
            col = AI_move[0][1]
            r = AI_move[1][0]
            c = AI_move[1][1]
            unique_piece = chess.board_unique[row, col]
            n, previous_values = chess.update_board(AI_move)
            x = c * 79 + 40
            y = r * 79 + 40
            draw_piece_black(x, y, unique_piece)
            delete_piece_white(chess, n)
            # print(chess.board_unique)
            print('board valuation simple = ', chess.evaluate_board_simple())
            print('board valuation with weights = ', chess.evaluate_board_with_weights()/100)
            chess.white_move = True


def draw_piece_white(x, y, n):
    if n < 1 or n > 16:
        print('invalid move')
    elif n == 1:
        window.coords(WhitePawn1, x, y)
    elif n == 2:
        window.coords(WhitePawn2, x, y)
    elif n == 3:
        window.coords(WhitePawn3, x, y)
    elif n == 4:
        window.coords(WhitePawn4, x, y)
    elif n == 5:
        window.coords(WhitePawn5, x, y)
    elif n == 6:
        window.coords(WhitePawn6, x, y)
    elif n == 7:
        window.coords(WhitePawn7, x, y)
    elif n == 8:
        window.coords(WhitePawn8, x, y)
    elif n == 9:
        window.coords(WhiteRook1, x, y)
    elif n == 10:
        window.coords(WhiteKnight1, x, y)
    elif n == 11:
        window.coords(WhiteBishop1, x, y)
    elif n == 12:
        window.coords(WhiteQueen, x, y)
    elif n == 13:
        window.coords(WhiteKing, x, y)
    elif n == 14:
        window.coords(WhiteBishop2, x, y)
    elif n == 15:
        window.coords(WhiteKnight2, x, y)
    elif n == 16:
        window.coords(WhiteRook2, x, y)


def draw_piece_black(x, y, n):
    if n < 101 or n > 116:
        print('invalid move')
    elif n == 109:
        window.coords(BlackPawn1, x, y)
    elif n == 110:
        window.coords(BlackPawn2, x, y)
    elif n == 111:
        window.coords(BlackPawn3, x, y)
    elif n == 112:
        window.coords(BlackPawn4, x, y)
    elif n == 113:
        window.coords(BlackPawn5, x, y)
    elif n == 114:
        window.coords(BlackPawn6, x, y)
    elif n == 115:
        window.coords(BlackPawn7, x, y)
    elif n == 116:
        window.coords(BlackPawn8, x, y)
    elif n == 101:
        window.coords(BlackRook1, x, y)
    elif n == 102:
        window.coords(BlackKnight1, x, y)
    elif n == 103:
        window.coords(BlackBishop1, x, y)
    elif n == 104:
        window.coords(BlackQueen, x, y)
    elif n == 105:
        window.coords(BlackKing, x, y)
    elif n == 106:
        window.coords(BlackBishop2, x, y)
    elif n == 107:
        window.coords(BlackKnight2, x, y)
    elif n == 108:
        window.coords(BlackRook2, x, y)


def delete_piece_white(chess, n):
    if 1 <= n <= 16:
        if n == 1:
            window.delete(WhitePawn1)
        elif n == 2:
            window.delete(WhitePawn2)
        elif n == 3:
            window.delete(WhitePawn3)
        elif n == 4:
            window.delete(WhitePawn4)
        elif n == 5:
            window.delete(WhitePawn5)
        elif n == 6:
            window.delete(WhitePawn6)
        elif n == 7:
            window.delete(WhitePawn7)
        elif n == 8:
            window.delete(WhitePawn8)
        elif n == 9:
            window.delete(WhiteRook1)
        elif n == 10:
            window.delete(WhiteKnight1)
        elif n == 11:
            window.delete(WhiteBishop1)
        elif n == 12:
            window.delete(WhiteQueen)
        elif n == 13:
            window.delete(WhiteKing)
        elif n == 14:
            window.delete(WhiteBishop2)
        elif n == 15:
            window.delete(WhiteKnight2)
        elif n == 16:
            window.delete(WhiteRook2)


def delete_piece_black(chess, n):
    if 101 <= n <= 116:
        if n == 109:
            window.delete(BlackPawn1)
        elif n == 110:
            window.delete(BlackPawn2)
        elif n == 111:
            window.delete(BlackPawn3)
        elif n == 112:
            window.delete(BlackPawn4)
        elif n == 113:
            window.delete(BlackPawn5)
        elif n == 114:
            window.delete(BlackPawn6)
        elif n == 115:
            window.delete(BlackPawn7)
        elif n == 116:
            window.delete(BlackPawn8)
        elif n == 101:
            window.delete(BlackRook1)
        elif n == 102:
            window.delete(BlackKnight1)
        elif n == 103:
            window.delete(BlackBishop1)
        elif n == 104:
            window.delete(BlackQueen)
        elif n == 105:
            window.delete(BlackKing)
        elif n == 106:
            window.delete(BlackBishop2)
        elif n == 107:
            window.delete(BlackKnight2)
        elif n == 108:
            window.delete(BlackRook2)


def x_y_to_row_col(x, y):
    r = round((y - 40) / 79)
    c = round((x - 40) / 79)
    if r <= 0:
        r = 0
    elif r >= 7:
        r = 7
    if c <= 0:
        c = 0
    elif c >= 7:
        c = 7
    return r, c


# setup the main GUI object, and assign user mouse inputs to trigger functions
root = Tk()
root.bind('<Button-1>', click)
root.bind('<B1-Motion>', holding)
root.bind('<ButtonRelease-1>', release)

# create main window to add GUI stuff to
window = Canvas(root, width=632, height=632)
window.pack()

# import images
EmptyBoardImg = PhotoImage(file="EmptyBoard.gif")
BlackBishopImg = PhotoImage(file="BlackBishop.gif")
BlackKingImg = PhotoImage(file="BlackKing.gif")
BlackKnightImg = PhotoImage(file="BlackKnight.gif")
BlackPawnImg = PhotoImage(file="BlackPawn.gif")
BlackQueenImg = PhotoImage(file="BlackQueen.gif")
BlackRookImg = PhotoImage(file="BlackRook.gif")
WhiteBishopImg = PhotoImage(file="WhiteBishop.gif")
WhiteKingImg = PhotoImage(file="WhiteKing.gif")
WhiteKnightImg = PhotoImage(file="WhiteKnight.gif")
WhitePawnImg = PhotoImage(file="WhitePawn.gif")
WhiteQueenImg = PhotoImage(file="WhiteQueen.gif")
WhiteRookImg = PhotoImage(file="WhiteRook.gif")

# draw background board
EmptyBoard = window.create_image(318, 318, image=EmptyBoardImg)

# draw black pieces in the starting positions
BlackPawn1 = window.create_image(40, 119, image=BlackPawnImg)
BlackPawn2 = window.create_image(119, 119, image=BlackPawnImg)
BlackPawn3 = window.create_image(198, 119, image=BlackPawnImg)
BlackPawn4 = window.create_image(277, 119, image=BlackPawnImg)
BlackPawn5 = window.create_image(356, 119, image=BlackPawnImg)
BlackPawn6 = window.create_image(435, 119, image=BlackPawnImg)
BlackPawn7 = window.create_image(514, 119, image=BlackPawnImg)
BlackPawn8 = window.create_image(593, 119, image=BlackPawnImg)
BlackBishop1 = window.create_image(198, 40, image=BlackBishopImg)
BlackBishop2 = window.create_image(435, 40, image=BlackBishopImg)
BlackRook1 = window.create_image(40, 40, image=BlackRookImg)
BlackRook2 = window.create_image(593, 40, image=BlackRookImg)
BlackQueen = window.create_image(277, 40, image=BlackQueenImg)
BlackKing = window.create_image(356, 40, image=BlackKingImg)
BlackKnight1 = window.create_image(119, 40, image=BlackKnightImg)
BlackKnight2 = window.create_image(514, 40, image=BlackKnightImg)

# draw white pieces in the starting positions
WhitePawn1 = window.create_image(40, 514, image=WhitePawnImg)
WhitePawn2 = window.create_image(119, 514, image=WhitePawnImg)
WhitePawn3 = window.create_image(198, 514, image=WhitePawnImg)
WhitePawn4 = window.create_image(277, 514, image=WhitePawnImg)
WhitePawn5 = window.create_image(356, 514, image=WhitePawnImg)
WhitePawn6 = window.create_image(435, 514, image=WhitePawnImg)
WhitePawn7 = window.create_image(514, 514, image=WhitePawnImg)
WhitePawn8 = window.create_image(593, 514, image=WhitePawnImg)
WhiteBishop1 = window.create_image(198, 593, image=WhiteBishopImg)
WhiteBishop2 = window.create_image(435, 593, image=WhiteBishopImg)
WhiteRook1 = window.create_image(40, 593, image=WhiteRookImg)
WhiteRook2 = window.create_image(593, 593, image=WhiteRookImg)
WhiteQueen = window.create_image(277, 593, image=WhiteQueenImg)
WhiteKing = window.create_image(356, 593, image=WhiteKingImg)
WhiteKnight1 = window.create_image(119, 593, image=WhiteKnightImg)
WhiteKnight2 = window.create_image(514, 593, image=WhiteKnightImg)

# start the main loop for GUI's and user input to start working
mainloop()


