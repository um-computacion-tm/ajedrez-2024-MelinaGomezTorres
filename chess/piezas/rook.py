from chess.piece import Piece

#Los símbolos de la torre se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Rook(Piece):
    __white_symbol__ = "♜"
    __black_symbol__ = "♖"

#Llama al constructor de la clase base con el color (en referencia a "piece.py")
    def __init__(self, color,board=None):
        super().__init__(color, board)


    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col)
    


    
    
    
    
