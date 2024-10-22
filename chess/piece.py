class Piece:
    """
    Clase base que representa una pieza de ajedrez.
    """

    def __init__(self, color ,board):
        """
        Inicializa una pieza de ajedrez.

        Parámetros:
            color (str): Color de la pieza ("WHITE" o "BLACK").
            board (Board): Referencia al tablero donde se encuentra la pieza.

        Realiza:
            - Asigna el color de la pieza y referencia al tablero en el que se encuentra.
        """
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        """
        Devuelve una representación en cadena de la pieza, mostrando su símbolo según su color.

        Retorna:
            str: Símbolo visual de la pieza.

        Realiza:
            - Obtiene el símbolo correspondiente al color de la pieza utilizando el atributo adecuado.
        """
        return getattr(self, f"__{self.__color__.lower()}_symbol__", "")
         
    def get_color(self):
        """
        Obtiene el color de la pieza.

        Retorna:
            str: Color de la pieza.

        Realiza:
            - Retorna el color que se asignó a la pieza en su inicialización.
        """
        return self.__color__
    
    def __valid_positions__(self, from_row, from_col, to_row, to_col):
        """
        Determina si un movimiento propuesto para una pieza es permitido o no según las reglas de la pieza específica y el tablero.

        Parámetros:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Retorna:
            bool: Verdadero si el movimiento es válido; de lo contrario, falso.

        Realiza:
            - Obtiene las posiciones posibles para la pieza y valida si el movimiento está permitido.
        """
    #Método genérico para validar posiciones
        possible_positions = self.get_possible_positions(from_row, from_col)
        return self.is_valid_move(to_row, to_col, possible_positions)
    
    def is_valid_move(self, to_row, to_col, possible_positions):
        """
        Verifica si la posición de destino es válida comparándola con las posiciones posibles.

        Parámetros:
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
            possible_positions (list): Lista de posiciones posibles.

        Retorna:
            bool: Verdadero si la posición es válida; de lo contrario, falso.

        Realiza:
            - Comprueba si la posición de destino está en la lista de posiciones posibles.
        """
        return (to_row, to_col) in possible_positions
  
    def get_possible_positions(self, from_row, from_col):
        """
        Este método será sobrescrito por las subclases para proporcionar posiciones posibles.

        Parámetros:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.

        Retorna:
            list: Lista de posiciones posibles.

        Realiza:
            - Devuelve una lista vacía como método genérico para ser sobrescrito.
        """
        return []

    def possible_diagonal_positions(self, from_row, from_col):
        """
        Obtiene todas las posiciones diagonales posibles desde una posición dada.

        Parámetros:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.

        Retorna:
            list: Lista de posiciones diagonales válidas.

        Realiza:
            - Llama a un método que calcula las posiciones válidas en las cuatro direcciones diagonales.
        """
        return (
            self.possible_positions_in_direction(from_row, from_col, -1, -1) +  # Diagonal arriba-izquierda
            self.possible_positions_in_direction(from_row, from_col, -1, 1) +   # Diagonal arriba-derecha
            self.possible_positions_in_direction(from_row, from_col, 1, -1) +   # Diagonal abajo-izquierda
            self.possible_positions_in_direction(from_row, from_col, 1, 1)      # Diagonal abajo-derecha
        )
    
    def possible_orthogonal_positions(self, from_row, from_col):
        """
        Obtiene todas las posiciones ortogonales posibles desde una posición dada.

        Parámetros:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.

        Retorna:
            list: Lista de posiciones ortogonales válidas.

        Realiza:
            - Llama a un método que calcula las posiciones válidas en las cuatro direcciones ortogonales.
        """
        return (
            self.possible_positions_in_direction(from_row, from_col, 1, 0) +    # Vertical descendente
            self.possible_positions_in_direction(from_row, from_col, -1, 0) +   # Vertical ascendente
            self.possible_positions_in_direction(from_row, from_col, 0, 1) +    # Horizontal derecha
            self.possible_positions_in_direction(from_row, from_col, 0, -1)     # Horizontal izquierda
        )
    
    def possible_positions_in_direction(self, row, col, row_delta, col_delta):
        """
        Calcula todas las posiciones válidas en una dirección particular, hasta que encuentra una pieza o sale del tablero.

        Parámetros:
            row (int): Fila de origen.
            col (int): Columna de origen.
            row_delta (int): Cambio en la fila para la dirección.
            col_delta (int): Cambio en la columna para la dirección.

        Retorna:
            list: Lista de posiciones válidas en la dirección especificada.

        Realiza:
            - Recorre la dirección dada y añade las posiciones válidas a una lista hasta encontrar una pieza o salir del tablero.
        """
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