from chess.piece import Piece

#Los símbolos de la torre se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Rook(Piece):
    __white_symbol__ = "♜"
    __black_symbol__ = "♖"

# Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        self.__board__ = board
        super().__init__(color)

    def __str__(self):
        return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__

    
    """def possible_positions_vd(self, x, y):
        positions = []
        for i in range(x + 1, 8):
            piece_at_position = self.__board__.get_piece(i, y)
            if piece_at_position is None:
                positions.append((i, y))
            elif piece_at_position.__color__ != self.__board__.get_piece(x, y).__color__:
                positions.append((i, y))
                break
            else:
                break
        return positions
    
    def possible_positions_va(self, x, y):
        positions = []
        for i in range(x - 1, -1, -1):
            piece_at_position = self.__board__.get_piece(i, y)
            if piece_at_position is None:
                positions.append((i, y))
            elif piece_at_position.__color__ != self.__board__.get_piece(x, y).__color__:
                positions.append((i, y))
                break
            else:
                break
        return positions"""
