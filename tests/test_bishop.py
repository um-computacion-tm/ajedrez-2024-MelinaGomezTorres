import unittest
from chess.piezas.bishop import Bishop
from chess.board import Board


class TestBishop(unittest.TestCase):

    def test_str(self):
        """
        Verifica que el símbolo del alfil sea el correcto según el color.
        
        Comprueba que el método __str__ devuelve '♝' para el alfil blanco
        y '♗' para el alfil negro.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        self.assertEqual(str(self.bishop_white),"♝")   # Símbolo para el alfil blanco
        bishop_black = Bishop("BLACK")
        self.assertEqual(str(bishop_black),"♗")        # Símbolo para el alfil negro

    def setUp(self):
        """
        Configura el tablero y el alfil blanco antes de cada prueba.
        
        Crea un tablero vacío para pruebas y coloca un alfil blanco en la
        posición (4, 4) del tablero.
        """
        self.board = Board(for_test=True) 
        self.bishop_white = Bishop("WHITE", self.board)    # Crea un alfil blanco
        self.board.set_piece(4, 4, self.bishop_white)   # Coloca el alfil blanco en la posición (4, 4) en el tablero
    
    def test_bishop_valid_moves(self):
        """
        Verifica los movimientos válidos del alfil.
        
        Comprueba que el alfil puede moverse a posiciones válidas en diagonal
        y que no puede moverse a posiciones no válidas, como horizontal o vertical.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si alguna de las aserciones falla.
        """
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 5))  # Movimiento válido diagonal (hacia arriba a la derecha)
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 3, 3))  # Movimiento válido diagonal (hacia abajo a la izquierda)
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 4))  # Movimiento no válido (horizontal)
        # Verifica que el alfil no puede saltar sobre la pieza aliada (no puede moverse a (2, 2))
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 4, 5))  # Movimiento no válido (vertical)

    def test_bishop_cannot_jump_over_ally(self):
        """
        Verifica que el alfil no puede saltar sobre piezas aliadas.

        Coloca un alfil aliado en el camino del alfil blanco y verifica
        que el movimiento a la posición en diagonal está bloqueado.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        self.board.set_piece(3, 3, Bishop("WHITE", self.board)) 
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 2, 2))  # No puede moverse

    def test_bishop_can_capture_enemy(self):
        """
        Verifica que el alfil puede capturar piezas enemigas.

        Coloca un alfil enemigo en la posición del alfil blanco y verifica
        que el movimiento a esa posición para capturar al enemigo es válido.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        self.board.set_piece(5, 5, Bishop("BLACK", self.board)) 
        # Verifica que el alfil blanco puede moverse a la posición (5, 5) para capturar al enemigo
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 5))  # Movimiento válido (captura)

    def test_bishop_moves_until_obstacle(self):
        """
        Verifica que el alfil se detiene al encontrar un obstáculo.

        Coloca un alfil aliado en la diagonal del alfil blanco y verifica
        que el alfil no puede moverse más allá de esa pieza.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        self.board.set_piece(6, 6, Bishop("WHITE", self.board))  
        # Verifica que el alfil no puede moverse más allá de la pieza aliada (no puede moverse a (7, 7))
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 7, 7))  # No puede moverses


if __name__ == "__main__":
    unittest.main()





