from chess.chess import Chess

def main():
    chess = Chess()  # Inicializa el juego de ajedrez
    while chess.is_playing():
        play(chess)  # Llama a la función de juego

# Controla el flujo principal del juego en cada turno.
# Este método permite a los jugadores realizar movimientos en el tablero de ajedrez
# Y gestionar las acciones de fin de juego como salir o proponer un empate.
# Parámetros:
# chess (Chess): Instancia del juego de ajedrez que se está jugando.
def play(chess):
    try:
        print(chess.show_board()) # Muestra el tablero actual en la consola
        # Informa al jugador de qué color es su turno (blancas o negras).
        print(f"Turno de las piezas {'blancas' if chess.turn == 'WHITE' else 'negras'}.")

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if not chess.is_playing():
            chess.end_game() # Finaliza el juego si no hay piezas.
            print("Un jugador se ha quedado sin piezas. El juego ha terminado.")
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

# Solicita al usuario una entrada válida y devuelve un número entero entre 0 y 7.
# Parámetros:
# prompt (str): Mensaje que se muestra al usuario para solicitar entrada.
# Retorna:
# int: Un número entero válido entre 0 y 7.
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
