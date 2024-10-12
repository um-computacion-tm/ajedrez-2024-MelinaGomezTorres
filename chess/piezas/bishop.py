from chess.piece import Piece

#Los símbolos del alfíl se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Bishop(Piece):
    __white_symbol__ = "♝"
    __black_symbol__ = "♗"

    #Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        super().__init__(color, board)

    #def __str__(self):
     #   return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__
    
    #def valid_positions_in_bishop(self, from_row, from_col, to_row, to_col,):
     #   possible_positions = (
      #      self.possible_positions_in_direction(from_row, from_col, 1, 1) +         # Diagonal hacia abajo a la derecha
       #     self.possible_positions_in_direction(from_row, from_col, 1, -1) +        # Diagonal hacia abajo a la izquierda
        #    self.possible_positions_in_direction(from_row, from_col, -1, 1) +        # Diagonal hacia arriba a la derecha
         #   self.possible_positions_in_direction(from_row, from_col, -1, -1)         # Diagonal hacia arriba a la izquierda
         #)
        #return (to_row, to_col) in possible_positions

    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(from_row, from_col)

    def valid_positions_in_bishop(self, from_row, from_col, to_row, to_col):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return self.is_valid_move(to_row, to_col, possible_positions)


    
    #def possible_positions_dtr(self, row, col):
        # diagonal top-right (movimiento hacia arriba a la derecha)
     #   possibles = []
      #  next_row, next_col = row - 1, col + 1
       # while next_row >= 0 and next_col < 8:
        #    piece = self.__board__.get_piece(next_row, next_col)
         #   if piece is None:
          #      possibles.append((next_row, next_col))
           # elif piece.get_color() != self.get_color():  # Pieza del oponente
            #    possibles.append((next_row, next_col))
             #   break  # Detener el bucle si se encuentra una pieza del oponente
            #else:
             #   break  # Detener el bucle si se encuentra una pieza del mismo color
            #next_row -= 1
            #next_col += 1
        #return possibles


    #def possible_positions_dtl(self, row, col):
        # diagonal top-left (movimiento hacia arriba a la izquierda)
     #   possibles = []
      #  next_row, next_col = row - 1, col - 1
       # while next_row >= 0 and next_col >= 0:
        #    piece = self.__board__.get_piece(next_row, next_col)
         #   if piece is None:
          #      possibles.append((next_row, next_col))
           # elif piece.get_color() != self.get_color():  # Pieza del oponente
            #    possibles.append((next_row, next_col))
             #   break  # Detener el bucle si se encuentra una pieza del oponente
            #else:
             #   break  # Detener el bucle si se encuentra una pieza del mismo color
            #next_row -= 1
            #next_col -= 1
        #return possibles
    

    #def possible_positions_dbr(self, row, col):
        # diagonal bottom-right (movimiento hacia abajo a la derecha)
     #   possibles = []
      #  next_row, next_col = row + 1, col + 1
       # while next_row < 8 and next_col < 8:
        #    piece = self.__board__.get_piece(next_row, next_col)
         #   if piece is None:
          #      possibles.append((next_row, next_col))
           # elif piece.get_color() != self.get_color():  # Pieza del oponente
            #    possibles.append((next_row, next_col))
             #   break # Detener el bucle si se encuentra una pieza
            #else:
             #   break # Detener el bucle si se encuentra una pieza del mismo color
            #next_row += 1
            #next_col += 1
        #return possibles


    #def possible_positions_dbl(self, row, col):
        # diagonal bottom-left (movimiento hacia abajo a la izquierda)
     #   possibles = []
      #  next_row, next_col = row + 1, col - 1
       # while next_row < 8 and next_col >= 0:
        #    piece = self.__board__.get_piece(next_row, next_col)
         #   if piece is None:
          #      possibles.append((next_row, next_col))
           # elif piece.get_color() != self.get_color():  # Pieza del oponente
            #    possibles.append((next_row, next_col))
             #   break  # Detener el bucle si se encuentra una pieza del oponente
            #else:
             #   break  # Detener el bucle si se encuentra una pieza del mismo color
            #next_row += 1
            #next_col -= 1
        #return possibles
    


    