from chess.piece import Piece

#Los símbolos del caballo se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__white_symbol__ = "♞"
        self.__black_symbol__ = "♘"

    '''def __init__(self, color, board=None):
        super().__init__(color, board)  # Pasar 'board' al constructor de la clase base'''



    #def __str__(self):
     #   return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__