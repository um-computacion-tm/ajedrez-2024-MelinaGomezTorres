from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row (0-7): "))
        from_col = int(input("From col (0-7): "))
        to_row = int(input("To Row (0-7): "))
        to_col = int(input("To Col (0-7): "))

#Aquí se verifica que las coordenadas estén en el rango 0-7, si no, lanza un error
        if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
            raise ValueError("Las coordenadas deben estar entre 0 y 7.")

        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
    except Exception as e:
        print("Error", e)



if __name__ == '__main__':
    main()