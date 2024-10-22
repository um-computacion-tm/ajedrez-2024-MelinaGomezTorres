import unittest
from chess.piezas.knight import Knight
from chess.board import Board

class TestKnight(unittest.TestCase):
    """Clase de prueba para la pieza Caballo en ajedrez."""

    def setUp(self):
        """
        Configura el entorno de pruebas antes de cada método de prueba.

        Inicializa un tablero para pruebas y coloca los caballos blanco y negro en sus posiciones.

        :return: None
        """
        self.board = Board(for_test=True) 
        self.knight_white = Knight("white", self.board) # Caballo blanco
        self.knight_black = Knight("black", self.board) # Caballo negro

    def test_knight_symbol(self):
        """
        Verifica que el símbolo del caballo sea correcto según su color.

        Compara el símbolo de cada caballo con el valor esperado.

        :return: None
        """
        self.assertEqual(str(self.knight_white), "♞", "El símbolo del caballo blanco debería ser ♞")
        self.assertEqual(str(self.knight_black), "♘", "El símbolo del caballo negro debería ser ♘")

    def test_knight_possible_positions(self):
        """
        Verifica las posiciones posibles que el caballo puede alcanzar desde una posición dada.

        Coloca el caballo en una posición inicial y obtiene sus posiciones posibles.

        :return: None
        """
        self.board.set_piece(4, 4, self.knight_white)
        positions = self.knight_white.get_possible_positions(4, 4)
        expected_positions = [
            (6, 5), (6, 3), (2, 5), (2, 3), 
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        self.assertCountEqual(positions, expected_positions, "Las posiciones posibles no coinciden")

    def test_knight_captures(self):
        """
        Verifica que el caballo pueda capturar piezas enemigas.

        Coloca una pieza enemiga en una posición que el caballo pueda capturar y comprueba la validez.

        :return: None
        """
        self.board.set_piece(4, 4, self.knight_white)
        self.board.set_piece(6, 5, Knight("black", self.board))  # Coloca un caballo negro en (6, 5)
        
        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertIn((6, 5), positions, "El caballo debería poder capturar la pieza en (6, 5)")

    def test_knight_invalid_moves(self):
        """
        Verifica los movimientos del caballo cuando está en el borde del tablero.

        Coloca el caballo en el borde del tablero y comprueba que no tenga movimientos válidos fuera de los límites.

        :return: None
        """
        self.board.set_piece(0, 0, self.knight_white)

        positions = self.knight_white.get_possible_positions(0, 0)
        expected_positions = [(2, 1), (1, 2)]  # Movimientos válidos desde (0, 0)
        self.assertCountEqual(positions, expected_positions, "Las posiciones posibles no coinciden en el borde")

    def test_knight_cannot_capture_own_piece(self):
        """
        Verifica que el caballo no pueda capturar sus propias piezas.

        Coloca una pieza blanca en una posición de captura y asegura que el caballo no pueda capturarla.

        :return: None
        """
        self.board.set_piece(4, 4, self.knight_white)
        self.board.set_piece(6, 5, Knight("white", self.board))  # Caballo blanco en (6, 5)

        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertNotIn((6, 5), positions, "El caballo no debería poder capturar su propia pieza en (6, 5)")

    def test_knight_moves_at_board_edges(self):
        """
        Verifica los movimientos del caballo cuando está en la esquina superior izquierda.

        Coloca el caballo en la esquina y comprueba que tenga los movimientos correctos desde allí.

        :return: None
        """

        self.board.set_piece(0, 0, self.knight_white)
        expected_positions = [(2, 1), (1, 2)]  # Movimientos válidos desde la esquina
        positions = self.knight_white.get_possible_positions(0, 0)
        self.assertCountEqual(positions, expected_positions, "El caballo debería tener movimientos correctos en el borde del tablero")

    def test_knight_moves_at_board_edges_lower_right(self):
        """
        Verifica los movimientos del caballo cuando está en la esquina inferior derecha.

        Coloca el caballo en la esquina y comprueba que tenga los movimientos correctos desde allí.

        :return: None
        """
        self.board.set_piece(7, 7, self.knight_white)
        expected_positions = [(5, 6), (6, 5)]  # Movimientos válidos desde la esquina
        positions = self.knight_white.get_possible_positions(7, 7)
        self.assertCountEqual(positions, expected_positions, "El caballo debería tener movimientos correctos en la esquina inferior derecha")

    def test_knight_cannot_move_out_of_bounds(self):
        """
        Verifica que el caballo no pueda moverse fuera de los límites del tablero.

        Coloca el caballo en una esquina y asegura que no haya movimientos inválidos que excedan el tablero.

        :return: None
        """
        self.board.set_piece(0, 0, self.knight_white)
        invalid_positions = [(-1, -2), (-2, -1)]  # Movimientos fuera del tablero
        positions = self.knight_white.get_possible_positions(0, 0)
        for pos in invalid_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, positions, "El caballo no debería moverse fuera del tablero")

    def test_knight_cannot_move_onto_self(self):
        """
        Verifica que el caballo no pueda moverse a su propia posición.

        Coloca el caballo en una posición y asegura que no pueda moverse a la misma.

        :return: None
        """
        self.board.set_piece(4, 4, self.knight_white)
        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertNotIn((4, 4), positions, "El caballo no debería moverse a su propia posición")


if __name__ == '__main__':
    unittest.main()
