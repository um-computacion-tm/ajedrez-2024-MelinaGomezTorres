from chess.piece import Piece  

#Los símbolos del peón se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza         
class Pawn(Piece):
    __white_symbol__ = "♟"
    __black_symbol__ = "♙"

    def __str__(self):
        return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__
