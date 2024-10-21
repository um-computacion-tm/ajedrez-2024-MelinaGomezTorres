from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition


class Chess:
    # Inicializa el juego de ajedrez.
    def __init__(self):
        # Crea un nuevo tablero y establece el turno inicial en blanco
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    # Verifica si el juego está en curso.
    # Retorna:
    # bool: Verdadero si se está jugando y hay piezas en el tablero.
    def is_playing(self):
        return self.__playing__ and self.__has_pieces__()

    # Mueve una pieza del tablero.
    # Parámetros:
    # from_row (int): Fila de origen de la pieza.
    # from_col (int): Columna de origen de la pieza.
    # to_row (int): Fila de destino para la pieza.
    # to_col (int): Columna de destino para la pieza.
    # Lanza:
    # InvalidMove: Si el movimiento no es válido.
    # EmptyPosition: Si no hay ninguna pieza en la posición de origen.
    # InvalidTurn: Si no es el turno del jugador que intenta mover la pieza.
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
 
    # Valida si un movimiento es posible para la pieza en la posición especificada.
    # Parámetros:
    # piece (Piece): La pieza a mover.
    # from_row (int): Fila de origen.
    # from_col (int): Columna de origen.
    # to_row (int): Fila de destino.
    # to_col (int): Columna de destino.
    # Retorna:
    # bool: Verdadero si el movimiento es válido.
    def __validate_move(self, piece, from_row, from_col, to_row, to_col):
        #return piece.valid_positions(from_row, from_col, to_row, to_col)
        return piece.__valid_positions__(from_row, from_col, to_row, to_col)


    # Verifica si hay piezas de ambos colores en el tablero.
    # Retorna:
    # bool: Verdadero si hay piezas blancas y negras en el tablero.
    def __has_pieces__(self):
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        return white_pieces and black_pieces
    
    # Obtiene el tablero actual.
    # Retorna:
    # Board: El tablero del juego.
    def get_board(self):
        return self.__board__
      
# Propiedad que devuelve el color del turno actual.
    @property
    def turn(self):
        return self.__turn__
    
    # Muestra el tablero en formato de cadena.
    # Retorna:
    # str: Representación en forma de cadena del tablero.
    def show_board(self):
        return str(self.__board__)

    # Cambia el turno al otro jugador.
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    # Finaliza el juego.
    def end_game(self):
        self.__playing__ = False
 
    # Propuesta de empate.
    # Retorna:
    # str: Propuesta de empate.
    def propose_draw(self):
        return "DRAW_PROPOSAL"

    # Sale del juego y lo finaliza.
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


            
















