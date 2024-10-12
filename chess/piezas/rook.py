from chess.piece import Piece

#Los símbolos de la torre se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Rook(Piece):
    __white_symbol__ = "♜"
    __black_symbol__ = "♖"

#Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        super().__init__(color, board)

#Verifica si un movimiento de la torre es válido
#Llama al método possible_positions_direction para obtener las posiciones posibles y comprueba si la posición de destino está en esa lista
    #def valid_positions(self, from_row, from_col, to_row, to_col):
     #   possible_positions = (
      #      #movimientos horizontales y verticales
       #     self.possible_positions_in_direction(from_row, from_col, 1, 0) +   # Vertical descendente
        #    self.possible_positions_in_direction(from_row, from_col, -1, 0) +  # Vertical ascendente
         #   self.possible_positions_in_direction(from_row, from_col, 0, 1) +   # Horizontal derecha
          #  self.possible_positions_in_direction(from_row, from_col, 0, -1)    # Horizontal izquierda
        #)
        #return (to_row, to_col) in possible_positions

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col)
    
    def valid_positions_in_rook(self, from_row, from_col, to_row, to_col):
        return self.valid_positions(from_row, from_col, to_row, to_col)

    

#Genera las posiciones posibles en una dirección específica (definida por `row_step` y `col_step`) 
#Recorre esas posiciones hasta encontrar el borde del tablero o una pieza
#Si encuentra una pieza del color contrario, agrega su posición a la lista; si no, se detiene
#Luego retorna todas las posiciones válidas que puede ocupar la torre en esa dirección
    #def possible_positions_direction(self, row, col, row_step, col_step):
     #   possibles = []
      #  next_row, next_col = row + row_step, col + col_step
       # while 0 <= next_row < 8 and 0 <= next_col < 8:
        #    other_piece = self.__board__.get_piece(next_row, next_col)
         #   if other_piece is not None:
          #      if other_piece.__color__ != self.__color__:
           #         possibles.append((next_row, next_col))
            #    break
            #possibles.append((next_row, next_col))
            #next_row += row_step
            #next_col += col_step
        #return possibles



    
    
    
    
