import unittest
from chess.piezas.queen import Queen
from chess.board import Board

class TestQueen(unittest.TestCase):

    def test_str(self):
    #Verifica que el símbolo de la reina sea el correcto
        self.assertEqual(str(self.queen_white), "♛")  # Símbolo para la reina blanca
        queen_black = Queen("BLACK", self.board)
        self.assertEqual(str(queen_black), "♕")  # Símbolo para la reina negra

    def setUp(self):
    #Configura el tablero y la reina blanca
        self.board = Board(for_test=True)  
        self.queen_white = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, self.queen_white)

    def test_possible_orthogonal_positions(self):
    #Verifica los movimientos ortogonales válidos
        self.clear_positions((4, 5), (4, 3), (3, 4), (5, 4))
        # Verifica todos los movimientos ortogonales
        for pos in [(5, 4), (3, 4), (4, 5), (4, 3)]:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.queen_white.possible_orthogonal_positions(4, 4))

    def test_possible_diagonal_positions(self):
    #Verifica los movimientos diagonales válidos
        self.clear_positions((3, 3), (3, 5), (5, 3), (5, 5))
        # Verifica todos los movimientos diagonales
        for pos in [(3, 3), (3, 5), (5, 3), (5, 5)]:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.queen_white.possible_diagonal_positions(4, 4))

    def test_queen_can_capture_enemy(self):
    #Verifica que la reina puede capturar piezas enemigas
        self.board.set_piece(5, 5, Queen("BLACK", self.board))  # Pieza enemiga
        self.assertIn((5, 5), self.queen_white.possible_diagonal_positions(4, 4))
        self.board.set_piece(5, 4, Queen("BLACK", self.board))  # Pieza enemiga
        self.assertIn((5, 4), self.queen_white.possible_orthogonal_positions(4, 4))
    
    def test_valid_positions(self):
        self.clear_positions((4, 5), (4, 3), (3, 4), (5, 4))
    
    # Verifica que el movimiento de (4, 4) a (5, 4) sea válido
        self.assertTrue(self.queen_white.valid_positions(4, 4, 5, 4))
    # Verifica que el movimiento de (4, 4) a (3, 4) sea válido
        self.assertTrue(self.queen_white.valid_positions(4, 4, 3, 4))
    # Verifica que el movimiento de (4, 4) a (4, 5) sea válido
        self.assertTrue(self.queen_white.valid_positions(4, 4, 4, 5))

    def clear_positions(self, *positions):
    #Limpia las posiciones del tablero
        for row, col in positions:
            self.board.set_piece(row, col, None)

if __name__ == '__main__':
    unittest.main()









