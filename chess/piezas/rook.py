from chess.piece import Piece


class Rook(Piece):
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"