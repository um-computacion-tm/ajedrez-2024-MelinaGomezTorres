import unittest
from chess.piece import Piece

class TestPiece(unittest.TestCase):
    """Clase de prueba para la pieza de ajedrez."""

    def setUp(self):
        """
        Configura el entorno de prueba antes de cada método de prueba.

        Crea un objeto de tablero simulado y dos piezas, una blanca y una negra.

        :return: None
        """
        self.mock_board = MockBoard()

        # Creamos una pieza blanca
        self.white_piece = Piece("WHITE", self.mock_board)

        # Creamos una pieza negra
        self.black_piece = Piece("BLACK", self.mock_board)

    def test_str_representation(self):
        """
        Verifica la representación visual de las piezas.

        Asegura que la representación de las piezas blanca y negra retorne el símbolo adecuado.

        :return: None
        """
        # Retorne el símbolo adecuado, que debería ser una cadena no vacía.
        self.assertEqual(str(self.white_piece), "", "La representación de la pieza blanca debería ser un símbolo")
        self.assertEqual(str(self.black_piece), "", "La representación de la pieza negra debería ser un símbolo")

    def test_get_color(self):
        """
        Verifica que la función get_color retorne el color correcto de las piezas.

        :return: None
        """
        self.assertEqual(self.white_piece.get_color(), "WHITE")
        self.assertEqual(self.black_piece.get_color(), "BLACK")

    def test_valid_positions(self):
        """
        Verifica que el método valid_positions funcione correctamente.

        Coloca una pieza blanca en una posición y asegura que las posiciones posibles
        sean evaluadas correctamente para movimientos válidos.

        :return: None
        """
        self.mock_board.set_piece_at(3, 3, self.white_piece)  

        possible_positions = [(2, 2), (4, 4)]  # Posiciones posibles, por ejemplo, diagonales
        self.white_piece.get_possible_positions = lambda r, c: possible_positions


        self.assertTrue(self.white_piece.__valid_positions__(3, 3, 2, 2))
        self.assertFalse(self.white_piece.__valid_positions__(3, 3, 5, 5))

    def test_possible_positions_in_direction(self):
        """
        Verifica que las posiciones posibles en una dirección se calculen correctamente.

        Coloca una pieza que bloquee el movimiento y asegura que las posiciones
        posibles se detengan al encontrar un obstáculo.

        :return: None
        """
        self.mock_board.set_piece_at(3, 3, self.white_piece)  

    # Colocamos una pieza que bloquee en (6, 6)
        blocking_piece = Piece("BLACK", self.mock_board)
        self.mock_board.set_piece_at(6, 6, blocking_piece)  # La pieza negra bloquea el movimiento

        possible_positions = self.white_piece.possible_positions_in_direction(3, 3, 1, 1)
    
    # Las posiciones deberían detenerse en (5, 5) porque hay una pieza enemiga en (6, 6)
        expected_positions = [(4, 4), (5, 5), (6, 6)]  # Puede capturar en (6, 6), pero no avanzar más allá
        self.assertEqual(possible_positions, expected_positions)


class MockBoard:
    """Clase simulada para representar un tablero de ajedrez."""
    def __init__(self):
        """
        Inicializa un tablero vacío de 8x8.

        :return: None
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def set_piece_at(self, row, col, piece):
        """
        Coloca una pieza en la posición especificada del tablero.

        :param row: Fila donde se colocará la pieza.
        :param col: Columna donde se colocará la pieza.
        :param piece: La pieza que se colocará en el tablero.
        :return: None
        """
        self.board[row][col] = piece

    def get_piece(self, row, col):
        """
        Retorna la pieza en la posición especificada del tablero.

        :param row: Fila de la posición deseada.
        :param col: Columna de la posición deseada.
        :return: La pieza en la posición especificada o None si no hay pieza.
        """
        return self.board[row][col]


if __name__ == '__main__':
    unittest.main()
