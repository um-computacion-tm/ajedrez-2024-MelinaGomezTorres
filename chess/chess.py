from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition


class Chess:
    """
    Clase que representa un juego de ajedrez.
    """
    def __init__(self):
        """
        Inicializa el juego de ajedrez, creando un nuevo tablero y estableciendo el turno inicial en blanco.
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    def is_playing(self):
        """
        Verifica si el juego está en curso.

        Retorna:
            bool: Verdadero si se está jugando y hay piezas en el tablero.
        """
        return self.__playing__ and self.__has_pieces__()

    def move(self, from_row, from_col, to_row, to_col, ):
        """
        Mueve una pieza del tablero.

        Parámetros:
            from_row (int): Fila de origen de la pieza.
            from_col (int): Columna de origen de la pieza.
            to_row (int): Fila de destino para la pieza.
            to_col (int): Columna de destino para la pieza.

        Lanza:
            InvalidMove: Si el movimiento no es válido.
            EmptyPosition: Si no hay ninguna pieza en la posición de origen.
            InvalidTurn: Si no es el turno del jugador que intenta mover la pieza.
        
        Realiza:
            - Verifica si el juego está en curso.
            - Obtiene la pieza en la posición de origen.
            - Verifica si hay una pieza en la posición de origen y si es del color del jugador actual.
            - Valida el movimiento de la pieza.
            - Mueve la pieza de la posición de origen a la de destino.
            - Cambia el turno al otro jugador.
        """
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
 
    def __validate_move(self, piece, from_row, from_col, to_row, to_col):
        """
        Valida si un movimiento es posible para la pieza en la posición especificada.

        Parámetros:
            piece (Piece): La pieza a mover.
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Retorna:
            bool: Verdadero si el movimiento es válido.

        Realiza:
            - Llama al método __valid_positions__ de la pieza para comprobar la validez del movimiento.
        """
        return piece.__valid_positions__(from_row, from_col, to_row, to_col)

    def __has_pieces__(self):
        """
        Verifica si hay piezas de ambos colores en el tablero.

        Este método revisa la configuración del tablero para determinar si hay piezas blancas y negras presentes.
        Si alguno de los dos colores no tiene piezas, se imprime un mensaje indicando que el juego ha terminado.

        Retorna:
            bool: Verdadero si hay piezas blancas y negras en el tablero, Falso en caso contrario.
        
        Realiza:
            - Revisa el tablero para determinar si hay piezas blancas y negras.
            - Imprime un mensaje si alguno de los dos colores no tiene piezas.
        """
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        if not(white_pieces and black_pieces):
            print ('Un jugador se ha quedado sin piezas. El juego ha terminado.')
        return white_pieces and black_pieces
    
    def get_board(self):
        """
        Obtiene el tablero actual.

        Retorna:
            Board: El tablero del juego.

        Realiza:
            - Retorna la instancia del tablero.
        """
        return self.__board__
      
    @property
    def turn(self):
        """
        Propiedad que devuelve el color del turno actual.

        Retorna:
            str: Color del turno actual ("WHITE" o "BLACK").
        """
        return self.__turn__
    
    def show_board(self):
        """
        Muestra el tablero en formato de cadena.

        Retorna:
            str: Representación en forma de cadena del tablero.

        Realiza:
            - Llama al método __str__ del tablero para obtener su representación.
        """
        return str(self.__board__)

    def change_turn(self):
        """
        Cambia el turno al otro jugador.

        Realiza:
            - Alterna el valor de __turn__ entre "WHITE" y "BLACK".
        """
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def end_game(self):
        """
        Finaliza el juego.

        Realiza:
            - Cambia el estado de __playing__ a False.
        """
        self.__playing__ = False
 
    def propose_draw(self):
        """
        Propuesta de empate.

        Retorna:
            str: Propuesta de empate ("DRAW_PROPOSAL").

        Realiza:
            - Retorna un mensaje de propuesta de empate.
        """
        return "DRAW_PROPOSAL"

    def exit_game(self):
        """
        Sale del juego y lo finaliza.

        Realiza:
            - Cambia el estado de __playing__ a False.
        """
        self.__playing__ = False


        



















