import piece as piece


class Board():
    """
    A class to represent a chess board.

    ...

    Attributes:
    -----------
    board : list[list[Piece]]
        represents a chess board

    turn : bool
        True if white's turn

    white_ghost_piece : tup
        The coordinates of a white ghost piece representing a takeable pawn for en passant

    black_ghost_piece : tup
        The coordinates of a black ghost piece representing a takeable pawn for en passant

    Methods:
    --------
    print_board() -> None
        Prints the current configuration of the board

    move(start:tup, to:tup) -> None
        Moves the piece at `start` to `to` if possible. Otherwise, does nothing.

    """

    def __init__(self):
        """
        Initializes the board per standard chess rules
        """

        self.board = []

        # Board set-up
        for i in range(8):
            self.board.append([None] * 8)

        # Pre set position for white:
        self.board[1][5] = piece.King(True)
        self.board[0][2] = piece.Rook(True)
        self.board[3][4] = piece.Bishop(True)
        self.board[4][6] = piece.Pawn(True)
        self.board[5][5] = piece.Pawn(True)
        self.board[6][5] = piece.Pawn(True)

        # Pre set posistion for black:
        self.board[3][3] = piece.King(False)

    def print_board(self):
        """
        Prints the current state of the board.
        """

        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j == None or j.name == 'GP':
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
