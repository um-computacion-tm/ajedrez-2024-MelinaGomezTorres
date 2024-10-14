from chess.piece import Piece

#Los símbolos del rey se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__symbol__ = "♚" if color == "WHITE" else "♔"

    def __str__(self):
        return self.__symbol__

    def possible_moves(self, row, col):
        # Movimientos posibles en las ocho direcciones
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [
            (row + dr, col + dc)
            for dr, dc in directions
            if self.__is_valid_move(row + dr, col + dc)
        ]

    def __is_valid_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        piece_at_position = self.__board__.get_piece(row, col)
        return piece_at_position is None or piece_at_position.__color__ != self.__color__











    #def __str__(self):
     #   return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__
