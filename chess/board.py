from chess.piezas.rook import Rook
#from chess.piezas.knight import Knight
#from chess.piezas.bishop import Bishop
#from chess.piezas.queen import Queen
#from chess.piezas.king import King
#from chess.piezas.pawn import Pawn

#Creo un tablero vacío de 8x8 
#Utilizo un método para configurar la torre y la coloco en el tablero
class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_pieces()

    def __initialize_pieces(self):
         self.__setup_rooks()

    def __setup_rooks(self):
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        
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
        return self.__positions__[row][col]