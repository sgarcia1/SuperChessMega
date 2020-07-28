import numpy as np


class Chess:
    def __init__(self):
        self.board_unique = np.array([[101, 102, 103, 104, 105, 106, 107, 108],
                                      [109, 110, 111, 112, 113, 114, 115, 116],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [1, 2, 3, 4, 5, 6, 7, 8],
                                      [9, 10, 11, 12, 13, 14, 15, 16]])

        self.board_pawn_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [100, 100, 100, 100, 100, 100, 100, 100],
                                                 [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_pawn_values_black = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                 [100, 100, 100, 100, 100, 100, 100, 100],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_knight_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 320, 0, 0, 0, 0, 320, 0]])

        self.board_knight_values_black = np.array([[0, 320, 0, 0, 0, 0, 320, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_bishop_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 330, 0, 0, 330, 0, 0]])

        self.board_bishop_values_black = np.array([[0, 0, 330, 0, 0, 330, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_rook_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [500, 0, 0, 0, 0, 0, 0, 500]])

        self.board_rook_values_black = np.array([[500, 0, 0, 0, 0, 0, 0, 500],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_queen_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 900, 0, 0, 0, 0]])

        self.board_queen_values_black = np.array([[0, 0, 0, 900, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0]])

        self.board_king_values_white = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 20000, 0, 0, 0]])

        self.board_king_values_black = np.array([[0, 0, 0, 0, 20000, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0]])

        self.pawn_weights_white = (np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [10, 10, 20, 30, 30, 20, 10, 10],
            [5, 5, 10, 25, 25, 10, 5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [5, -5, -10, 0, 0, -10, -5, 5],
            [5, 10, 10, -20, -20, 10, 10, 5],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]) + 100) / 100

        self.pawn_weights_black = np.flip(self.pawn_weights_white, 0)

        self.knight_weights_white = (np.array([
            [-50, -40, -30, -30, -30, -30, -40, -50],
            [-40, -20, 0, 0, 0, 0, -20, -40],
            [-30, 0, 10, 15, 15, 10, 0, -30],
            [-30, 5, 15, 20, 20, 15, 5, -30],
            [-30, 0, 15, 20, 20, 15, 0, -30],
            [-30, 5, 10, 15, 15, 10, 5, -30],
            [-40, -20, 0, 5, 5, 0, -20, -40],
            [-50, -40, -30, -30, -30, -30, -40, -50]
        ]) + 320) / 320

        self.knight_weights_black = np.flip(self.knight_weights_white, 0)

        self.bishop_weights_white = (np.array([
            [-20, -10, -10, -10, -10, -10, -10, -20],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-10, 0, 5, 10, 10, 5, 0, -10],
            [-10, 5, 5, 10, 10, 5, 5, -10],
            [-10, 0, 10, 10, 10, 10, 0, -10],
            [-10, 10, 10, 10, 10, 10, 10, -10],
            [-10, 5, 0, 0, 0, 0, 5, -10],
            [-20, -10, -10, -10, -10, -10, -10, -20]
        ]) + 330) / 330

        self.bishop_weights_black = np.flip(self.bishop_weights_white, 0)

        self.rook_weights_white = (np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [5, 10, 10, 10, 10, 10, 10, 5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [0, 0, 0, 5, 5, 0, 0, 0]
        ]) + 500) / 500

        self.rook_weights_black = np.flip(self.rook_weights_white, 0)

        self.queen_weights_white = (np.array([
            [-20, -10, -10, -5, -5, -10, -10, -20],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-10, 0, 5, 5, 5, 5, 0, -10],
            [-5, 0, 5, 5, 5, 5, 0, -5],
            [0, 0, 5, 5, 5, 5, 0, -5],
            [-10, 5, 5, 5, 5, 5, 0, -10],
            [-10, 0, 5, 0, 0, 0, 0, -10],
            [-20, -10, -10, -5, -5, -10, -10, -20]
        ]) + 900) / 900

        self.queen_weights_black = np.flip(self.queen_weights_white, 0)

        self.king_weights_white = (np.array([
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-10, -20, -20, -20, -20, -20, -20, -10],
            [20, 20, 0, 0, 0, 0, 20, 20, ],
            [20, 30, 10, 0, 0, 10, 30, 20]
        ]) + 20000) / 20000

        self.king_weights_black = np.flip(self.king_weights_white, 0)

        self.white_pawns_moved = [False] * 8
        self.black_pawns_moved = [False] * 8
        self.white_num_pieces = 16
        self.black_num_pieces = 16
        self.white_move = True  # update this in main (and use in ai alpha beta)
        self.count = 0

        print(self.board_unique)

    def evaluate_board_with_weights(self):

        value = self.board_pawn_values_white * self.pawn_weights_white + \
                self.board_knight_values_white * self.knight_weights_white + \
                self.board_bishop_values_white * self.bishop_weights_white + \
                self.board_rook_values_white * self.rook_weights_white + \
                self.board_queen_values_white * self.queen_weights_white + \
                self.board_king_values_white * self.king_weights_white - \
                self.board_pawn_values_black * self.pawn_weights_black - \
                self.board_knight_values_black * self.knight_weights_black - \
                self.board_bishop_values_black * self.bishop_weights_black - \
                self.board_rook_values_black * self.rook_weights_black - \
                self.board_queen_values_black * self.queen_weights_black - \
                self.board_king_values_black * self.king_weights_black

        return value.sum()

    def evaluate_board_simple(self):
        board = self.board_unique
        white_num_pieces = self.white_num_pieces
        black_num_pieces = self.black_num_pieces
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
        return -value

    def update_board(self, move):
        row_from = move[0][0]
        col_from = move[0][1]
        row_to = move[1][0]
        col_to = move[1][1]

        # update unique board
        previous_piece = self.board_unique[row_to, col_to]
        self.board_unique[row_to, col_to] = self.board_unique[row_from, col_from]
        self.board_unique[row_from, col_from] = 0

        # update the values boards:
        pw = self.board_pawn_values_white[row_to, col_to]
        self.board_pawn_values_white[row_to, col_to] = self.board_pawn_values_white[row_from, col_from]
        self.board_pawn_values_white[row_from, col_from] = 0

        # update the values board
        pb = self.board_pawn_values_black[row_to, col_to]
        self.board_pawn_values_black[row_to, col_to] = self.board_pawn_values_black[row_from, col_from]
        self.board_pawn_values_black[row_from, col_from] = 0

        # update the values board
        nw = self.board_knight_values_white[row_to, col_to]
        self.board_knight_values_white[row_to, col_to] = self.board_knight_values_white[row_from, col_from]
        self.board_knight_values_white[row_from, col_from] = 0

        # update the values board
        nb = self.board_knight_values_black[row_to, col_to]
        self.board_knight_values_black[row_to, col_to] = self.board_knight_values_black[row_from, col_from]
        self.board_knight_values_black[row_from, col_from] = 0

        # update the values board
        bw = self.board_bishop_values_white[row_to, col_to]
        self.board_bishop_values_white[row_to, col_to] = self.board_bishop_values_white[row_from, col_from]
        self.board_bishop_values_white[row_from, col_from] = 0

        # update the values board
        bb = self.board_bishop_values_black[row_to, col_to]
        self.board_bishop_values_black[row_to, col_to] = self.board_bishop_values_black[row_from, col_from]
        self.board_bishop_values_black[row_from, col_from] = 0

        # update the values board
        rw = self.board_rook_values_white[row_to, col_to]
        self.board_rook_values_white[row_to, col_to] = self.board_rook_values_white[row_from, col_from]
        self.board_rook_values_white[row_from, col_from] = 0

        # update the values board
        rb = self.board_rook_values_black[row_to, col_to]
        self.board_rook_values_black[row_to, col_to] = self.board_rook_values_black[row_from, col_from]
        self.board_rook_values_black[row_from, col_from] = 0

        # update the values board
        qw = self.board_queen_values_white[row_to, col_to]
        self.board_queen_values_white[row_to, col_to] = self.board_queen_values_white[row_from, col_from]
        self.board_queen_values_white[row_from, col_from] = 0

        # update the values board
        qb = self.board_queen_values_black[row_to, col_to]
        self.board_queen_values_black[row_to, col_to] = self.board_queen_values_black[row_from, col_from]
        self.board_queen_values_black[row_from, col_from] = 0

        # update the values board
        kw = self.board_king_values_white[row_to, col_to]
        self.board_king_values_white[row_to, col_to] = self.board_king_values_white[row_from, col_from]
        self.board_king_values_white[row_from, col_from] = 0

        # update the values board
        kb = self.board_king_values_black[row_to, col_to]
        self.board_king_values_black[row_to, col_to] = self.board_king_values_black[row_from, col_from]
        self.board_king_values_black[row_from, col_from] = 0

        previous_values = [pw, pb, nw, nb, bw, bb, rw, rb, qw, qb, kw, kb]

        if 1 <= previous_piece <= 16:
            self.white_num_pieces -= 1
        elif 101 <= previous_piece <= 116:
            self.black_num_pieces -= 1

        return previous_piece, previous_values

    def undo_move(self, move, previous_piece, previous_values):
        row_from = move[0][0]
        col_from = move[0][1]
        row_to = move[1][0]
        col_to = move[1][1]

        if 1 <= previous_piece <= 16:
            self.white_num_pieces += 1
        elif 101 <= previous_piece <= 116:
            self.black_num_pieces += 1

        # update unique board
        self.board_unique[row_from, col_from] = self.board_unique[row_to, col_to]
        self.board_unique[row_to, col_to] = previous_piece

        # undo the values boards:
        self.board_pawn_values_white[row_from, col_from] = self.board_pawn_values_white[row_to, col_to]
        self.board_pawn_values_white[row_to, col_to] = previous_values[0]

        # update the values board
        self.board_pawn_values_black[row_from, col_from] = self.board_pawn_values_black[row_to, col_to]
        self.board_pawn_values_black[row_to, col_to] = previous_values[1]

        # update the values board
        self.board_knight_values_white[row_from, col_from] = self.board_knight_values_white[row_to, col_to]
        self.board_knight_values_white[row_to, col_to] = previous_values[2]

        # update the values board
        self.board_knight_values_black[row_from, col_from] = self.board_knight_values_black[row_to, col_to]
        self.board_knight_values_black[row_to, col_to] = previous_values[3]

        # update the values board
        self.board_bishop_values_white[row_from, col_from] = self.board_bishop_values_white[row_to, col_to]
        self.board_bishop_values_white[row_to, col_to] = previous_values[4]

        # update the values board
        self.board_bishop_values_black[row_from, col_from] = self.board_bishop_values_black[row_to, col_to]
        self.board_bishop_values_black[row_to, col_to] = previous_values[5]

        # update the values board
        self.board_rook_values_white[row_from, col_from] = self.board_rook_values_white[row_to, col_to]
        self.board_rook_values_white[row_to, col_to] = previous_values[6]

        # update the values board
        self.board_rook_values_black[row_from, col_from] = self.board_rook_values_black[row_to, col_to]
        self.board_rook_values_black[row_to, col_to] = previous_values[7]

        # update the values board
        self.board_queen_values_white[row_from, col_from] = self.board_queen_values_white[row_to, col_to]
        self.board_queen_values_white[row_to, col_to] = previous_values[8]

        # update the values board
        self.board_queen_values_black[row_from, col_from] = self.board_queen_values_black[row_to, col_to]
        self.board_queen_values_black[row_to, col_to] = previous_values[9]

        # update the values board
        self.board_king_values_white[row_from, col_from] = self.board_king_values_white[row_to, col_to]
        self.board_king_values_white[row_to, col_to] = previous_values[10]

        # update the values board
        self.board_king_values_black[row_from, col_from] = self.board_king_values_black[row_to, col_to]
        self.board_king_values_black[row_to, col_to] = previous_values[11]

#    def get_moves_white(self):
#        #  initialize all move lists
#        moves = []
#
#        # scan through board to get all available moves
#        for i in range(8):  # loop through rows
#            for j in range(8):  # loop through columns
#                p = self.board_unique[i, j]
#
#                if 1 <= p <= 8:  # pawn
#                    # print('pawn')
#                    available = self.pawn_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 9 or p == 16:  # rook
#                    # print('rook')
#                    available = self.rook_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 10 or p == 15:  # knight
#                    # print('knight')
#                    available = self.knight_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 11 or p == 14:  # bishop
#                    # print('bishop')
#                    available = self.bishop_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 12:  # queen
#                    # print('queen')
#                    available = self.queen_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 13:  # king
#                    # print('king')
#                    available = self.king_valid_moves_white(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#        # print(moves)
#        return moves

    def get_moves_black(self):
        moves = []
        board = self.board_unique

        # counter = 0
        pieces_checked = 0
        outer_loop_must_break = False

        # scan through board to get all available moves
        for row in range(8):  # loop through rows
            for col in range(8):  # loop through columns
                if pieces_checked >= self.black_num_pieces:
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
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 2
                    col_check = col

                    if row_check <= 7 and row == 1:  # checking two up spot and if have moved yet
                        check_value1 = board[row_check][col_check]
                        check_value2 = board[row_check - 1][col_check]
                        if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col - 1

                    if row_check <= 7 and col_check >= 0:  # checking left attack spot
                        check_value = board[row_check][col_check]
                        if 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        # add en passont

                    row_check = row + 1
                    col_check = col + 1

                    if row_check <= 7 and col_check <= 7:  # checking right attack spot
                        check_value = board[row_check][col_check]
                        if 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while row_check < 7:  # run for all spaces below rook
                        row_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check > 0:  # run for all spaces left of rook
                        col_check -= 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check < 7:  # run for all spaces right of rook
                        col_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 2
                    col_check = col + 1

                    if row_check >= 0 and col_check <= 7:  # checking top right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 2
                    col_check = col - 1

                    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 2
                    col_check = col + 1

                    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col - 2

                    if row_check >= 0 and col_check >= 0:  # checking left upper spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col - 2

                    if row_check <= 7 and col_check >= 0:  # checking left lower spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col + 2

                    if row_check >= 0 and col_check <= 7:  # checking right upper spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col + 2

                    if row_check <= 7 and col_check <= 7:  # checking right lower spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while row_check < 7:  # run for all spaces below
                        row_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check > 0:  # run for all spaces to the left
                        col_check -= 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check < 7:  # run for all spaces to the right
                        col_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1

                    if row_check <= 7:  # checking bottom spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row
                    col_check = col - 1

                    if col_check >= 0:  # checking left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    col_check = col + 1

                    if col_check <= 7:  # checking right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col - 1

                    if row_check >= 0 and col_check >= 0:  # checking top left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col - 1

                    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col + 1

                    if row_check >= 0 and col_check <= 7:  # checking top right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col + 1

                    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 1 <= check_value <= 16:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

            if outer_loop_must_break:
                break

            # time2 = time.time()
            # print('loop time = ', time2)

        # end = time.time()

        # print('counter = ', counter)
        # print('pieces_checked = ', pieces_checked)

        # print('TOTAL TIME = ', end - start)
        # print(len(boards))
        return moves

    def get_moves_white(self):
        moves = []
        board = self.board_unique

        # counter = 0
        pieces_checked = 0
        outer_loop_must_break = False

        # scan through board to get all available moves
        for row in range(8):  # loop through rows
            for col in range(8):  # loop through columns
                if pieces_checked >= self.white_num_pieces:
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
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 2
                    col_check = col

                    if row_check >= 0 and row == 6:  # checking two up spot and that pawn has not moved yet
                        check_value1 = board[row_check][col_check]
                        check_value2 = board[row_check + 1][col_check]
                        if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col - 1

                    if row_check >= 0 and col_check >= 0:  # checking left attack spot
                        check_value = board[row_check][col_check]
                        if 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        # add en passont

                    row_check = row - 1
                    col_check = col + 1

                    if row_check >= 0 and col_check <= 7:  # checking right attack spot
                        check_value = board[row_check][col_check]
                        if 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while row_check < 7:  # run for all spaces below rook
                        row_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check > 0:  # run for all spaces left of rook
                        col_check -= 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check < 7:  # run for all spaces right of rook
                        col_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 2
                    col_check = col + 1

                    if row_check >= 0 and col_check <= 7:  # checking top right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 2
                    col_check = col - 1

                    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 2
                    col_check = col + 1

                    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col - 2

                    if row_check >= 0 and col_check >= 0:  # checking left upper spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col - 2

                    if row_check <= 7 and col_check >= 0:  # checking left lower spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col + 2

                    if row_check >= 0 and col_check <= 7:  # checking right upper spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col + 2

                    if row_check <= 7 and col_check <= 7:  # checking right lower spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while row_check < 7:  # run for all spaces below
                        row_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check > 0:  # run for all spaces to the left
                        col_check -= 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
                            break
                        else:  # if your own piece is in the space
                            break

                    row_check = row
                    col_check = col

                    while col_check < 7:  # run for all spaces to the right
                        col_check += 1
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move
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
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1

                    if row_check <= 7:  # checking bottom spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row
                    col_check = col - 1

                    if col_check >= 0:  # checking left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    col_check = col + 1

                    if col_check <= 7:  # checking right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col - 1

                    if row_check >= 0 and col_check >= 0:  # checking top left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col - 1

                    if row_check <= 7 and col_check >= 0:  # checking bottom left spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row - 1
                    col_check = col + 1

                    if row_check >= 0 and col_check <= 7:  # checking top right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

                    row_check = row + 1
                    col_check = col + 1

                    if row_check <= 7 and col_check <= 7:  # checking bottom right spot
                        check_value = board[row_check][col_check]
                        if check_value == 0:  # if space is empty
                            moves.append([[row, col], [row_check, col_check]])  # add move
                        elif 101 <= check_value <= 116:  # if space has enemy
                            moves.append([[row, col], [row_check, col_check]])  # add move

            if outer_loop_must_break:
                break

        return moves

#    def get_moves_black(self):
#        #  initialize all move lists
#        moves = []
#
#        # scan through board to get all available moves
#        for i in range(8):  # loop through rows
#            for j in range(8):  # loop through columns
#                p = self.board_unique[i, j]
#
#                if 109 <= p <= 116:  # pawn
#                    # print('pawn')
#                    available = self.pawn_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 101 or p == 108:  # rook
#                    # print('rook')
#                    available = self.rook_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 102 or p == 107:  # knight
#                    # print('knight')
#                    available = self.knight_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 103 or p == 106:  # bishop
#                    # print('bishop')
#                    available = self.bishop_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 104:  # queen
#                    # print('queen')
#                    available = self.queen_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#                elif p == 105:  # king
#                    # print('king')
#                    available = self.king_valid_moves_black(i, j)
#                    for ii in range(8):  # loop through rows of available
#                        for jj in range(8):  # loop through columns of available
#                            if available[ii, jj] == 1:
#                                moves.append([[i, j], [ii, jj]])  # add move from [i,j] to [ii,jj]
#
#        # print(moves)
#        return moves

    def check_valid_move_white(self, row, col, r, c):
        board = self.board_unique
        p = board[row, col]

        #  simple checks
        if row == r and col == c:  # check if not moved
            return False

        elif 1 <= board[r, c] <= 16:  # check if moving into white piece
            return False

        # elif move_puts_in_check(row, col, r, c):  # check if move puts you in check

        else:  # check valid moves for the specific type of piece

            if 1 <= p <= 8:  # pawn
                # print('pawn')
                available = self.pawn_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 9 or p == 16:  # rook
                # print('rook')
                if r != row and c != col:  # must move in a line
                    return False
                else:  # check if moving spot is in set of all allowed piece moves
                    available = self.rook_valid_moves_white(row, col)
                    if available[r, c] == 1:
                        return True
                    else:
                        return False

            elif p == 10 or p == 15:  # knight
                # print('knight')
                available = self.knight_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 11 or p == 14:  # bishop
                # print('bishop')
                if r == row or c == col:  # cant move in a straight line
                    return False
                else:  # check if moving spot is in set of all allowed piece moves
                    available = self.bishop_valid_moves_white(row, col)
                    if available[r, c] == 1:
                        return True
                    else:
                        return False

            elif p == 12:  # queen
                # print('queen')
                available = self.queen_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 13:  # king
                # print('king')
                available = self.king_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

    def rook_valid_moves_white(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0:  # run for all spaces above rook
            row_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def bishop_valid_moves_white(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
            row_check -= 1
            col_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def queen_valid_moves_white(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0:  # run for all spaces above
            row_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def knight_valid_moves_white(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        row_check -= 2
        col_check -= 1

        if row_check >= 0 and col_check >= 0:  # checking top left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 2
        col_check = col + 1

        if row_check >= 0 and col_check <= 7:  # checking top right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 2
        col_check = col - 1

        if row_check <= 7 and col_check >= 0:  # checking bottom left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 2
        col_check = col + 1

        if row_check <= 7 and col_check <= 7:  # checking bottom right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col - 2

        if row_check >= 0 and col_check >= 0:  # checking left upper spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col - 2

        if row_check <= 7 and col_check >= 0:  # checking left lower spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col + 2

        if row_check >= 0 and col_check <= 7:  # checking right upper spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col + 2

        if row_check <= 7 and col_check <= 7:  # checking right lower spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        # print(available)
        return available

    def pawn_valid_moves_white(self, row, col):
        board = self.board_unique
        available = np.zeros((8, 8))

        row_check = row - 1
        col_check = col

        if row_check >= 0:  # checking one up spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1

        row_check = row - 2
        col_check = col

        if row_check >= 0:  # checking two up spot
            check_value1 = board[row_check, col_check]
            check_value2 = board[row_check + 1, col_check]
            unique_pawn = board[row, col]
            if not self.white_pawns_moved[unique_pawn - 1]:  # check if pawn has moved yet (CHANGE TO == 6)
                if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                    available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col - 1

        if row_check >= 0 and col_check >= 0:  # checking left attack spot
            check_value = board[row_check, col_check]
            if 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1
            # add en passont

        row_check = row - 1
        col_check = col + 1

        if row_check >= 0 and col_check <= 7:  # checking right attack spot
            check_value = board[row_check, col_check]
            if 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1
            # add en passont

        return available

    def king_valid_moves_white(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        row_check -= 1

        if row_check >= 0:  # checking top spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1

        if row_check <= 7:  # checking bottom spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row
        col_check = col - 1

        if col_check >= 0:  # checking left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        col_check = col + 1

        if col_check <= 7:  # checking right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col - 1

        if row_check >= 0 and col_check >= 0:  # checking top left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col - 1

        if row_check <= 7 and col_check >= 0:  # checking bottom left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col + 1

        if row_check >= 0 and col_check <= 7:  # checking top right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col + 1

        if row_check <= 7 and col_check <= 7:  # checking bottom right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 101 <= check_value <= 116:  # if space has enemy
                available[row_check, col_check] = 1

        # print(available)
        return available

    def check_valid_move_black(self, row, col, r, c):
        board = self.board_unique
        p = board[row, col]

        #  simple checks
        if row == r and col == c:  # check if not moved
            return False

        elif 101 <= board[r, c] <= 116:  # check if moving into black piece
            return False

        # elif move_puts_in_check(row, col, r, c):  # check if move puts you in check

        else:  # check valid moves for the specific type of piece

            if 109 <= p <= 116:  # pawn
                # print('pawn')
                available = self.pawn_valid_moves_black(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 101 or p == 108:  # rook
                # print('rook')
                if r != row and c != col:  # must move in a line
                    return False
                else:  # check if moving spot is in set of all allowed piece moves
                    available = self.rook_valid_moves_white(row, col)
                    if available[r, c] == 1:
                        return True
                    else:
                        return False

            elif p == 102 or p == 107:  # knight
                # print('knight')
                available = self.knight_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 103 or p == 106:  # bishop
                # print('bishop')
                if r == row or c == col:  # cant move in a straight line
                    return False
                else:  # check if moving spot is in set of all allowed piece moves
                    available = self.bishop_valid_moves_white(row, col)
                    if available[r, c] == 1:
                        return True
                    else:
                        return False

            elif p == 104:  # queen
                # print('queen')
                available = self.queen_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

            elif p == 105:  # king
                # print('king')
                available = self.king_valid_moves_white(row, col)
                if available[r, c] == 1:
                    return True
                else:
                    return False

    def rook_valid_moves_black(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0:  # run for all spaces above rook
            row_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def bishop_valid_moves_black(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0 and col_check > 0:  # run for all spaces in the top left direction
            row_check -= 1
            col_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def queen_valid_moves_black(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        while row_check > 0:  # run for all spaces above
            row_check -= 1
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
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
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1
                break
            else:  # if your own piece is in the space
                break

        return available

    def knight_valid_moves_black(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        row_check -= 2
        col_check -= 1

        if row_check >= 0 and col_check >= 0:  # checking top left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 2
        col_check = col + 1

        if row_check >= 0 and col_check <= 7:  # checking top right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 2
        col_check = col - 1

        if row_check <= 7 and col_check >= 0:  # checking bottom left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 2
        col_check = col + 1

        if row_check <= 7 and col_check <= 7:  # checking bottom right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col - 2

        if row_check >= 0 and col_check >= 0:  # checking left upper spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col - 2

        if row_check <= 7 and col_check >= 0:  # checking left lower spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col + 2

        if row_check >= 0 and col_check <= 7:  # checking right upper spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col + 2

        if row_check <= 7 and col_check <= 7:  # checking right lower spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        # print(available)
        return available

    def pawn_valid_moves_black(self, row, col):
        board = self.board_unique
        available = np.zeros((8, 8))

        row_check = row + 1
        col_check = col

        if row_check <= 7:  # checking one up spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1

        row_check = row + 2
        col_check = col

        if row_check <= 7:  # checking two up spot
            check_value1 = board[row_check, col_check]
            check_value2 = board[row_check - 1, col_check]
            unique_pawn = board[row, col]
            if not self.white_pawns_moved[unique_pawn - 109]:  # check if pawn has moved yet
                if check_value1 == 0 and check_value2 == 0:  # if spaces above are empty
                    available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col - 1

        if row_check <= 7 and col_check >= 0:  # checking left attack spot
            check_value = board[row_check, col_check]
            if 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1
            # add en passont

        row_check = row + 1
        col_check = col + 1

        if row_check <= 7 and col_check <= 7:  # checking right attack spot
            check_value = board[row_check, col_check]
            if 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1
            # add en passont

        return available

    def king_valid_moves_black(self, row, col):
        board = self.board_unique
        row_check = row
        col_check = col
        available = np.zeros((8, 8))

        row_check -= 1

        if row_check >= 0:  # checking top spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1

        if row_check <= 7:  # checking bottom spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row
        col_check = col - 1

        if col_check >= 0:  # checking left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        col_check = col + 1

        if col_check <= 7:  # checking right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col - 1

        if row_check >= 0 and col_check >= 0:  # checking top left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col - 1

        if row_check <= 7 and col_check >= 0:  # checking bottom left spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row - 1
        col_check = col + 1

        if row_check >= 0 and col_check <= 7:  # checking top right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        row_check = row + 1
        col_check = col + 1

        if row_check <= 7 and col_check <= 7:  # checking bottom right spot
            check_value = board[row_check, col_check]
            if check_value == 0:  # if space is empty
                available[row_check, col_check] = 1
            elif 1 <= check_value <= 16:  # if space has enemy
                available[row_check, col_check] = 1

        # print(available)
        return available
