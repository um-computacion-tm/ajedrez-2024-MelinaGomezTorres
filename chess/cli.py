from chess.chess import Chess

def main():
    """
    Función principal que inicializa el juego de ajedrez y gestiona el flujo del juego.
    """
    chess = Chess()  # Inicializa el juego de ajedrez
    while chess.is_playing():
        play(chess)  # Llama a la función de juego

def play(chess):
    """
    Gestiona el turno del jugador, permitiendo realizar movimientos y gestionar acciones como salir o proponer un empate.
    
    Parámetros:
    chess (Chess): Instancia del juego de ajedrez que se está jugando.

    Realiza:
    - Muestra el tablero actual.
    - Informa al jugador sobre su turno.
    - Solicita decisiones de fin de juego (salir o proponer empate).
    - Solicita las coordenadas de movimiento.
    
    Devuelve:
    - None: Sale de la función si el juego ha terminado o se ha decidido salir.
    """
    try:
        print(chess.show_board()) # Muestra el tablero actual en la consola
        # Informa al jugador de qué color es su turno (blancas o negras).
        print(f"Turno de las piezas {'blancas' if chess.turn == 'WHITE' else 'negras'}.")

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if not chess.is_playing():
            print("Un jugador se ha quedado sin piezas. El juego ha terminado.")
            chess.end_game() # Finaliza el juego si no hay piezas.
            return # Sale de la función ya que el juego ha terminado

        # Solicita al jugador que ingrese una decisión: salir o proponer un empate.
        decision = input("Escribe 'EXIT' para salir o escribe 'EMPATE' para proponer empate. Si no, continúa: ").strip().upper()
        if decision == "EXIT":
            chess.exit_game() # Cambia el estado del juego a terminado.
            print("El juego ha terminado.")
            return

        # Si el jugador decide proponer un empate, se solicita la confirmación.
        if decision == "EMPATE":
            draw_decision = input("¿Ambos jugadores acuerdan el empate? (sí/no): ").lower()
            if draw_decision == "sí":
                chess.end_game()  # Cambia el estado del juego a terminado.
                print("El juego ha terminado en empate.")
                return
            
        # Solicita las coordenadas de la pieza a mover y la posición de destino.    
        from_row = get_valid_input("From row: ") # Fila de origen.
        from_col = get_valid_input("From col: ") # Columna de origen.
        to_row = get_valid_input("To Row: ") # Fila de destino.
        to_col = get_valid_input("To Col: ") # Columna de destino.

        # Realiza el movimiento de la pieza en el tablero.
        chess.move(from_row, from_col, to_row, to_col,)

    # Manejo de excepciones: imprime el mensaje de error en caso de cualquier fallo.
    except Exception as e:
        print("Error", e)

def get_valid_input(prompt):
    """
    Solicita al usuario un número entero entre 0 y 7.

    Parámetros:
    prompt (str): Mensaje que se muestra al usuario para solicitar entrada.

    Retorna:
    int: Un número entero válido entre 0 y 7.

    Realiza:
    - Valida que la entrada sea un número entre 0 y 7.
    """
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
