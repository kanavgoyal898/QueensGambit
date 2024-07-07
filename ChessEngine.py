import chess as ch

class Engine:

    def __init__(self, board, max_depth, color):
        self.board = board
        self.max_depth = max_depth
        self.color = color

    