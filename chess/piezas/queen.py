from chess.piece import Piece

#Los símbolos de la reina se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__white_symbol__ = "♛"  # Símbolo de la reina blanca.
        self.__black_symbol__ = "♕"  # Símbolo de la reina negra. 

    # Devuelve las posiciones posibles de la reina desde su posición actual.
    # Parámetros:
    # from_row (int): La fila actual de la reina.
    # from_col (int): La columna actual de la reina.
    # Retorna:
    # list: Una lista de posiciones posibles en forma de coordenadas (fila, columna).
    def get_possible_positions(self, from_row, from_col):
        # La reina puede moverse en direcciones ortogonales y diagonales
        return (
            self.possible_orthogonal_positions(from_row, from_col) +
            self.possible_diagonal_positions(from_row, from_col)
        )
    
    # Valida los movimientos de la reina usando el método genérico de validación.
    # Parámetros:
    # from_row (int): La fila actual de la reina.
    # from_col (int): La columna actual de la reina.
    # to_row (int): La fila de destino.
    # to_col (int): La columna de destino.
    # Retorna:
    # bool: True si el movimiento es válido; False en caso contrario.
    def valid_positions(self, from_row, from_col, to_row, to_col):
        return self.__valid_positions__(from_row, from_col, to_row, to_col)
    
   




