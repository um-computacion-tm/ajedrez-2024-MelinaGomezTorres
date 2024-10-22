from chess.piece import Piece

class King(Piece):
    """
    Los símbolos del rey se guardan como atributos.
    Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza.
    """
    def __init__(self, color, board):
        """
        Inicializa un rey con el color especificado.

        Parámetros:
            color (str): El color del rey ('WHITE' o 'BLACK').
            board (Board): La referencia al tablero en el que se encuentra el rey.
        """
        super().__init__(color, board)
        self.__king_symbol__ = "♚" if color == "WHITE" else "♔"

    def __str__(self):
        """
        Devuelve el símbolo correspondiente del rey según su color.

        Retorna:
            str: El símbolo del rey (♚ para blanco, ♔ para negro).
        """
        return self.__king_symbol__
    
    def get_possible_positions(self, row, col):
        """
        Devuelve los movimientos posibles del rey en las ocho direcciones.

        Parámetros:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Retorna:
            list: Una lista de posiciones posibles en forma de coordenadas (fila, columna).
        """
        # Movimientos posibles en las ocho direcciones
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [
            (row + dr, col + dc)
            for dr, dc in directions
            if self.__is_valid_move__(row + dr, col + dc)
        ]

    def __is_valid_move__(self, row, col):
        """
        Verifica si el movimiento a la posición especificada es válido.

        Parámetros:
            row (int): La fila de destino.
            col (int): La columna de destino.

        Retorna:
            bool: True si el movimiento es válido; False en caso contrario.
        """
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        piece_at_position = self.__board__.get_piece(row, col)
        return piece_at_position is None or piece_at_position.__color__ != self.__color__
