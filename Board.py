from Move import Move

class Board(Move):
    """Manipulates the chess board"""
    def __init__(self):
        """Calls create_board method to make the initialize the board when Board is instantiated"""
        self.main_board = self.set_new_game()

    def __repr__(self):
        """Formats how the board will be displayed. Displays rank and file letters/numbers and pieces"""
        disp = u"  1 2 3 4 5 6 7 8\n"
        for row in xrange(8):
            disp += chr(ord('A') + row) + ' '
            for col in xrange(8):
                disp += unicode(self.main_board[row][col]) + ' '

            disp += '\n'

        return disp.encode('utf8')


