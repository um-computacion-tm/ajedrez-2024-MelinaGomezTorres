import unittest
from chess.piezas.rook import Rook
from chess.board import Board

class TestRook(unittest.TestCase):
    """Clase de prueba para la pieza Torre en el juego de ajedrez."""

#Verifica que el símbolo de la torre sea el correcto
    def test_str(self):
        """
        Verifica que el símbolo de la torre blanca y negra sea correcto.

        :return: None
        """
        rook_white = Rook("WHITE", None)
        self.assertEqual(str(rook_white), "♜")  # Símbolo para la torre blanca  
        rook_black = Rook("BLACK")
        self.assertEqual(str(rook_black), "♖")  # Símbolo para la torre negra

    def setUp(self):
        """
        Configura el entorno de prueba antes de cada método de prueba.

        Crea un tablero vacío y una torre blanca, colocándola en la posición (7, 0).
        :return: None
        """
        self.board = Board(for_test=True)  # Crea una instancia del tablero para pruebas.
        self.rook_white = Rook("WHITE", self.board) # Crea una torre blanca.
        self.board.set_piece(7, 0, self.rook_white) # Coloca la torre blanca en la posición (7, 0).
        self.clear_positions(6, 0, 5, 0) # Limpia las posiciones (6, 0) y (5, 0).

    def clear_positions(self, *positions):
        """
        Limpia las posiciones especificadas en el tablero.

        :param positions: Tuplas de coordenadas a limpiar en el tablero.
        :return: None
        """
        for pos in positions:
            self.board.set_piece(pos, 0, None) # Establece cada posición como None.

    def test_rook_valid_moves(self):
        """
        Verifica los movimientos válidos de la torre.

        Comprueba que la torre pueda moverse a posiciones válidas y que no
        pueda moverse sobre piezas aliadas.

        :return: None
        """
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Movimiento hacia arriba.
        self.board.set_piece(5, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (5, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))  # No puede moverse sobre una aliada.
        self.board.set_piece(6, 0, Rook("BLACK", self.board))   # Coloca una torre negra en (6, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 6, 0))   # Puede capturar la negra.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 8, 0))  # Fuera de límites.

    def test_rook_cannot_jump_over_ally(self):
        """
        Verifica que la torre no puede saltar sobre piezas aliadas.

        Coloca una pieza aliada en la trayectoria de la torre y asegura que no
        pueda moverse a esa posición.

        :return: None
        """
        self.board.set_piece(6, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (6, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))   # No puede moverse a (5, 0).

    def test_rook_can_capture_enemy(self):
        """
        Verifica que la torre puede capturar piezas enemigas.

        Coloca una pieza enemiga en la trayectoria de la torre y asegura que pueda
        capturarla.

        :return: None
        """
        self.board.set_piece(5, 0, Rook("BLACK", self.board))  # Coloca una torre negra en (5, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Puede capturar.

    def test_rook_cannot_move_diagonally(self):
        """
        Verifica que la torre no puede moverse en diagonal.

        Asegura que cualquier intento de movimiento diagonal falle.

        :return: None
        """
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 6, 1))  # Movimiento diagonal inválido.

    def test_rook_moves_until_obstacle(self):
        """
        Verifica que la torre se detiene al encontrar un obstáculo.

        Asegura que la torre no pueda moverse más allá de una pieza en su trayectoria.

        :return: None
        """
        for i in range(6, 0, -1):
            self.board.set_piece(i, 0, None) # Limpia las posiciones en la columna.
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 0, 0))   # Puede moverse a (0, 0).
        self.board.set_piece(3, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (3, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 0, 0))  # No puede moverse a (0, 0) por obstáculo.

    def test_rook_move_out_of_bounds(self):
        """
        Verifica movimientos fuera del tablero (fila y columna).

        Asegura que cualquier intento de movimiento que esté fuera de los límites del tablero falle.

        :return: None
        """
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 9, 0))  # Fuera de límites en fila.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 7, -1))  # Fuera de límites en columna.


if __name__ == '__main__':
    unittest.main()  