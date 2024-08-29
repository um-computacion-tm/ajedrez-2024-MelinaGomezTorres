from chess.piece import Piece


class Rook(Piece):
    def __str__(self):
        return "♜" if self.__color__ == "WHITE" else "♖"
