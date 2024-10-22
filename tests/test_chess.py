import unittest
from chess.chess import Chess
from chess.exceptions import InvalidMove, EmptyPosition

class TestChess(unittest.TestCase):
    
    def setUp(self):
        """
        Inicializa una nueva instancia del juego de ajedrez antes de cada prueba.
        
        Este método se llama automáticamente antes de cada método de prueba,
        asegurando que cada prueba comience con un nuevo juego de ajedrez.
        
        :Return: None
        """
        self.__game__ = Chess() 

    def test_is_playing(self):
        """
        Verifica que el juego esté en curso.
        
        Este método comprueba si el juego ha comenzado y que el estado
        del juego es 'en curso'.
        
        :Return: None
        :raises: AssertionError si el juego no está en curso.
        """
        self.assertTrue(self.__game__.is_playing(), "El juego debería estar en curso")

    def test_initial_turn(self):
        """
        Verifica que el turno inicial sea de las piezas blancas y que 
        los turnos cambien correctamente.
        
        Este método comprueba que el turno inicial sea "WHITE", cambia
        el turno a "BLACK" y luego de vuelta a "WHITE", verificando que
        los cambios se realicen correctamente.
        
        :Return: None
        :Raises: AssertionError si el turno inicial no es "WHITE" o 
                  si el cambio de turno no se realiza como se espera.
        """
        self.assertEqual(self.__game__.turn, "WHITE" , "El turno inicial debe ser de las piezas blancas")
        # Cambiar el turno a "BLACK"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "BLACK", "El turno debe cambiar a negro ('BLACK')")
        
        # Cambiar el turno de nuevo a "WHITE"
        self.__game__.change_turn()
        self.assertEqual(self.__game__.__turn__, "WHITE", "El turno debe cambiar a blanco ('WHITE') nuevamente")

    def test_move_piece(self):
        """
        Verifica que se puede mover una pieza válida (peón) a una nueva posición.
        
        Este método mueve el peón blanco desde (6,0) a (5,0) y verifica
        que la pieza se encuentra en la nueva posición y que su color es
        correcto.
        
        :Return: None
        :Raises: AssertionError si la pieza no se encuentra en la nueva 
                  posición o si el color de la pieza no es "WHITE".
        """
        self.__game__.move(6, 0, 5, 0)  # Mover el peón blanco de (6,0) a (5,0)
        piece = self.__game__.get_board().get_piece(5, 0)  
        self.assertIsNotNone(piece, "El peón debe estar en la nueva posición.")
        self.assertEqual(piece.get_color(), "WHITE", "La pieza debe ser blanca.")

    def test_has_pieces_both_colors(self):
        """
        Verifica que al iniciar el juego hay piezas de ambos colores en el tablero.
        
        Este método asume que el tablero está correctamente inicializado y
        que debe contener piezas de ambos colores (blancas y negras).
        
        :Return: None
        :Raises: AssertionError si no hay piezas de ambos colores en el tablero.
        """
        # Asumiendo que el tablero al iniciar el juego tiene piezas de ambos colores
        self.assertTrue(self.__game__.__has_pieces__(), "Debe haber piezas de ambos colores al iniciar el juego")

    def test_has_pieces_no_white(self):
        """
        Verifica que no hay piezas blancas en el tablero.
        
        Este método elimina todas las piezas blancas del tablero y verifica
        que el método `__has_pieces__` devuelva `False`, indicando que
        falta una de las piezas de color.
        
        :Return: None
        :Raises: AssertionError si aún hay piezas blancas en el tablero.
        """
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "WHITE":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las blancas")

    def test_has_pieces_no_black(self):
        """
        Verifica que no hay piezas negras en el tablero.
        
        Este método elimina todas las piezas negras del tablero y verifica
        que el método `__has_pieces__` devuelva `False`, indicando que
        falta una de las piezas de color.
        
        :Return: None
        :Raises: AssertionError si aún hay piezas negras en el tablero.
        """
        for row in self.__game__.__board__.__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "BLACK":
                    row[i] = None
        self.assertFalse(self.__game__.__has_pieces__(), "No debe haber piezas de ambos colores si faltan las negras")

    def test_game_ends_when_no_pieces(self):
        """
        Verifica que el juego termina cuando no quedan piezas en el tablero.
        
        Este método establece el tablero para que no tenga piezas y verifica
        que el estado del juego cambie a 'terminado'.
        
        :Return: None
        :Raises: AssertionError si el juego no está terminado.
        """
        self.__game__.get_board().__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.assertFalse(self.__game__.is_playing(), "El juego debe estar terminado.")

    def test_move_game_over(self):
        """
        Verifica que se lanza una excepción al intentar mover piezas cuando el juego ha terminado.
        
        Este método termina el juego y luego intenta hacer un movimiento,
        verificando que se lance `InvalidMove`.
        
        :Return: None
        :Raises: InvalidMove si se intenta mover cuando el juego ha terminado.
        """
        # Simular fin del juego
        self.__game__.end_game()  # Método que se llama cuando el juego termina
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el juego ha terminado"):
            self.__game__.move(0, 0, 0, 1)

    def test_move_empty_position(self):
        """
        Verifica que se lanza una excepción al intentar mover desde una posición vacía.
        
        Este método intenta mover una pieza desde una posición que se supone
        está vacía, y verifica que se lance `EmptyPosition`.
        
        :Return: None
        :Raises: EmptyPosition si se intenta mover desde una posición sin pieza.
        """
        with self.assertRaises(EmptyPosition, msg="Debe lanzar EmptyPosition si no hay pieza en la posición"):
            self.__game__.move(3, 3, 3, 4)  # Asumiendo que la posición (3, 3) está vacía al inicio

    def test_move_invalid_move(self):
        """
        Verifica que se lanza una excepción al intentar hacer un movimiento inválido.
        
        Este método intenta realizar un movimiento que no es válido según las
        reglas del ajedrez y verifica que se lance `InvalidMove`.
        
        :Return: None
        :Raises: InvalidMove si se intenta hacer un movimiento inválido.
        """
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el movimiento no es válido"):
            self.__game__.move(0, 0, 2, 2)  # Movimiento inválido para una torre

    def test_turn_unchanged(self):
        """
        Verifica que el turno no cambie al llamar al método is_playing().
        
        Este método guarda el turno actual, llama a `is_playing` y verifica
        que el turno no cambie.
        
        :Return: None
        :Raises: AssertionError si el turno cambia después de llamar a `is_playing`.
        """
        initial_turn = self.__game__.turn
        self.__game__.is_playing()  # Acción que no debería cambiar el turno
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar al llamar a is_playing()")

    def test_turn_unchanged_after_invalid_move(self):
        """
        Verifica que el turno no cambie después de un movimiento inválido.
        
        Este método guarda el turno actual, intenta realizar un movimiento
        inválido y verifica que el turno no cambie después del intento.
        
        :Return: None
        :Raises: AssertionError si el turno cambia después de un movimiento inválido.
        """
        initial_turn = self.__game__.turn
        try:
            self.__game__.move(10, 10, 11, 11)  # Movimiento inválido de ejemplo
        except Exception:
            pass
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar después de un movimiento inválido")

    def test_turn_changes_after_valid_move(self):
        """
        Verifica que el turno cambie a negro después de un movimiento válido.
        
        Este método mueve el peón blanco y verifica que el turno cambie
        a "BLACK" después del movimiento.
        
        :Return: None
        :Raises: AssertionError si el turno no cambia a "BLACK" después de un movimiento válido.
        """
        self.__game__.move(6, 0, 5, 0)  # Mover el peón blanco de (6, 0) a (5, 0) y verifica que el turno cambie a negro
        self.assertEqual(self.__game__.turn, "BLACK", "El turno debe cambiar a negro después de un movimiento válido.")

    def test_move_out_of_bounds(self):
        """
        Intenta mover una pieza fuera de los límites del tablero y verifica que se lance InvalidMove.
        
        Este método intenta mover una pieza a una posición que está fuera del
        rango del tablero y verifica que se produzca la excepción adecuada.
        
        :return: None
        :raises: InvalidMove si el movimiento está fuera de los límites.
        """
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si el movimiento está fuera de los límites"):
            self.__game__.move(6, 0, 8, 0)  # Fuera del rango del tablero
   
    def test_propose_draw(self):
        """
        Verifica que la propuesta de empate devuelve el mensaje esperado.
    
        Este método llama al método `propose_draw` del juego y comprueba que
        el mensaje devuelto sea "DRAW_PROPOSAL", indicando que la propuesta
        de empate se ha realizado correctamente.
    
        :Return: None
        :Raises: AssertionError si el mensaje devuelto no es "DRAW_PROPOSAL".
        """
        self.assertEqual(self.__game__.propose_draw(), "DRAW_PROPOSAL", "La propuesta de empate debe devolver 'DRAW_PROPOSAL'.")

    def test_exit_game(self):
        """
        Verifica que el juego se haya terminado correctamente al salir.
    
        Este método llama al método `exit_game` del juego y luego verifica
        que el estado del juego cambie a 'terminado' utilizando el método 
        `is_playing()`.
    
        :Return: None
        :Raises: AssertionError si el juego sigue en curso después de llamar
              a `exit_game`.
        """
        self.__game__.exit_game()
        self.assertFalse(self.__game__.is_playing(), "El juego debe estar terminado después de llamar a exit_game.")

    def test_invalid_rook_move(self):
        """
        Verifica que se lanza una excepción al intentar mover la torre de manera inválida.
    
        Este método intenta mover la torre desde (7, 0) a (6, 1), lo que
        representa un movimiento diagonal que no es válido para una torre.
        Se espera que se lance `InvalidMove` en esta situación.
    
        :Return: None
        :Raises: InvalidMove si se intenta mover la torre de manera diagonal.
        """
        with self.assertRaises(InvalidMove, msg="Debe lanzar InvalidMove si la torre intenta moverse diagonalmente"):
            self.__game__.move(7, 0, 6, 1)  # Movimiento inválido para una torre (diagonal)

    def test_game_ends_when_no_black_pieces(self):
        """
        Verifica que el juego termine cuando no quedan piezas negras en el tablero.
    
        Este método elimina todas las piezas negras del tablero y verifica
        que el estado del juego cambie a 'terminado', lo que significa que
        no hay piezas disponibles para continuar jugando.
    
       :Return: None
       :Raises: AssertionError si el juego sigue en curso después de eliminar
              las piezas negras.
       """
        for row in self.__game__.get_board().__positions__:
            for i, piece in enumerate(row):
                if piece and piece.get_color() == "BLACK":
                    row[i] = None
        self.assertFalse(self.__game__.is_playing(), "El juego debe terminar cuando no quedan piezas negras.")


                         
if __name__ == '__main__':
    unittest.main()









