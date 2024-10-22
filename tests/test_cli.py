import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.cli import main, play, get_valid_input

class TestCli(unittest.TestCase):

    # Prueba que el juego se salga correctamente cuando el usuario escribe 'EXIT'
    @patch('builtins.input', side_effect=['EXIT'] )
    def test_play_exit_game(self, mock_input):
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
        # Mockea la función print
        with patch('builtins.print') as mocked_print:
            main() # Llama a la función principal del juego
            # Verifica que se imprima "El juego ha terminado."
            mocked_print.assert_called_with("El juego ha terminado.")

    # Prueba que el juego gestione un empate correctamente cuando el usuario propone y acepta
    @patch('builtins.input', side_effect=['EMPATE', 'sí'])
    def test_play_draw(self, mock_input):
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
       
        # Verifica que se imprima "El juego ha terminado en empate."
        mocked_print.assert_any_call("El juego ha terminado en empate.")
        # Verifica que se haya llamado al método end_game del objeto chess
        chess.end_game.assert_called_once() # Verifica que se haya llamado al método end_game

    # Prueba que el juego termine cuando un jugador no tiene piezas
    @patch('builtins.input', side_effect=['1', '1', '1', '1'])  # Movimiento válido
    def test_play_no_pieces(self, mock_input):
        # Crea un objeto Chess mockeado
        chess = MagicMock(spec=Chess)
        # Configura las respuestas mockeadas
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.is_playing.return_value = False  # Simula que un jugador no tiene piezas
        chess.turn = 'WHITE'
        # Mockea la función print
        with patch('builtins.print') as mocked_print:
            play(chess) # Llama a la función play con el objeto chess mockeado
        
        # Verifica que se imprima "Un jugador se ha quedado sin piezas. El juego ha terminado."
        mocked_print.assert_any_call("Un jugador se ha quedado sin piezas. El juego ha terminado.")
        # Verifica que se haya llamado al método end_game del objeto chess
        chess.end_game.assert_called_once()  # Verifica que se haya llamado al método end_game


if __name__ == '__main__':
    unittest.main()

    

   
