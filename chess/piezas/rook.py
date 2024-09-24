from chess.piece import Piece

#Los símbolos de la torre se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Rook(Piece):
    __white_symbol__ = "♜"
    __black_symbol__ = "♖"

#Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        super().__init__(color, board)


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
            #movimientos horizontales y verticales
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hr(from_row, from_col) + 
            self.possible_positions_hl(from_row, from_col) 
            )
         return (to_row, to_col) in possible_positions
     
    def possible_positions_vd(self, row, col):
       #vertical descendente(moverse  hacia abajo en la misma columna)
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
       #vertical ascendente(se mueve hacia arriba en la misma columna)
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break  
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_hr(self, row, col):
        # Horizontal derecha (moverse hacia la derecha en la misma fila)
        possibles = []
        for next_col in range(col + 1, 8):  # Desde la columna actual hasta la columna 7
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                  possibles.append((row, next_col))
               break  # Se detiene el movimiento si se encuentra cualquier pieza
            possibles.append((row, next_col))
        return possibles


    def possible_positions_hl(self, row, col):
        # Horizontal izquierda (moverse hacia la izquierda en la misma fila)
        possibles = []
        for next_col in range(col - 1, -1, -1):  # Hasta la columna 0
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
               break
            possibles.append((row, next_col))
        return possibles

    
    
    
    
