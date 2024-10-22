from chess.piece import Piece

class Bishop(Piece):
    __white_symbol__ = "♝"   # Símbolo del alfil blanco.
    __black_symbol__ = "♗"   # Símbolo del alfil negro.

    def __init__(self, color,board=None):
        """
        Inicializa un alfil con el color especificado.

        Llama al constructor de la clase base con el color (en referencia a "piece.py").

        Parámetros:
            color (str): El color del alfil ('WHITE' o 'BLACK').
            board (Board, opcional): La referencia al tablero en el que se encuentra el alfil.
        """
        super().__init__(color, board)

    def get_possible_positions(self, from_row, from_col):
        """
        Devuelve las posiciones posibles del alfil desde su posición actual.

        Parámetros:
            from_row (int): La fila actual del alfil.
            from_col (int): La columna actual del alfil.

        Retorna:
            list: Una lista de posiciones posibles en forma de coordenadas (fila, columna).
        """
        return self.possible_diagonal_positions(from_row, from_col)
    
    def valid_positions_in_bishop(self, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento del alfil a la posición de destino es válido.

        Parámetros:
            from_row (int): La fila actual del alfil.
            from_col (int): La columna actual del alfil.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Retorna:
            bool: True si el movimiento es válido; False en caso contrario.
        """
        return self.__valid_positions__(from_row, from_col,to_row, to_col)
    
    



    