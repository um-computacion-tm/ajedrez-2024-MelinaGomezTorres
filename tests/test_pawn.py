import unittest
from chess.board import Board
from chess.piezas.pawn import Pawn
from chess.exceptions import OutOfBoard

class TestPawn(unittest.TestCase):
    """Clase de prueba para la pieza peón en ajedrez."""

    def setUp(self):
        """
        Configura el entorno de pruebas antes de cada método de prueba.

        Inicializa un tablero para pruebas y coloca peones blanco y negro en sus posiciones iniciales.

        :return: None
        """
        self.board = Board(for_test=True)
        self.pawn_white = Pawn("WHITE", self.board)
        self.pawn_black = Pawn("BLACK", self.board)
        self.board.set_piece(6, 4, self.pawn_white)  # Peón blanco en la fila 6, columna 4
        self.board.set_piece(1, 4, self.pawn_black)  # Peón negro en la fila 1, columna 4

    def test_pawn_initial_double_move(self):
        """
        Verifica que los peones puedan realizar su movimiento inicial de dos casillas.

        Asegura que tanto el peón blanco como el negro puedan moverse dos casillas hacia adelante
        en su primer turno.

        :return: None
        """
        self.assertTrue(self.pawn_white.valid_positions(6, 4, 4, 4), "El peón blanco debería poder moverse dos casillas en su primer turno")
        self.assertTrue(self.pawn_black.valid_positions(1, 4, 3, 4), "El peón negro debería poder moverse dos casillas en su primer turno")

    def test_pawn_single_move(self):
        """
        Verifica que un peón solo pueda avanzar una casilla después de su primer movimiento.

        Mueve el peón blanco dos casillas y luego comprueba que solo pueda moverse una casilla hacia adelante.

        :return: None
        """
        self.board.move(6, 4, 4, 4)  
        self.assertTrue(self.pawn_white.valid_positions(4, 4, 3, 4), "El peón blanco debería poder moverse solo una casilla después de su primer movimiento")

    def test_pawn_illegal_move_backwards(self):
        """
        Verifica que los peones no puedan moverse hacia atrás.

        Mueve el peón blanco una casilla hacia adelante y luego intenta moverlo hacia atrás.

        :return: None
        """
        self.board.move(6, 4, 5, 4) 
        self.assertFalse(self.pawn_white.valid_positions(5, 4, 6, 4), "El peón blanco no debería poder moverse hacia atrás")

    def test_pawn_capture_diagonally(self):
        """
        Verifica que un peón pueda capturar piezas enemigas diagonalmente.

        Coloca una pieza enemiga en la posición diagonal del peón blanco y asegura que puede capturarla.

        :return: None
        """
        enemy_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 5, enemy_pawn)  # Peón negro en posición diagonal del peón blanco
        self.assertTrue(self.pawn_white.valid_positions(6, 4, 5, 5), "El peón blanco debería poder capturar diagonalmente una pieza enemiga")

    def test_pawn_illegal_capture_forward(self):
        """
        Verifica que un peón no pueda capturar piezas que se encuentren directamente enfrente.

        Coloca una pieza enemiga directamente enfrente del peón blanco y asegura que no puede capturarla.

        :return: None
        """
        enemy_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 4, enemy_pawn)  
        self.assertFalse(self.pawn_white.valid_positions(6, 4, 5, 4), "El peón blanco no debería poder capturar una pieza directamente enfrente")

    def test_pawn_out_of_board(self):
        """
        Verifica que mover fuera del tablero arroje una excepción.

        Intenta acceder a una posición fuera de los límites del tablero y asegura que se lanza una excepción.

        :return: None
        """
        with self.assertRaises(OutOfBoard):
            self.board.get_piece(-1, 0)

if __name__ == "__main__":
    unittest.main()
