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
class Board:
    def __init__(self, for_test=False ):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_pieces()

    def __initialize_pieces(self):
         self.__setup_rooks()
         self.__setup_knights()
         self.__setup_bishops()
         self.__setup_royalty()
         self.__setup_pawns()

#Incluyo self como segundo argumento
    def __setup_rooks(self):                           #Torre
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

    def __setup_knights(self):                         #Caballo
        self.__positions__[0][1] = Knight("BLACK", self)
        self.__positions__[0][6] = Knight("BLACK", self)
        self.__positions__[7][1] = Knight("WHITE", self)
        self.__positions__[7][6] = Knight("WHITE", self)

    def __setup_bishops(self):                         #Alfíl
        self.__positions__[0][2] = Bishop("BLACK", self)
        self.__positions__[0][5] = Bishop("BLACK", self)
        self.__positions__[7][2] = Bishop("WHITE", self)
        self.__positions__[7][5] = Bishop("WHITE", self)
        
    def __setup_royalty(self):                         #Reina y Rey
        self.__positions__[0][3] = Queen("BLACK", self)
        self.__positions__[0][4] = King("BLACK", self)
        self.__positions__[7][3] = Queen("WHITE", self)
        self.__positions__[7][4] = King("WHITE", self)

    def __setup_pawns(self):                           #Peón
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK", self)
            self.__positions__[6][i] = Pawn("WHITE", self)


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