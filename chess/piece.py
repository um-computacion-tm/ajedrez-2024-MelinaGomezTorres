class Piece:
    def __init__(self, color ,board):
        self.__color__ = color
        self.__board__ = board

#Cambio de codigo para que las piezas sean más visuales y fáciles de identificar en el juego
    def __str__(self):
        #Obtiene el símbolo de la pieza según su color
        return getattr(self, f"__{self.__color__.lower()}_symbol__", "")
        
    def get_color(self):
        return self.__color__
    
    #Determina si un movimiento propuesto para una pieza es permitido o no según las reglas de la pieza específica y el tablero
    def __valid_positions__(self, from_row, from_col, to_row, to_col):
    #Método genérico para validar posiciones
        possible_positions = self.get_possible_positions(from_row, from_col)
        return self.is_valid_move(to_row, to_col, possible_positions)
    
    def is_valid_move(self, to_row, to_col, possible_positions):
    #Verifica si la posición de destino es válida
        return (to_row, to_col) in possible_positions

    def get_possible_positions(self, from_row, from_col):
    #Este método será sobrescrito por las subclases
        return []

    def possible_diagonal_positions(self, from_row, from_col):
        # Llama al método genérico para las 4 direcciones diagonales
        return (
            self.possible_positions_in_direction(from_row, from_col, -1, -1) +  # Diagonal arriba-izquierda
            self.possible_positions_in_direction(from_row, from_col, -1, 1) +   # Diagonal arriba-derecha
            self.possible_positions_in_direction(from_row, from_col, 1, -1) +   # Diagonal abajo-izquierda
            self.possible_positions_in_direction(from_row, from_col, 1, 1)      # Diagonal abajo-derecha
        )

    def possible_orthogonal_positions(self, from_row, from_col):
        # Llama al método genérico para las 4 direcciones ortogonales (vertical y horizontal)
        return (
            self.possible_positions_in_direction(from_row, from_col, 1, 0) +    # Vertical descendente
            self.possible_positions_in_direction(from_row, from_col, -1, 0) +   # Vertical ascendente
            self.possible_positions_in_direction(from_row, from_col, 0, 1) +    # Horizontal derecha
            self.possible_positions_in_direction(from_row, from_col, 0, -1)     # Horizontal izquierda
        )
    
    #Calcula todas las posiciones válidas en una dirección particular, hasta que encuentra una pieza o sale del tablero
    def possible_positions_in_direction(self, row, col, row_delta, col_delta):
        possibles = []
        next_row = row + row_delta
        next_col = col + col_delta
        while 0 <= next_row < 8 and 0 <= next_col < 8:  # Verifica límites del tablero
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.__color__:  # Si es del oponente puede capturarla
                    possibles.append((next_row, next_col))
                break  # Detiene si encuentra una pieza
            possibles.append((next_row, next_col))  # Celda vacía es válida
            next_row += row_delta
            next_col += col_delta
        return possibles