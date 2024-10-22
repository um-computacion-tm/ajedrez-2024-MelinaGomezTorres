import unittest
from chess.piezas.queen import Queen
from chess.board import Board

class TestQueen(unittest.TestCase):
    """Clase de prueba para la pieza Reina en el juego de ajedrez."""

    def test_str(self):
        """
        Verifica que el símbolo de la reina blanca y negra sea correcto.

        :return: None
        """
        self.assertEqual(str(self.queen_white), "♛")  # Símbolo para la reina blanca
        queen_black = Queen("BLACK", self.board) # Crea una reina negra.
        self.assertEqual(str(queen_black), "♕")  # Símbolo para la reina negra

    def setUp(self):
        """
        Configura el entorno de prueba antes de cada método de prueba.

        Crea un tablero vacío y una reina blanca, colocándola en la posición (4, 4).
        :return: None
        """
        self.board = Board(for_test=True)  
        self.queen_white = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, self.queen_white)

    def test_possible_orthogonal_positions(self):
        """
        Verifica los movimientos ortogonales válidos de la reina.

        Limpia posiciones específicas y asegura que la reina pueda moverse
        a las posiciones ortogonales esperadas.

        :return: None
        """
        self.clear_positions((4, 5), (4, 3), (3, 4), (5, 4))
        for pos in [(5, 4), (3, 4), (4, 5), (4, 3)]:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.queen_white.possible_orthogonal_positions(4, 4))

    def test_possible_diagonal_positions(self):
        """
        Verifica los movimientos diagonales válidos de la reina.

        Limpia posiciones específicas y asegura que la reina pueda moverse
        a las posiciones diagonales esperadas.

        :return: None
        """
        self.clear_positions((3, 3), (3, 5), (5, 3), (5, 5))
        for pos in [(3, 3), (3, 5), (5, 3), (5, 5)]:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.queen_white.possible_diagonal_positions(4, 4))

    def test_queen_can_capture_enemy(self):
        """
        Verifica que la reina puede capturar piezas enemigas.

        Coloca piezas enemigas en posiciones diagonales y ortogonales y asegura
        que la reina pueda capturarlas.

        :return: None
        """
        self.board.set_piece(5, 5, Queen("BLACK", self.board))  # Pieza enemiga
        self.assertIn((5, 5), self.queen_white.possible_diagonal_positions(4, 4))
        self.board.set_piece(5, 4, Queen("BLACK", self.board))  # Pieza enemiga
        self.assertIn((5, 4), self.queen_white.possible_orthogonal_positions(4, 4))
    
    def test_valid_positions(self):
        """
        Verifica que los movimientos de la reina sean válidos.

        Limpia posiciones antes de verificar los movimientos válidos
        de la reina en diferentes direcciones.

        :return: None
        """
        self.clear_positions((4, 5), (4, 3), (3, 4), (5, 4))
    
    # Verifica que el movimiento de (4, 4) a (5, 4) sea válido
        self.assertTrue(self.queen_white.__valid_positions__(4, 4, 5, 4))  # Abajo
    # Verifica que el movimiento de (4, 4) a (3, 4) sea válido
        self.assertTrue(self.queen_white.__valid_positions__(4, 4, 3, 4)) # Arriba
    # Verifica que el movimiento de (4, 4) a (4, 5) sea válido
        self.assertTrue(self.queen_white.__valid_positions__(4, 4, 4, 5)) # Derecha

    def clear_positions(self, *positions):
        """
        Limpia las posiciones especificadas en el tablero.

        :param positions: Tuplas de coordenadas a limpiar en el tablero.
        :return: None
        """
        for row, col in positions:
            self.board.set_piece(row, col, None)

if __name__ == '__main__':
    unittest.main()









