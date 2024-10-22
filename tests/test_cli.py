import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.cli import main, play, get_valid_input

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['EMPATE', 'no'])
    def test_play_draw_rejection(self, mock_input):
        """
        Verifica que el juego continúe cuando se rechaza una propuesta de empate.

        Este método simula la jugabilidad del ajedrez donde se rechaza una
        propuesta de empate por parte del jugador y verifica que el juego
        sigue activo, mostrando el tablero sin terminar el juego.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        chess = MagicMock(spec=Chess) 
        chess.is_playing.return_value = True # El juego está en curso
        chess.show_board.return_value = "Tablero" # Muestra un tablero ficticio
        chess.turn = 'WHITE' # Establece que es el turno de las piezas blancas
        
        with patch('builtins.print') as mocked_print:
            play(chess) # Llama a la función play para simular el juego
    
    # Verificar que el juego continúa después de rechazar el empate
        mocked_print.assert_any_call("Tablero") # Se debe mostrar el tablero
        chess.end_game.assert_not_called()  # El juego no debe terminar

    @patch('builtins.input', side_effect=['10', '-1', 'abc', '3'])
    def test_get_valid_input_invalid(self, mock_input):
        """
        Verifica que la función get_valid_input maneja entradas inválidas correctamente.

        Este método simula varias entradas no válidas (fuera de rango,
        negativas y no numéricas) antes de una entrada válida y asegura
        que la función retorna el valor válido.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Verifica que la función get_valid_input maneja entradas inválidas correctamente
        # Simula varias entradas no válidas (fuera de rango, negativos y no numéricas) antes de una entrada válida
        with patch('builtins.print') as mocked_print:
            result = get_valid_input("Enter value: ") # Llama a la función para obtener una entrada válida
            self.assertEqual(result, 3)  # Verificar que retorna el valor válido finalmente
            mocked_print.assert_any_call("Por favor, ingresa un número entre 0 y 7.")  # Mensaje para rango inválido
            mocked_print.assert_any_call("Entrada inválida. Por favor, ingresa un número válido.") # Mensaje para entrada no numérica

    # Prueba que el juego se salga correctamente cuando el usuario escribe 'EXIT'
    @patch('builtins.input', side_effect=['EXIT'] )
    def test_play_exit_game(self, mock_input):
        """
        Verifica que el juego se salga correctamente cuando el usuario escribe 'EXIT'.

        Este método simula que el usuario desea salir del juego
        inmediatamente y asegura que se llame al método exit_game
        y que se imprima el mensaje correspondiente.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Mockea un objeto Chess para simular el juego
        chess = MagicMock(spec=Chess)
        # Configura las respuestas mockeadas
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.__has_pieces__.return_value = True
        chess.turn = 'WHITE'

        # Mockea la función print para verificar las salidas en consola
        with patch('builtins.print') as mocked_print:
            play(chess) # Llama a la función play con el objeto mockeado
        # Verifica que se imprima "El juego ha terminado."
        mocked_print.assert_any_call("El juego ha terminado.")
        chess.exit_game.assert_called_once()  # Verifica que se haya llamado al método exit_game

    # Prueba que se gestione una propuesta de empate correctamente
    @patch('builtins.input', side_effect= [
        'EMPATE', 'sí',  # El usuario propone empate y acepta
    ])
    def test_draw_proposal(self, mock_input):
        """
        Verifica que se gestione una propuesta de empate correctamente.

        Este método simula que el usuario propone un empate y acepta
        la propuesta, asegurando que se imprima el mensaje de empate.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Mockea la función print para verificar lo que se imprime en consola
        with patch('builtins.print') as mocked_print:
            main() # Llama a la función principal
            # Verifica que se imprima "El juego ha terminado en empate."
            mocked_print.assert_called_with("El juego ha terminado en empate.")

    # Prueba que el juego termine cuando el usuario elige salir inmediatamente
    @patch('builtins.input', side_effect= [
        'EXIT'  # Salir inmediatamente
    ])

    def test_play_exit(self, mock_input,):
        """
        Verifica que el juego termine cuando un jugador elige salir.

        Este método simula que el jugador elige salir del juego
        inmediatamente y asegura que se imprima el mensaje correspondiente.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Mockea la función print
        with patch('builtins.print') as mocked_print:
            main() # Llama a la función principal del juego
            mocked_print.assert_called_with("El juego ha terminado.")

    @patch('builtins.input', side_effect=['EMPATE', 'sí'])
    def test_play_draw(self, mock_input):
        """
        Verifica que el juego gestione un empate correctamente cuando el usuario propone y acepta.

        Este método simula que el usuario propone un empate y acepta
        la propuesta, asegurando que se imprima el mensaje de empate
        y se llame al método end_game.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Crea un objeto Chess mockeado
        chess = MagicMock(spec=Chess)
        # Configura las respuestas mockeadas
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.is_playing.return_value = True
        chess.turn = 'WHITE'

        # Mockea la función print
        with patch('builtins.print') as mocked_print:
            play(chess) # Llama a la función play con el objeto chess mockeado
        mocked_print.assert_any_call("El juego ha terminado en empate.")
        chess.end_game.assert_called_once() 

    @patch('builtins.input', side_effect=['1', '1', '1', '1'])  # Movimiento válido
    def test_play_no_pieces(self, mock_input):
        """
        Verifica que el juego termine cuando un jugador no tiene piezas.

        Este método simula que un jugador se queda sin piezas y
        asegura que se imprima el mensaje correspondiente y se llame
        al método end_game.

        :param mock_input: Simulación de la entrada del usuario.
        :return: None
        """
        # Crea un objeto Chess mockeado
        chess = MagicMock(spec=Chess)
        # Configura las respuestas mockeadas
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.is_playing.return_value = False  
        chess.turn = 'WHITE'
        # Mockea la función print
        with patch('builtins.print') as mocked_print:
            play(chess) # Llama a la función play con el objeto chess mockeado
        
        # Verifica que se imprima "Un jugador se ha quedado sin piezas. El juego ha terminado."
        mocked_print.assert_any_call("Un jugador se ha quedado sin piezas. El juego ha terminado.")
        chess.end_game.assert_called_once()  


if __name__ == '__main__':
    unittest.main()

    

   
