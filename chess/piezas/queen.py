from chess.piece import Piece

class Queen(Piece):
    """
    Los símbolos de la reina se guardan como atributos.
    Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza.
    """
    def __init__(self, color, board):
        """
        Inicializa una reina con el color especificado.

        Parámetros:
            color (str): El color de la reina ('WHITE' o 'BLACK').
            board (Board): La referencia al tablero en el que se encuentra la reina.
        """
        super().__init__(color, board)
        self.__white_symbol__ = "♛"  # Símbolo de la reina blanca.
        self.__black_symbol__ = "♕"  # Símbolo de la reina negra. 

    def get_possible_positions(self, from_row, from_col):
        """
        Devuelve las posiciones posibles de la reina desde su posición actual.

        La reina puede moverse en direcciones ortogonales y diagonales.

        Parámetros:
            from_row (int): La fila actual de la reina.
            from_col (int): La columna actual de la reina.

        Retorna:
            list: Una lista de posiciones posibles en forma de coordenadas (fila, columna).
        """
        return (
            self.possible_orthogonal_positions(from_row, from_col) +
            self.possible_diagonal_positions(from_row, from_col)
        )
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        """
        Valida los movimientos de la reina usando el método genérico de validación.

        Parámetros:
            from_row (int): La fila actual de la reina.
            from_col (int): La columna actual de la reina.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Retorna:
            bool: True si el movimiento es válido; False en caso contrario.
        """
        return self.__valid_positions__(from_row, from_col, to_row, to_col)
    
   




