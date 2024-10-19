from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    def is_playing(self):
        return self.__playing__ and self.__has_pieces__()

    def move(self, from_row, from_col, to_row, to_col, ):
        if not self.is_playing():
            raise InvalidMove("El juego ha terminado.")

        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise EmptyPosition(f"No hay ninguna pieza en la posición ({from_row}, {from_col}).")
        
        if piece.get_color() != self.__turn__:
            raise InvalidTurn(f"Es el turno de {self.__turn__}, no puedes mover una pieza {piece.get_color()}.")

        if not self.__validate_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMove(f"Movimiento inválido para la pieza {piece}.")

        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()

        if not self.__has_pieces__():
            self.end_game()

    def __validate_move(self, piece, from_row, from_col, to_row, to_col):
        return piece.valid_positions(from_row, from_col, to_row, to_col)

    def __has_pieces__(self):
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        return white_pieces and black_pieces
    
    def get_board(self):
        return self.__board__
      
    
    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def end_game(self):
        self.__playing__ = False

    def propose_draw(self):
        return "DRAW_PROPOSAL"

    def exit_game(self):
        self.__playing__ = False


        




'''class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    def is_playing(self):
        return self.__playing__ and self.__has_pieces__()

    def move(self, from_row, from_col, to_row, to_col):
        if not self.is_playing():
            raise InvalidMove("El juego ha terminado.")

        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise EmptyPosition(f"No hay ninguna pieza en la posición ({from_row}, {from_col}).")
        
        if piece.get_color() != self.__turn__:
            raise InvalidTurn(f"Es el turno de {self.__turn__}, no puedes mover una pieza {piece.get_color()}.")

        if not self.__validate_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMove(f"Movimiento inválido para la pieza {piece}.")

        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()

        if not self.__has_pieces__():
            self.end_game()

    def __validate_move(self, piece, from_row, from_col, to_row, to_col):
        return piece.valid_positions(from_row, from_col, to_row, to_col)

    def __has_pieces__(self):
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        return white_pieces and black_pieces
    
    def get_board(self):
        return self.__board__

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def end_game(self):
        self.__playing__ = False

    def propose_draw(self):
        return "DRAW_PROPOSAL"

    def exit_game(self):
        self.__playing__ = False'''


            
















