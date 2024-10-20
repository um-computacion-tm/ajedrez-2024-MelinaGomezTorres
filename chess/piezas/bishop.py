from chess.piece import Piece

# Representa un alfil en el juego de ajedrez.
#Los símbolos del alfíl se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 

class Bishop(Piece):
    __white_symbol__ = "♝"   # Símbolo del alfil blanco.
    __black_symbol__ = "♗"   # Símbolo del alfil negro.

    #Llama al constructor de la clase base con el color (en referencia a "piece.py")
    #Inicializa un alfil con el color especificado.
    # Parámetros:
    # color (str): El color del alfil ('WHITE' o 'BLACK').
    # board (Board, opcional): La referencia al tablero en el que se encuentra el alfil.
    
    def __init__(self, color,board=None):
        super().__init__(color, board)

    # Devuelve las posiciones posibles del alfil desde su posición actual.
    # Parámetros:
    # from_row (int): La fila actual del alfil.
    # from_col (int): La columna actual del alfil.
    # Retorna:
    # list: Una lista de posiciones posibles en forma de coordenadas (fila, columna).
    def get_possible_positions(self, from_row, from_col):
        # Devuelve las posiciones posibles del alfil desde su posición actual.
        return self.possible_diagonal_positions(from_row, from_col)
    
    # Verifica si el movimiento del alfil a la posición de destino es válido.
    # Parámetros:
    # from_row (int): La fila actual del alfil.
    # from_col (int): La columna actual del alfil.
    # to_row (int): La fila de destino.
    # to_col (int): La columna de destino.
    # Retorna:
    # bool: True si el movimiento es válido; False en caso contrario.
    def valid_positions_in_bishop(self, from_row, from_col, to_row, to_col):
        # Verifica si el movimiento del alfil a la posición de destino es válido.
        return self.__valid_positions__(from_row, from_col,to_row, to_col)
    
    



    