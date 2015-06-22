class Piece(object):
    """
    Generalized piece class that contains attributes about whether it is an empty piece or if it is black or white.
    All pieces except empty have their own subclass. Contains a list of locations the piece can move to
    """
    def __init__(self):
        self.empty = True
        self.color = "NA"

    def __repr__(self):
        if self.empty:
            return u"\u25A1"
    def move_set(self, piece, board):
        print "Error: This is an empty space"

    def piece_at(self, at, color = None):
        """
        If only at argument is filled, the function checks to see if there is a chess piece at the given
        coordinate.

        If the color argument is given as well, the function checks to see if the given coordinate's piece
        matches the queried color.
        """
        if color == None:
            if not at.empty:
                return True
            else:
                return False

        else:
            if at.color == color:
                return True
            else:
                return False

class Pawn(Piece):
    """
    Contains attributes of a pawn. Unicode for all black and white pieces switched around since they
    are going to be displayed on a black background
    """
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color
        self.moved = False  # To determine whether the pawn can move two spaces forward
        self.double_step = False  # Used for en passant

    def __repr__(self):
        if self.color == "White":
            return u"\u265f"

        else:
            return u"\u2659"

    def move_set(self, piece, board):
        """Consolidates all the movement set information and returns final list"""
        pass

    def generate_moves(self, piece, board):
        """Takes piece and calculates all the spaces the piece can move to"""
        self.total = []
        if self.color == "White":
            if not self.piece_at(board[piece[0]][piece[1] + 1]):  # If there is not a piece there
                self.total.append((piece[0], piece[1] + 1))  # One square forward

            if not self.moved and not self.piece_at(board[piece[0]][piece[1] + 2]):
                self.total.append((piece[0], piece[1] + 2))  # Two squares forward

        else:   # If piece is black, the math is backwards
            if not self.piece_at(board[piece[0]][piece[1] - 1]):
                self.total.append((piece[0], piece[1] - 1))

            if not self.moved and not self.piece_at(board[piece[0]][piece[1] - 2]):
                self.total.append((piece[0], piece[1] - 2))

        return self.total

    def capture_set(self, piece, board):
        """Creates a list of moves where a piece can be captured by the pawn"""
        self.cset = []
        if self.color == "White":
            if self.piece_at(board[piece[0] - 1][piece[1] + 1], "Black"):
                self.cset.append((piece[0] - 1 , piece[1] + 1))
            if self.piece_at(board[piece[0] + 1][piece[1] + 1], "Black"):
                self.cset.append((piece[0] + 1 , piece[1] + 1))

        else:
            if self.piece_at(board[piece[0] - 1][piece[1] - 1], "White"):
                self.cset.append((piece[0] - 1 , piece[1] - 1))
            if self.piece_at(board[piece[0] + 1][piece[1] - 1], "White"):
                self.cset.append((piece[0] + 1 , piece[1] - 1))

        return self.cset

class Rook(Piece):
    """Contains attributes of a rook"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265C"

        else:
            return u"\u2656"

class Knight(Piece):
    """Contains attributes of a knight"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265E"

        else:
            return u"\u2658"

class Bishop(Piece):
    """Contains attributes of a bishop"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265D"

        else:
            return u"\u2657"

class Queen(Piece):
    """Contains attributes of a queen"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265B"

        else:
            return u"\u2655"

class King(Piece):
    """Contains attributes of a king"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265A"

        else:
            return u"\u2654"


