from chess.piece import Piece

#Los símbolos del alfíl se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Bishop(Piece):
    __white_symbol__ = "♝"
    __black_symbol__ = "♗"

    #Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        self.__board__ = board
        super().__init__(color)

    def __str__(self):
        return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__
    

    def valid_positions(
         self,
         from_row,
         from_col,
         to_row,
         to_col,
    ):
         possible_positions = (
            # movimientos diagonales
            self.possible_positions_dtr(from_row, from_col) +
            self.possible_positions_dtl(from_row, from_col) 
         )
         return (to_row, to_col) in possible_positions
    
    def possible_positions_dtr(self, row, col):
        # diagonal top-right (movimiento hacia arriba a la derecha)
        possibles = []
        next_row, next_col = row - 1, col + 1
        while next_row >= 0 and next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col += 1
        return possibles

    def possible_positions_dtl(self, row, col):
        # diagonal top-left (movimiento hacia arriba a la izquierda)
        possibles = []
        next_row, next_col = row - 1, col - 1
        while next_row >= 0 and next_col >= 0:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col -= 1
        return possibles