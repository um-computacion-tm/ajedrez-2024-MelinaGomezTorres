from chess.chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print(f"Turno de las piezas {'blancas' if chess.turn == 'WHITE' else 'negras'}.")

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if not chess.is_playing():
            chess.end_game()
            print("Un jugador se ha quedado sin piezas. El juego ha terminado.")
            return

        decision = input("Escribe 'EXIT' para salir o escribe 'EMPATE' para proponer empate. Si no, continúa: ").strip().upper()
        if decision == "EXIT":
            chess.exit_game()
            print("El juego ha terminado.")
            return

        if decision == "EMPATE":
            draw_decision = input("¿Ambos jugadores acuerdan el empate? (sí/no): ").lower()
            if draw_decision == "sí":
                chess.end_game()
                print("El juego ha terminado en empate.")
                return
            
        from_row = get_valid_input("From row: ")
        from_col = get_valid_input("From col: ")
        to_row = get_valid_input("To Row: ")
        to_col = get_valid_input("To Col: ")

        chess.move(from_row, from_col, to_row, to_col,)

    except Exception as e:
        print("Error", e)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 7:  
                return value
            else:
                print("Por favor, ingresa un número entre 0 y 7.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")



if __name__ == '__main__':
    main()

'''from chess.chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print(f"Turno de las piezas {'blancas' if chess.turn == 'WHITE' else 'negras'}.")

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if not chess.__has_pieces__():
            chess.end_game()
            print("Un jugador se ha quedado sin piezas. El juego ha terminado.")
            return

        decision = input("Escribe 'EXIT' para salir o escribe 'EMPATE' para proponer empate. Si no, continúa: ").strip().upper()
        if decision == "EXIT":
            chess.exit_game()
            print("El juego ha terminado.")
            return

        if decision == "EMPATE":
            draw_decision = input("¿Ambos jugadores acuerdan el empate? (sí/no): ").lower()
            if draw_decision == "sí":
                chess.end_game()
                print("El juego ha terminado en empate.")
                return

        # Pedimos el movimiento por separado (primero origen, luego destino)
        from_row = get_valid_input("From row (fila de origen): ")
        from_col = get_valid_input("From col (columna de origen): ")
        to_row = get_valid_input("To row (fila de destino): ")
        to_col = get_valid_input("To col (columna de destino): ")

        # Realizar el movimiento
        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Error:", e)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 7:  # Asumiendo que el tablero es de 8x8
                return value
            else:
                print("Por favor, ingresa un número entre 0 y 7.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")


if __name__ == '__main__':
    main()'''




























