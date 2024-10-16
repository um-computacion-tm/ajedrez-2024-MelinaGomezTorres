import unittest
from chess.piezas.king import King
from chess.board import Board

class TestKing(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(self.king_white), "♚")  # Símbolo para el rey blanco
        king_black = King("BLACK", self.board)
        self.assertEqual(str(king_black), "♔")  # Símbolo para el rey negro

    def setUp(self):
        self.board = Board(for_test=True)  
        self.king_white = King("WHITE", self.board)
        self.board.set_piece(4, 4, self.king_white)

    def test_possible_king_moves(self):
        # Movimientos posibles del rey (un espacio en cualquier dirección)
        expected_positions = [
            (3, 3), (3, 4), (3, 5), 
            (4, 3),         (4, 5), 
            (5, 3), (5, 4), (5, 5)
        ]
        self.clear_positions(*expected_positions)
        for pos in expected_positions:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.king_white.possible_moves(4, 4))

    def test_king_cannot_move_to_occupied_by_ally(self):
        # Coloca piezas aliadas alrededor del rey
        ally_positions = [(3, 3), (4, 3), (5, 4)]
        for pos in ally_positions:
            self.board.set_piece(*pos, King("WHITE", self.board))  # Coloca piezas aliadas
        for pos in ally_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, self.king_white.possible_moves(4, 4))

    def test_king_can_capture_enemy(self):
        # Coloca una pieza enemiga en una posición a donde el rey puede moverse
        self.board.set_piece(3, 3, King("BLACK", self.board))  # Pieza enemiga
        self.assertIn((3, 3), self.king_white.possible_moves(4, 4))

    def test_king_moves_at_board_edges(self):
        # Rey en la esquina superior izquierda
        self.board.set_piece(0, 0, self.king_white)
        expected_positions = [(0, 1), (1, 0), (1, 1)]  # Movimientos válidos en la esquina
        self.clear_positions(*expected_positions)
        self.assertEqual(self.king_white.possible_moves(0, 0), expected_positions)

        # Rey en la esquina inferior derecha
        self.board.set_piece(7, 7, self.king_white)
        expected_positions = [(6, 6), (6, 7), (7, 6)]  # Movimientos válidos en la esquina
        self.clear_positions(*expected_positions)
        self.assertEqual(self.king_white.possible_moves(7, 7), expected_positions)
    
    def test_king_cannot_move_out_of_bounds(self):
        # Movimientos fuera de los límites del tablero
        self.board.set_piece(0, 0, self.king_white)
        invalid_positions = [(-1, 0), (0, -1), (-1, -1)]  # Fuera de los límites
        for pos in invalid_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, self.king_white.possible_moves(0, 0))

    def test_king_cannot_move_onto_self(self):
        # El rey no puede moverse a su propia posición
        self.assertNotIn((4, 4), self.king_white.possible_moves(4, 4))

    def clear_positions(self, *positions):
        for row, col in positions:
            self.board.set_piece(row, col, None)

if __name__ == '__main__':
    unittest.main()