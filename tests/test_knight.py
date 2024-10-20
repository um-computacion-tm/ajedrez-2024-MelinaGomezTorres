import unittest
from chess.piezas.knight import Knight
from chess.board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  # Crea un tablero sin piezas iniciales
        self.knight_white = Knight("white", self.board) # Caballo blanco
        self.knight_black = Knight("black", self.board) # Caballo negro

    def test_knight_symbol(self):
        # Verifica que el símbolo sea correcto según el color
        self.assertEqual(str(self.knight_white), "♞", "El símbolo del caballo blanco debería ser ♞")
        self.assertEqual(str(self.knight_black), "♘", "El símbolo del caballo negro debería ser ♘")

    def test_knight_possible_positions(self):
        # Coloca el caballo en una posición inicial
        self.board.set_piece(4, 4, self.knight_white)
        # Obtiene las posiciones posibles que puede alcanzar el caballo
        # Verifica esas posiciones
        positions = self.knight_white.get_possible_positions(4, 4)
        expected_positions = [
            (6, 5), (6, 3), (2, 5), (2, 3), 
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        self.assertCountEqual(positions, expected_positions, "Las posiciones posibles no coinciden")

    def test_knight_captures(self):
        # Coloca el caballo en el centro del tablero
        self.board.set_piece(4, 4, self.knight_white)

        # Coloca una pieza opuesta en una posición que el caballo pueda capturar
        self.board.set_piece(6, 5, Knight("black", self.board))  # Coloca un caballo negro en (6, 5)
        
        # Verifica que el caballo blanco pueda capturar el caballo negro
        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertIn((6, 5), positions, "El caballo debería poder capturar la pieza en (6, 5)")

    def test_knight_invalid_moves(self):
        # Coloca el caballo blanco en el borde del tablero
        self.board.set_piece(0, 0, self.knight_white)

        # Verifica que no haya movimientos válidos fuera del tablero
        positions = self.knight_white.get_possible_positions(0, 0)
        expected_positions = [(2, 1), (1, 2)]  # Movimientos válidos desde (0, 0)
        self.assertCountEqual(positions, expected_positions, "Las posiciones posibles no coinciden en el borde")

    def test_knight_cannot_capture_own_piece(self):
        # Coloca el caballo blanco y una pieza blanca en posición de captura
        self.board.set_piece(4, 4, self.knight_white)
        self.board.set_piece(6, 5, Knight("white", self.board))  # Caballo blanco en (6, 5)

        # Verifica que el caballo no pueda capturar su propia pieza
        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertNotIn((6, 5), positions, "El caballo no debería poder capturar su propia pieza en (6, 5)")

    def test_knight_moves_at_board_edges(self):
        # Coloca el caballo en la esquina superior izquierda
        self.board.set_piece(0, 0, self.knight_white)
        expected_positions = [(2, 1), (1, 2)]  # Movimientos válidos desde la esquina
        positions = self.knight_white.get_possible_positions(0, 0)
        self.assertCountEqual(positions, expected_positions, "El caballo debería tener movimientos correctos en el borde del tablero")

    def test_knight_moves_at_board_edges_lower_right(self):
        # Coloca el caballo en la esquina inferior derecha
        self.board.set_piece(7, 7, self.knight_white)
        expected_positions = [(5, 6), (6, 5)]  # Movimientos válidos desde la esquina
        positions = self.knight_white.get_possible_positions(7, 7)
        self.assertCountEqual(positions, expected_positions, "El caballo debería tener movimientos correctos en la esquina inferior derecha")

    def test_knight_cannot_move_out_of_bounds(self):
        # Coloca el caballo en una esquina y verifica que no haya movimientos fuera de los límites
        self.board.set_piece(0, 0, self.knight_white)
        invalid_positions = [(-1, -2), (-2, -1)]  # Movimientos fuera del tablero
        positions = self.knight_white.get_possible_positions(0, 0)
        for pos in invalid_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, positions, "El caballo no debería moverse fuera del tablero")

    def test_knight_cannot_move_onto_self(self):
        # Verifica que el caballo no pueda moverse a su propia posición
        self.board.set_piece(4, 4, self.knight_white)
        positions = self.knight_white.get_possible_positions(4, 4)
        self.assertNotIn((4, 4), positions, "El caballo no debería moverse a su propia posición")


if __name__ == '__main__':
    unittest.main()
