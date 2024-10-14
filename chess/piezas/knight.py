from chess.piece import Piece

#Los símbolos del caballo se guardan como atributos
#Luego, en el método __str__, selecciona el símbolo correcto basado en el color de la pieza 
class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.__symbols__ = { "white": "♞" , "black": "♘" }
        
    def __str__(self):
        return self.__symbols__[self.__color__.lower()]

    def get_possible_positions(self, from_row, from_col):
        # El caballo puede moverse en forma de "L"
        possible_moves = [
            (from_row + 2, from_col + 1), (from_row + 2, from_col - 1),
            (from_row - 2, from_col + 1), (from_row - 2, from_col - 1),
            (from_row + 1, from_col + 2), (from_row + 1, from_col - 2),
            (from_row - 1, from_col + 2), (from_row - 1, from_col - 2)
        ]

        # Filtra las posiciones válidas dentro del tablero
        valid_moves = []
        for row, col in possible_moves:
            if 0 <= row < 8 and 0 <= col < 8:  # Verifica que esté dentro de los límites del tablero
                other_piece = self.__board__.get_piece(row, col)
                if other_piece is None or other_piece.get_color() != self.__color__:
                    valid_moves.append((row, col))  # Puede moverse o capturar

        return valid_moves






    #def __str__(self):
     #   return self.__white_symbol__ if self.__color__ == "WHITE" else self.__black_symbol__