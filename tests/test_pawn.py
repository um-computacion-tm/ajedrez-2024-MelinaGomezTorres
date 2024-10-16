import unittest
from chess.board import Board
from chess.piezas.pawn import Pawn
from chess.exceptions import OutOfBoard

class TestPawn(unittest.TestCase):

    def setUp(self):
        # Crea un tablero para pruebas sin configurar las piezas automáticamente
        self.board = Board(for_test=True)
        self.pawn_white = Pawn("WHITE", self.board)
        self.pawn_black = Pawn("BLACK", self.board)
        # Coloca el peón blanco en la posición inicial
        self.board.set_piece(6, 4, self.pawn_white)  # Peón blanco en la fila 6, columna 4
        # Coloca el peón negro en la posición inicial
        self.board.set_piece(1, 4, self.pawn_black)  # Peón negro en la fila 1, columna 4

    def test_pawn_initial_double_move(self):
        # Verifica que el peón blanco pueda moverse dos casillas hacia adelante
        self.assertTrue(self.pawn_white.valid_positions(6, 4, 4, 4), "El peón blanco debería poder moverse dos casillas en su primer turno")
        # Verifica que el peón negro pueda moverse dos casillas hacia adelante
        self.assertTrue(self.pawn_black.valid_positions(1, 4, 3, 4), "El peón negro debería poder moverse dos casillas en su primer turno")

    def test_pawn_single_move(self):
        # Después del primer movimiento, el peón solo debería poder avanzar una casilla
        self.board.move(6, 4, 4, 4)  # Mueve el peón blanco dos casillas
        self.assertTrue(self.pawn_white.valid_positions(4, 4, 3, 4), "El peón blanco debería poder moverse solo una casilla después de su primer movimiento")

    def test_pawn_illegal_move_backwards(self):
        # Los peones no pueden moverse hacia atrás
        self.board.move(6, 4, 5, 4)  # Mueve el peón blanco una casilla hacia adelante
        self.assertFalse(self.pawn_white.valid_positions(5, 4, 6, 4), "El peón blanco no debería poder moverse hacia atrás")

    def test_pawn_capture_diagonally(self):
        # Coloca una pieza enemiga para capturar diagonalmente
        enemy_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 5, enemy_pawn)  # Peón negro en posición diagonal del peón blanco
        self.assertTrue(self.pawn_white.valid_positions(6, 4, 5, 5), "El peón blanco debería poder capturar diagonalmente una pieza enemiga")

    def test_pawn_illegal_capture_forward(self):
        # Verifica que el peón no pueda capturar hacia adelante
        enemy_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 4, enemy_pawn)  # Peón negro directamente en frente del peón blanco
        self.assertFalse(self.pawn_white.valid_positions(6, 4, 5, 4), "El peón blanco no debería poder capturar una pieza directamente enfrente")

    def test_pawn_out_of_board(self):
        # Verifica que mover fuera del tablero arroje una excepción
        with self.assertRaises(OutOfBoard):
            self.board.get_piece(-1, 0)

if __name__ == "__main__":
    unittest.main()
