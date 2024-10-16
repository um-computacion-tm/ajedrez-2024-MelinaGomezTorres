from chess.piezas.rook import Rook
from chess.piezas.knight import Knight
from chess.piezas.bishop import Bishop
from chess.piezas.queen import Queen
from chess.piezas.king import King
from chess.piezas.pawn import Pawn

from chess.exceptions import OutOfBoard

#Creo un tablero vacío de 8x8 
#Utilizo un método para configurar la torre, caballo, alfíl, reina, rey y peón colocandolos en el tablero
#(Defino las posiciones en el tablero de las piezas blancas y negras)

#Modifico el código anterior para iniciar todas las piezas en una sola función usando un diccionario y bucles para evitar repeticiones
class Board:
    def __init__(self, for_test=False ):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_pieces()

    def __initialize_pieces(self, for_test=False):
    #Si for_test es True, no se inician las piezas
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
        
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):
        # Verifica que las coordenadas estén dentro de los límites del tablero
        if row < 0 or row >= len(self.__positions__) or col < 0 or col >= len(self.__positions__[0]):
            raise OutOfBoard("La posición indicada se encuentra fuera del tablero")
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    