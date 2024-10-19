import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.cli import main, play, get_valid_input

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['EXIT'] )
    def test_play_exit_game(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.__has_pieces__.return_value = True
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("El juego ha terminado.")
        chess.exit_game.assert_called_once()


    @patch('builtins.input', side_effect= [
        'EMPATE', 'sí',  # El usuario propone empate y acepta
    ])
    def test_draw_proposal(self, mock_input):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_called_with("El juego ha terminado en empate.")

    @patch('builtins.input', side_effect= [
        'EXIT'  # Salir inmediatamente
    ])

    def test_play_exit(self, mock_input,):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_called_with("El juego ha terminado.")

    @patch('builtins.input', side_effect=['EMPATE', 'sí'])
    def test_play_draw(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.is_playing.return_value = True
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("El juego ha terminado en empate.")
        chess.end_game.assert_called_once()

    @patch('builtins.input', side_effect=['1', '1', '1', '1'])  # Movimiento válido
    def test_play_no_pieces(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.is_playing.return_value = False  # Simula que un jugador no tiene piezas
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("Un jugador se ha quedado sin piezas. El juego ha terminado.")
        chess.end_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()

    

   


'''
import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.cli import main, play, get_valid_input

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['EXIT'])
    def test_play_exit_game(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.__has_pieces__.return_value = True
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("El juego ha terminado.")
        chess.exit_game.assert_called_once()

    @patch('builtins.input', side_effect=[
        'EMPATE', 'sí',  # El usuario propone empate y acepta
    ])
    def test_draw_proposal(self, mock_input):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_called_with("El juego ha terminado en empate.")

    @patch('builtins.input', side_effect=[
        'EXIT'  # Salir inmediatamente
    ])
    def test_play_exit(self, mock_input):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_called_with("El juego ha terminado.")

    @patch('builtins.input', side_effect=['EMPATE', 'sí'])
    def test_play_draw(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.__has_pieces__.return_value = True
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("El juego ha terminado en empate.")
        chess.end_game.assert_called_once()

    @patch('builtins.input', side_effect=['1', '1', '1', '1'])  # Movimiento válido
    def test_play_no_pieces(self, mock_input):
        chess = MagicMock(spec=Chess)
        chess.is_playing.return_value = True
        chess.show_board.return_value = "Tablero"
        chess.__has_pieces__.return_value = False  # Simula que un jugador no tiene piezas
        chess.turn = 'WHITE'

        with patch('builtins.print') as mocked_print:
            play(chess)

        mocked_print.assert_any_call("Un jugador se ha quedado sin piezas. El juego ha terminado.")
        chess.end_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()'''





