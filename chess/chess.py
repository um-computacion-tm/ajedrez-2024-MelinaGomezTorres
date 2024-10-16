'''from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"'''


from chess.board import Board
from chess.piezas.rook import Rook
from chess.piezas.knight import Knight
from chess.piezas.bishop import Bishop
from chess.piezas.queen import Queen
from chess.piezas.king import King
from chess.piezas.pawn import Pawn

from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

'''class Chess:
    def __init__(self):
        # Inicializa el tablero
        self.__board__ = Board()
        # El turno comienza con las piezas blancas
        self.__turn__ = "WHITE"
        # Indica si el juego está activo
        self.__playing__ = True

    def is_playing(self):
        # El juego continúa solo si ambas condiciones se cumplen:
        # 1. Hay piezas de ambos jugadores en el tablero.
        # 2. El juego no ha terminado por mutuo acuerdo.
        return self.__playing__ and self.__has_pieces__()

    def move(self, from_row, from_col, to_row, to_col):
        # Verifica si el juego sigue en curso
        if not self.is_playing():
            raise InvalidMove("El juego ha terminado.")

        # Obtiene la pieza en la posición de origen
        piece = self.__board__.get_piece(from_row, from_col)

        # Verifica si la posición está vacía
        if piece is None:
            raise EmptyPosition(f"No hay ninguna pieza en la posición ({from_row}, {from_col}).")
        
        # Verifica si es el turno de la pieza seleccionada
        if piece.get_color() != self.__turn__:
            raise InvalidTurn(f"Es el turno de {self.__turn__}, no puedes mover una pieza {piece.get_color()}.")

        # Valida el movimiento
        if not self.__validate_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMove(f"Movimiento inválido para la pieza {piece}.")

        # Mueve la pieza en el tablero
        self.__board__.move(from_row, from_col, to_row, to_col)

        # Cambia el turno al otro jugador
        self.change_turn()

        # Revisa si el juego ha terminado
        if not self.__has_pieces__():
            self.end_game()

    def __validate_move(self, piece, from_row, from_col, to_row, to_col):
    # Valida el movimiento dependiendo del tipo de pieza
        if isinstance(piece, Rook):  # Torre
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        elif isinstance(piece, Bishop):  # Alfil
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        elif isinstance(piece, Knight):  # Caballo
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        elif isinstance(piece, Queen):  # Reina
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        elif isinstance(piece, King):  # Rey
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        elif isinstance(piece, Pawn):  # Peón
            return piece.valid_positions(from_row, from_col, to_row, to_col)
    
    # Si la pieza no está reconocida o no tiene movimiento válido, devuelve False
        return False


    def __has_pieces__(self):
        # Verifica si ambos jugadores aún tienen piezas en el tablero
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        # El juego finaliza si alguno de los jugadores no tiene piezas
        return white_pieces and black_pieces

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        # Retorna una representación visual del tablero
        return str(self.__board__)

    def change_turn(self):
        # Cambia el turno entre blanco y negro
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def end_game(self):
        # Finaliza el juego por acuerdo mutuo o porque un jugador se quedó sin piezas
        self.__playing__ = False
        print("El juego ha terminado.")

    'def propose_draw(self):
        # Permite que los jugadores terminen el juego de mutuo acuerdo
        decision = input("¿Ambos jugadores desean terminar el juego? (sí/no): ")
        if decision.lower() == "sí":
            self.end_game()

    def propose_draw(self):
        # Permite que los jugadores terminen el juego de mutuo acuerdo
        decision = input("¿Ambos jugadores desean terminar el juego? (sí/no): ")
        if decision.lower() == "sí":
            self.end_game()
        else:
            print("El juego continúa.")

    def play(self):
        while self.__playing__:
            print(self.show_board())
            print(f"Turno de las piezas {'blancas' if self.__turn__ == 'WHITE' else 'negras'}.")

            # Opción para proponer un empate
            if input("¿Desea proponer un empate? (sí/no): ").lower() == "sí":
                self.propose_draw()
                if not self.__playing__:  # Si el juego terminó, salir del bucle
                    break

            move = input("Ingresa tu movimiento: ")
            # Aquí iría la lógica para validar y ejecutar el movimiento

            # Cambiar turno
            self.change_turn()'''

class Chess:
    def __init__(self):
        # Inicializa el tablero
        self.__board__ = Board()
        # El turno comienza con las piezas blancas
        self.__turn__ = "WHITE"
        # Indica si el juego está activo
        self.__playing__ = True

    def start_game(self):
        self.play()

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
        # Validación del movimiento según el tipo de pieza
        return piece.valid_positions(from_row, from_col, to_row, to_col)

    def __has_pieces__(self):
        white_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "WHITE"
        )
        black_pieces = any(
            piece for row in self.__board__.__positions__ for piece in row if piece and piece.get_color() == "BLACK"
        )
        return white_pieces and black_pieces

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def end_game(self):
        self.__playing__ = False
        print("El juego ha terminado.")

    def propose_draw(self):
        print("Proponiendo un empate...")  # Mensaje de depuración
    # Permite que los jugadores terminen el juego de mutuo acuerdo
        decision = input("¿Ambos jugadores desean terminar el juego? (sí/no): ")
        if decision.lower() == "sí":
            self.end_game()
        else:
            print("El juego continúa.")

    def play(self):
        while self.__playing__:
            print(self.show_board())
            print(f"Turno de las piezas {'blancas' if self.__turn__ == 'WHITE' else 'negras'}.")

        # Opción para proponer un empate
            decision = input("¿Desea proponer un empate? (sí/no): ").lower()
            if decision == "sí":
                self.propose_draw()
                if not self.__playing__:  # Si el juego terminó, salir del bucle
                    break

        # Aquí pides el movimiento después de la propuesta de empate
            move = input("Ingresa tu movimiento (ejemplo: 1 2 3 4): ")
        # Aquí iría la lógica para validar y ejecutar el movimiento

        # Cambiar turno
            self.change_turn()

def play(chess_game):
    try:
        chess_game.play()  # Llama al método play de la instancia de ChessGame
    except Exception as e:
        print(f"Ocurrió un error: {e}")

            
















