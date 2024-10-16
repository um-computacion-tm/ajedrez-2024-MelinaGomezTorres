from chess.piece import Piece  

#Los símbolos del peón se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza         
class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__white_symbol__ = "♟"
        self.__black_symbol__ = "♙"
        self.__has_moved__ = False  # Indica si el peón ya se ha movido

    def get_possible_positions(self, from_row, from_col):
        possibles = []
        direction = -1 if self.get_color() == "WHITE" else 1  # Los peones blancos se mueven hacia arriba (-1), los negros hacia abajo (+1)

        # Movimiento hacia adelante
        next_row = from_row + direction
        if self.__board__.get_piece(next_row, from_col) is None:  # Solo puede avanzar si la casilla está vacía
            possibles.append((next_row, from_col))

            # Movimiento doble hacia adelante si es el primer movimiento
            if not self.__has_moved__ and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                possibles.append((from_row + 2 * direction, from_col))

        # Captura diagonal
        possibles += self.possible_diagonal_capture(from_row, from_col, direction)

        return possibles

    def possible_diagonal_capture(self, from_row, from_col, direction):
        captures = []
        for col_delta in [-1, 1]:  # Diagonales izquierda y derecha
            to_row = from_row + direction
            to_col = from_col + col_delta
            if 0 <= to_col < 8:  # Verifica que no salga del tablero
                other_piece = self.__board__.get_piece(to_row, to_col)
                if other_piece is not None and other_piece.get_color() != self.get_color():  # Puede capturar si es una pieza enemiga
                    captures.append((to_row, to_col))
        return captures

    def valid_positions(self, from_row, from_col, to_row, to_col):
        valid = super().valid_positions(from_row, from_col, to_row, to_col)
        if valid:
            self.__has_moved__ = True  # Marca que el peón ya ha hecho su primer movimiento
        return valid









    #def __str__(self):
     #   return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__
