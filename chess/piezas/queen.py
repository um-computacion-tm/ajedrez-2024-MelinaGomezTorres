from chess.piece import Piece

#Los símbolos de la reina se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__white_symbol__ = "♛"
        self.__black_symbol__ = "♕"

    def get_possible_positions(self, from_row, from_col):
        # La reina puede moverse en direcciones ortogonales y diagonales
        return (
            self.possible_orthogonal_positions(from_row, from_col) +
            self.possible_diagonal_positions(from_row, from_col)
        )

    def valid_positions_in_queen(self, from_row, from_col, to_row, to_col):
        # Validar movimientos usando el método genérico de validación
        return self.valid_positions(from_row, from_col, to_row, to_col)



    #def __str__(self):
      #  return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__