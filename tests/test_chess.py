#Importo el módulo y la clase "Chess" desde la carpeta con el mismo nombre
#Importo más clases (Board y Piece)
import unittest
from chess.chess import Chess
from chess.exceptions import InvalidMove, EmptyPosition
#Creo la clase correspondiente para este test 
# Entro de setUp (se ejecuta automáticamente antes de cada prueba para asegurar que estas no se repitan)
# Creo una nueva instancia del juego de ajedrez (self.game = Chess())

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.__game__ = Chess()

# Asegura que el juego esté en marcha cuando se llama al método is_playing
    def test_is_playing(self):
        self.assertTrue(self.__game__.is_playing(), "El juego debería estar en curso")

#Verifica que el turno incial sea de las piezas blancas, casa contrario se mostrará un mensaje indicando el error
    def test_initial_turn(self):
        self.assertEqual(self.__game__.turn, "WHITE" , "El turno inicial debe ser de las piezas blancas")
        # Cambiar el turno a "BLACK"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "BLACK", "El turno debe cambiar a negro ('BLACK')")
        
        # Cambiar el turno de nuevo a "WHITE"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "WHITE", "El turno debe cambiar a blanco ('WHITE') nuevamente")

    def test_move_piece(self):
    # Mover una pieza válida (Peón)

        self.__game__.move(6, 0, 5, 0)  # Mover el peón blanco de (6,0) a (5,0)
        piece = self.__game__.get_board().get_piece(5, 0)  
        self.assertIsNotNone(piece, "El peón debe estar en la nueva posición.")
        self.assertEqual(piece.get_color(), "WHITE", "La pieza debe ser blanca.")

    def test_has_pieces_both_colors(self):
        # Asumiendo que el tablero al iniciar el juego tiene piezas de ambos colores
        self.assertTrue(self.__game__.__has_pieces__(), "Debe haber piezas de ambos colores al iniciar el juego")

    def test_has_pieces_no_white(self):
        # Quitar todas las piezas blancas
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "WHITE":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las blancas")

    def test_has_pieces_no_black(self):
        # Quitar todas las piezas negras
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "BLACK":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las negras")

    def test_game_ends_when_no_pieces(self):
        # Terminar el juego cuando no quedan piezas
        self.__game__.get_board().__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.assertFalse(self.__game__.is_playing(), "El juego debe estar terminado.")


    def test_move_game_over(self):
        # Simular fin del juego
        self.__game__.end_game()  # Método que se llama cuando el juego termina
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el juego ha terminado"):
            self.__game__.move(0, 0, 0, 1)

    def test_move_empty_position(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition, msg="Debe lanzar EmptyPosition si no hay pieza en la posición"):
            self.__game__.move(3, 3, 3, 4)  # Asumiendo que la posición (3, 3) está vacía al inicio

    def test_move_invalid_move(self):
        # Intentar hacer un movimiento inválido
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el movimiento no es válido"):
            self.__game__.move(0, 0, 2, 2)  # Movimiento inválido para una torre

#Se compara el turno actual con el turno guardado antes de la acción. Si son iguales, el test pasa, sino, el test falla con el mensaje especificado
    def test_turn_unchanged(self):
        initial_turn = self.__game__.turn
        self.__game__.is_playing()  # Acción que no debería cambiar el turno
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar al llamar a is_playing()")

#Verifica que el turno de los jugadores no cambia cuando se realiza un movimiento inválido
    def test_turn_unchanged_after_invalid_move(self):
        initial_turn = self.__game__.turn
        try:
            self.__game__.move(10, 10, 11, 11)  # Movimiento inválido de ejemplo
        except Exception:
            pass
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar después de un movimiento inválido")

                         
if __name__ == '__main__':
    unittest.main()




'''class TestChess(unittest.TestCase):
    def setUp(self):
        self.__game__ = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.__game__.turn, "WHITE", "El turno inicial debe ser blanco.")
        # Cambiar el turno a "BLACK"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "BLACK", "El turno debe cambiar a negro ('BLACK')")
        
        # Cambiar el turno de nuevo a "WHITE"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "WHITE", "El turno debe cambiar a blanco ('WHITE') nuevamente")

    def test_move_piece(self):
    # Mover una pieza válida (Peón)

        self.__game__.move(6, 0, 5, 0)  # Mover el peón blanco de (6,0) a (5,0)
        piece = self.__game__.get_board().get_piece(5, 0)  
        self.assertIsNotNone(piece, "El peón debe estar en la nueva posición.")
        self.assertEqual(piece.get_color(), "WHITE", "La pieza debe ser blanca.")

    def test_has_pieces_both_colors(self):
        # Asumiendo que el tablero al iniciar el juego tiene piezas de ambos colores
        self.assertTrue(self.__game__.__has_pieces__(), "Debe haber piezas de ambos colores al iniciar el juego")

    def test_has_pieces_no_white(self):
        # Quitar todas las piezas blancas
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "WHITE":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las blancas")

    def test_has_pieces_no_black(self):
        # Quitar todas las piezas negras
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "BLACK":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las negras")

    def test_game_ends_when_no_pieces(self):
        # Terminar el juego cuando no quedan piezas
        self.__game__.get_board().__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.assertFalse(self.__game__.is_playing(), "El juego debe estar terminado.")


    def test_move_game_over(self):
        # Simular fin del juego
        self.__game__.end_game()  # Método que se llama cuando el juego termina
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el juego ha terminado"):
            self.__game__.move(0, 0, 0, 1)

    def test_move_empty_position(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition, msg="Debe lanzar EmptyPosition si no hay pieza en la posición"):
            self.__game__.move(3, 3, 3, 4)  # Asumiendo que la posición (3, 3) está vacía al inicio

    def test_move_invalid_move(self):
        # Intentar hacer un movimiento inválido
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el movimiento no es válido"):
            self.__game__.move(0, 0, 2, 2)  # Movimiento inválido para una torre

if __name__ == "__main__":
    unittest.main()'''






