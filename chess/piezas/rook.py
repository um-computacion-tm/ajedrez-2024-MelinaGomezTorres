from chess.piece import Piece

class Rook(Piece):
    '''
    Los símbolos de la torre se guardan como atributos.
    Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza.
    '''
    __white_symbol__ = "♜"  # Símbolo de la torre blanca.
    __black_symbol__ = "♖"  # Símbolo de la torre negra.


    def __init__(self, color,board=None):
        """
        Inicializa una torre con el color especificado.

        Llama al constructor de la clase base con el color (en referencia a "piece.py").

        Parámetros:
            color (str): El color de la torre ('WHITE' o 'BLACK').
            board (Board, opcional): La referencia al tablero en el que se encuentra la torre.
        """
        super().__init__(color, board)

    def get_possible_positions(self, from_row, from_col):
        """
        Devuelve las posiciones posibles de la torre desde su posición actual.

        La torre puede moverse en líneas rectas, ya sea vertical u horizontalmente.

        Parámetros:
            from_row (int): La fila actual de la torre.
            from_col (int): La columna actual de la torre.

        Retorna:
            list: Una lista de posiciones válidas en forma de coordenadas (fila, columna).
        """
        return self.possible_orthogonal_positions(from_row, from_col)
    


    
    
    
    
