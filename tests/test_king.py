import unittest
from chess.piezas.king import King
from chess.board import Board

class TestKing(unittest.TestCase):
    """Clase de prueba para la pieza Rey en el juego de ajedrez."""

    def test_str(self):
        """
        Verifica que el símbolo del rey blanco y negro sea correcto.

        :return: None
        """
        self.assertEqual(str(self.king_white), "♚")  # Símbolo para el rey blanco
        king_black = King("BLACK", self.board) # Crea un rey negro
        self.assertEqual(str(king_black), "♔")  # Símbolo para el rey negro

    def setUp(self):
        """
        Configura el entorno de prueba antes de cada método de prueba.

        Crea un tablero vacío y un rey blanco, colocándolo en el centro del tablero.
        :return: None
        """
        self.board = Board(for_test=True)  
        self.king_white = King("WHITE", self.board) # Rey blanco
        self.board.set_piece(4, 4, self.king_white) # Coloca el rey blanco en el centro del tablero

    def test_possible_king_moves(self):
        """
        Verifica los movimientos posibles del rey.

        Comprueba que el rey pueda moverse a todas las posiciones válidas 
        desde su posición actual (4, 4).

        :return: None
        """
        expected_positions = [
            (3, 3), (3, 4), (3, 5), 
            (4, 3),         (4, 5), 
            (5, 3), (5, 4), (5, 5)
        ]
        self.clear_positions(*expected_positions) # Limpia las posiciones esperadas
        for pos in expected_positions:
            with self.subTest(pos=pos):
                self.assertIn(pos, self.king_white.get_possible_positions(4, 4))

    def test_king_cannot_move_to_occupied_by_ally(self):
        """
        Verifica que el rey no pueda moverse a posiciones ocupadas por aliadas.

        Coloca piezas aliadas alrededor del rey y asegura que no pueda moverse
        a esas posiciones.

        :return: None
        """
        ally_positions = [(3, 3), (4, 3), (5, 4)]
        for pos in ally_positions:
            self.board.set_piece(*pos, King("WHITE", self.board)) 
        for pos in ally_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, self.king_white.get_possible_positions(4, 4))

    def test_king_can_capture_enemy(self):
        """
        Verifica que el rey pueda capturar piezas enemigas.

        Coloca una pieza enemiga en una posición adyacente y asegura que el rey
        pueda capturarla.

        :return: None
        """
        self.board.set_piece(3, 3, King("BLACK", self.board))  # Pieza enemiga
        self.assertIn((3, 3), self.king_white.get_possible_positions(4, 4))

    def test_king_moves_at_board_edges(self):
        """
        Verifica los movimientos del rey cuando está en los bordes del tablero.

        Asegura que el rey se mueva correctamente cuando está en las esquinas del tablero.

        :return: None
        """
        self.board.set_piece(0, 0, self.king_white)
        expected_positions = [(0, 1), (1, 0), (1, 1)]  # Movimientos válidos en la esquina
        self.clear_positions(*expected_positions) # Limpia las posiciones esperadas
        self.assertEqual(self.king_white.get_possible_positions(0, 0), expected_positions)

        # Rey en la esquina inferior derecha
        self.board.set_piece(7, 7, self.king_white)
        expected_positions = [(6, 6), (6, 7), (7, 6)]  # Movimientos válidos en la esquina
        self.clear_positions(*expected_positions) # Limpia las posiciones esperadas
        self.assertEqual(self.king_white.get_possible_positions(7, 7), expected_positions)
    
    def test_king_cannot_move_out_of_bounds(self):
        """
        Verifica que el rey no pueda moverse fuera de los límites del tablero.

        Coloca el rey en la esquina del tablero y asegura que no pueda
        moverse a posiciones fuera de los límites.

        :return: None
        """
        self.board.set_piece(0, 0, self.king_white)
        invalid_positions = [(-1, 0), (0, -1), (-1, -1)]  # Fuera de los límites
        for pos in invalid_positions:
            with self.subTest(pos=pos):
                self.assertNotIn(pos, self.king_white.get_possible_positions(0, 0))

    def test_king_cannot_move_onto_self(self):
        """
        Verifica que el rey no pueda moverse a su propia posición.

        Asegura que el rey no pueda ocupar la misma posición en la que ya está.

        :return: None
        """
        self.assertNotIn((4, 4), self.king_white.get_possible_positions(4, 4))

    def clear_positions(self, *positions):
        """
        Limpia las posiciones especificadas en el tablero.

        :param positions: Tuplas de coordenadas (fila, columna) a limpiar.
        :return: None
        """
        for row, col in positions:
            self.board.set_piece(row, col, None)

if __name__ == '__main__':
    unittest.main()
