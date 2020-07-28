import numpy as np


class AIMinimaxAlphaBeta:

    depth = 2  # move search depth
    infinite = 1000000

    def move(self, chess):
        print('AI moving...')
        depth = AIMinimaxAlphaBeta.depth
        alpha = -AIMinimaxAlphaBeta.infinite
        beta = AIMinimaxAlphaBeta.infinite

        if chess.white_move:
            best_score, best_move = AIMinimaxAlphaBeta.max_alpha_beta(chess, depth, alpha, beta)
        else:
            best_score, best_move = AIMinimaxAlphaBeta.min_alpha_beta(chess, depth, alpha, beta)

        print('best move = ', best_move)
        print('best score = ', best_score/100)
        # print('count = ', chess.count)

        return best_move

    @staticmethod
    def min_alpha_beta(chess, depth, alpha, beta):
        # print('minimizing')
        # chess.count += 1
        # print(chess.count)
        if depth == 0:  # if at the end of the tree (leaves), evaluate the position and send up
            return chess.evaluate_board_with_weights(), 0

        best_score = AIMinimaxAlphaBeta.infinite
        best_move = []

        for moves in chess.get_moves_black():
            previous_piece, previous_values = chess.update_board(moves)  # updating board for current move
            # print('board before, with move = ', moves, 'prev_piece = ', previous_piece, alpha, beta, depth, best_score)
            # print(chess.board_unique)
            value, move = AIMinimaxAlphaBeta.max_alpha_beta(chess, depth - 1, alpha, beta)
            # print(value)
            if value < best_score:
                best_score = value
                best_move = moves

            chess.undo_move(moves, previous_piece, previous_values)  # undo move that is being explored to previous state
            # print('board after, with move = ', moves, 'prev_piece = ', previous_piece, alpha, beta, depth)
            # print(chess.board_unique)
            beta = min(beta, best_score)

            if alpha >= beta:
                # print('pruning')
                return best_score, best_move

        return best_score, best_move

    @staticmethod  # check against class method and normal method for speed
    def max_alpha_beta(chess, depth, alpha, beta):
        # print('maximizing')
        # chess.count += 1
        # print(chess.count)
        if depth == 0:  # if at the end of the tree (leaves), evaluate the position and send up
            return chess.evaluate_board_with_weights(), 0

        best_score = -AIMinimaxAlphaBeta.infinite
        best_move = []

        for moves in chess.get_moves_white():
            previous_piece, previous_values = chess.update_board(moves)  # updating board for current move
            # print('board before, with move = ', moves, 'prev_piece = ', previous_piece, alpha, beta, depth)
            # print(chess.board_unique)
            value, move = AIMinimaxAlphaBeta.min_alpha_beta(chess, depth - 1, alpha, beta)
            # print(value)
            if value > best_score:
                best_score = value
                best_move = moves

            chess.undo_move(moves, previous_piece, previous_values)  # undo move that is being explored to previous state
            # print('board after, with move = ', moves, 'prev_piece = ', previous_piece, alpha, beta, depth)
            # print(chess.board_unique)
            alpha = max(alpha, best_score)

            if alpha >= beta:
                # print('pruning')
                return best_score, best_move

        return best_score, best_move
