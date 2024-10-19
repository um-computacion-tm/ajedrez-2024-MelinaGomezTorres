import unittest
from chess.piece import Piece

class TestPiece(unittest.TestCase):

    def setUp(self):
        # Creamos un objeto "Board" de prueba (puede ser un mock o un objeto sencillo)
        self.mock_board = MockBoard()

        # Creamos una pieza blanca
        self.white_piece = Piece("WHITE", self.mock_board)

        # Creamos una pieza negra
        self.black_piece = Piece("BLACK", self.mock_board)

    def test_str_representation(self):
        # Verificamos la representación visual de las piezas
        self.assertEqual(str(self.white_piece), "", "La representación de la pieza blanca debería ser un símbolo")
        self.assertEqual(str(self.black_piece), "", "La representación de la pieza negra debería ser un símbolo")

    def test_get_color(self):
        # Verificamos que la función get_color retorne el color correcto
        self.assertEqual(self.white_piece.get_color(), "WHITE")
        self.assertEqual(self.black_piece.get_color(), "BLACK")

    def test_valid_positions(self):
        # Verificamos que el método valid_positions funcione correctamente
        self.mock_board.set_piece_at(3, 3, self.white_piece)  # Ubicamos la pieza blanca en 3, 3

        possible_positions = [(2, 2), (4, 4)]  # Posiciones posibles, por ejemplo, diagonales
        self.white_piece.get_possible_positions = lambda r, c: possible_positions

        # Verificamos si un movimiento propuesto es válido
        self.assertTrue(self.white_piece.__valid_positions__(3, 3, 2, 2))
        self.assertFalse(self.white_piece.__valid_positions__(3, 3, 5, 5))

    def test_possible_positions_in_direction(self):
    # Verificamos que las posiciones posibles en una dirección se calculen correctamente
        self.mock_board.set_piece_at(3, 3, self.white_piece)  # Ubicamos la pieza en el tablero

    # Colocamos una pieza que bloquee en (6, 6)
        blocking_piece = Piece("BLACK", self.mock_board)
        self.mock_board.set_piece_at(6, 6, blocking_piece)  # La pieza negra bloquea el movimiento

        possible_positions = self.white_piece.possible_positions_in_direction(3, 3, 1, 1)
    
    # Las posiciones deberían detenerse en (5, 5) porque hay una pieza enemiga en (6, 6)
        expected_positions = [(4, 4), (5, 5), (6, 6)]  # Puede capturar en (6, 6), pero no avanzar más allá
        self.assertEqual(possible_positions, expected_positions)



# Clase auxiliar para simular el tablero
class MockBoard:
    def __init__(self):
        # Simula un tablero vacío
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def set_piece_at(self, row, col, piece):
        self.board[row][col] = piece

    def get_piece(self, row, col):
        return self.board[row][col]


if __name__ == '__main__':
    unittest.main()
