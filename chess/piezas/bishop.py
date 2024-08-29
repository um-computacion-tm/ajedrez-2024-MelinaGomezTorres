from chess.piece import Piece


class Bishop(Piece):
    def __str__(self):
        return "♝" if self.__color__ == "WHITE" else "♗"
