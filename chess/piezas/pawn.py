from chess.piece import Piece


class Pawn(Piece):
    def __str__(self):
        return "♟" if self.__color__ == "WHITE" else "♙"   

        

