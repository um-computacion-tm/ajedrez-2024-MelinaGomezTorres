from chess.piezas.rook import Rook
from chess.piezas.knight import Knight
from chess.piezas.bishop import Bishop
from chess.piezas.queen import Queen
from chess.piezas.king import King
from chess.piezas.pawn import Pawn

from chess.exceptions import OutOfBoard

class Board:
    """
    Clase que representa un tablero de ajedrez de 8x8.
    """
    def __init__(self, for_test=False ):
        """
        Inicializa un tablero vacío de 8x8 y coloca las piezas en sus posiciones iniciales.

        Parámetros:
            for_test (bool): Si es True, no se inician las piezas.
        """
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_pieces()

    # Inicializa las piezas en el tablero.
    def __initialize_pieces(self, for_test=False):
        """
        Inicializa las piezas en el tablero.

        Parámetros:
            for_test (bool): Si es True, no se inician las piezas.

        Realiza:
            - Configura las posiciones iniciales de las piezas en el tablero utilizando un diccionario.
        """
        if for_test:
            return
    #Diccionario que define las posiciones iniciales de cada tipo de pieza en el tablero
        piece_setup = {
            "Rook": [                              #Torre
                (0, 0, "BLACK"), (0, 7, "BLACK"),
                (7, 0, "WHITE"), (7, 7, "WHITE")
            ],
            "Knight": [                            #Caballo
                (0, 1, "BLACK"), (0, 6, "BLACK"),
                (7, 1, "WHITE"), (7, 6, "WHITE")
            ],    
            "Bishop": [                            #Alfíl
                (0, 2, "BLACK"), (0, 5, "BLACK"),
                (7, 2, "WHITE"), (7, 5, "WHITE")
            ],            
            "Queen": [                             #Reina
                (0, 3, "BLACK"),
                (7, 3, "WHITE")
            ],
            "King": [                              #Rey
                (0, 4, "BLACK"),
                (7, 4, "WHITE")
            ],                
            "Pawn": [                              #Peón
                (1, i, "BLACK") for i in range(8)
            ] + [
                (6, i, "WHITE") for i in range(8)
            ]
        }
    #Se recorre el diccionario para colocar cada tipo de pieza en su posición correspondiente
        for piece, positions in piece_setup.items():
    #Para cada pieza se toman las posiciones definidas
            for x, y, color in positions:
    #Asigna en el tablero (self.__positions__) la pieza correspondiente en su posición (x, y)
    #Se usa globals() para crear la instancia de la pieza
                self.__positions__[x][y] = globals()[piece](color, self)
   
    def __str__(self):
        """
        Representa el tablero como una cadena para su visualización.

        Retorna:
            str: Representación en forma de cadena del tablero.

        Realiza:
            - Genera una representación visual del tablero con filas y columnas, mostrando las piezas y espacios vacíos.
        """
        board_str = "  0 1 2 3 4 5 6 7\n"  # Encabezado de columnas
        board_str += "  ----------------\n"
        
        for row_idx, row in enumerate(self.__positions__):
            board_str += str(row_idx) + "|"  # Encabezado de filas
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". "  # Punto para espacios vacíos
            board_str += "|" + str(row_idx) + "\n"  # Cierra la fila con el número de fila
        board_str += "  ----------------\n"
        board_str += "  0 1 2 3 4 5 6 7\n"  # Pie de columnas
        return board_str
    
    def get_piece(self, row, col):
        """
        Obtiene la pieza en una posición específica del tablero.

        Parámetros:
            row (int): Fila de la posición.
            col (int): Columna de la posición.

        Retorna:
            Piece: La pieza en la posición especificada.

        Lanza:
            OutOfBoard: Si las coordenadas están fuera de los límites del tablero.

        Realiza:
            - Verifica si la posición está dentro de los límites del tablero y retorna la pieza correspondiente.
        """
        if row < 0 or row >= len(self.__positions__) or col < 0 or col >= len(self.__positions__[0]):
            raise OutOfBoard("La posición indicada se encuentra fuera del tablero")
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        """
        Establece una pieza en una posición específica del tablero.

        Parámetros:
            row (int): Fila de la posición.
            col (int): Columna de la posición.
            piece (Piece): La pieza a colocar en la posición.

        Realiza:
            - Coloca la pieza en la posición especificada del tablero.
        """
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza de una posición a otra.

        Parámetros:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Realiza:
            - Obtiene la pieza en la posición de origen y la coloca en la posición de destino.
            - Limpia la posición de origen.
        """
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    

    