import numpy as np

class Board(object):


    EMPTY, BLACK, WHITE = '.', 'B', 'W'
    board = np.empty((8, 8), dtype=str)

    def __init__(self):
         # import pdb; pdb.set_trace()
        for i in range(0, 8):
            for j in range(0, 8):
                self.board[i][j] = Board.EMPTY

        self.board[3][3], self.board[4][4] = Board.WHITE, Board.WHITE
        self.board[3][4], self.board[4][3] = Board.BLACK, Board.BLACK


    def show(self):
        return print(self.board)

