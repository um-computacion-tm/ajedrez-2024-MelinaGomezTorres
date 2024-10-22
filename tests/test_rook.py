import unittest
from chess.piezas.rook import Rook
from chess.board import Board

class TestRook(unittest.TestCase):

#Verifica que el símbolo de la torre sea el correcto
    def test_str(self):
        rook_white = Rook("WHITE", None)
        self.assertEqual(str(rook_white), "♜")  # Símbolo para la torre blanca  
        rook_black = Rook("BLACK")
        self.assertEqual(str(rook_black), "♖")  # Símbolo para la torre negra

    def setUp(self):
#Configura el tablero y la torre blanca
        self.board = Board(for_test=True)  # Crea una instancia del tablero para pruebas.
        self.rook_white = Rook("WHITE", self.board) # Crea una torre blanca.
        self.board.set_piece(7, 0, self.rook_white) # Coloca la torre blanca en la posición (7, 0).
        self.clear_positions(6, 0, 5, 0) # Limpia las posiciones (6, 0) y (5, 0).

    def clear_positions(self, *positions):
#Limpia las posiciones del tablero estableciéndolas como vacías.
        for pos in positions:
            self.board.set_piece(pos, 0, None) # Establece cada posición como None.

    def test_rook_valid_moves(self):
#Verifica los movimientos válidos de la torre
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Movimiento hacia arriba.
        self.board.set_piece(5, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (5, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))  # No puede moverse sobre una aliada.
        self.board.set_piece(6, 0, Rook("BLACK", self.board))   # Coloca una torre negra en (6, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 6, 0))   # Puede capturar la negra.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 8, 0))  # Fuera de límites.

    def test_rook_cannot_jump_over_ally(self):
#Verifica que la torre no puede saltar sobre piezas aliadas
        self.board.set_piece(6, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (6, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))   # No puede moverse a (5, 0).

    def test_rook_can_capture_enemy(self):
#Verifica que la torre puede capturar piezas enemigas
        self.board.set_piece(5, 0, Rook("BLACK", self.board))  # Coloca una torre negra en (5, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Puede capturar.

    def test_rook_cannot_move_diagonally(self):
#Verifica que la torre no puede moverse en diagonal
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 6, 1))  # Movimiento diagonal inválido.

    def test_rook_moves_until_obstacle(self):
#Verifica que la torre se detiene al encontrar un obstáculo
        for i in range(6, 0, -1):
            self.board.set_piece(i, 0, None) # Limpia las posiciones en la columna.
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 0, 0))   # Puede moverse a (0, 0).
        self.board.set_piece(3, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (3, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 0, 0))  # No puede moverse a (0, 0) por obstáculo.

    def test_rook_move_out_of_bounds(self):
#Verifica movimientos fuera del tablero (fila y columna)
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 9, 0))  # Fuera de límites en fila.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 7, -1))  # Fuera de límites en columna.


if __name__ == '__main__':
    unittest.main()  