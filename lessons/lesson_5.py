empty_dot = "●"
row_1 = "1"
row_2 = "2"
row_3 = "3"
col_A = "a"
col_B = "b"
col_C = "c"

game_field = {
    row_1: {
        col_A: empty_dot,
        col_B: empty_dot,
        col_C: empty_dot
    },
    row_2: {
        col_A: empty_dot,
        col_B: empty_dot,
        col_C: empty_dot
    },
    row_3: {
        col_A: empty_dot,
        col_B: empty_dot,
        col_C: empty_dot
    }
}


def check_win():
    # Проверка по строкам
    if (game_field[row_1][col_A] == game_field[row_1][col_B]) and (
            game_field[row_1][col_A] == game_field[row_1][col_C]) and (game_field[row_1][col_A] != empty_dot):
        print(f"Победили {game_field[row_1][col_A]}")
        return False
    elif (game_field[row_2][col_A] == game_field[row_2][col_B]) and (
            game_field[row_2][col_A] == game_field[row_2][col_C]) and (game_field[row_2][col_A] != empty_dot):
        print(f"Победили {game_field[row_2][col_A]}")
        return False
    elif (game_field[row_3][col_A] == game_field[row_3][col_B]) and (
            game_field[row_3][col_A] == game_field[row_3][col_C]) and (game_field[row_3][col_A] != empty_dot):
        print(f"Победили {game_field[row_3][col_A]}")
        return False
    # Проверка по столбцам
    elif (game_field[row_1][col_A] == game_field[row_2][col_A]) and (
            game_field[row_1][col_A] == game_field[row_3][col_A]) and (game_field[row_1][col_A] != empty_dot):
        print(f"Победили {game_field[row_1][col_A]}")
        return False
    elif (game_field[row_1][col_B] == game_field[row_2][col_B]) and (
            game_field[row_1][col_B] == game_field[row_3][col_B]) and (game_field[row_1][col_B] != empty_dot):
        print(f"Победили {game_field[row_1][col_B]}")
        return False
    elif (game_field[row_1][col_C] == game_field[row_2][col_C]) and (
            game_field[row_1][col_C] == game_field[row_3][col_C]) and (game_field[row_1][col_C] != empty_dot):
        print(f"Победили {game_field[row_1][col_C]}")
        return False
    # Проверка по диагоналям
    elif (game_field[row_1][col_A] == game_field[row_2][col_B]) and (
            game_field[row_1][col_A] == game_field[row_3][col_C]) and (game_field[row_1][col_A] != empty_dot):
        print(f"Победили {game_field[row_1][col_A]}")
        return False
    elif (game_field[row_3][col_A] == game_field[row_2][col_B]) and (
            game_field[row_3][col_A] == game_field[row_1][col_C]) and (game_field[row_3][col_A] != empty_dot):
        print(f"Победили {game_field[row_3][col_A]}")
        return False
    else:
        return True


def check_empty(row, column):
    if game_field[row][column] == empty_dot:
        return True
    else:
        print(f"Выбранная ячейка {game_field[row][column]} занята, повторите ввод")
        return False


# def check_symbol(value):
#     allow_symbol = ["X", "O"]
#     if value in allow_symbol:
#         return True
#     else:
#         print(f"Выбран неверный символ: {value}, допустимые символы {allow_symbol} повторите ввод")
#         return False


def check_row(row):
    allow_row = [row_1, row_2, row_3]
    if row in allow_row:
        return True
    else:
        print(f"Строки {row} нет, допустимые строки {allow_row}, повторите ввод")
        return False


def check_column(column):
    allow_column = [col_A, col_B, col_C]
    if column in allow_column:
        return True
    else:
        print(f"Колонки {column} нет, допустимые колонки {column}, повторите ввод")
        return False


def check_input(dot_input):
    if len(dot_input) == 2:
        column = dot_input[1]
        row = dot_input[0].lower()

        if check_row(row) and check_column(column) and check_empty(row, column):
            return [row, column]
    else:
        print("Ошибка ввода, введите правильные данные")
        return False


def player_turn(current_player):
    input_dot_turn(input(f"Ходят - {current_player} (формат: 1а): "), current_player)
    print_game_field()


def input_dot_turn(dot_input, current_player):
    if check_input(dot_input):
        row, column = check_input(dot_input)
        game_field[row][column] = current_player
    else:
        player_turn()


def print_game_field():
    print(f"\t\ta\t\tb\t\tc\n")
    for key, value in game_field.items():
        print(f"{key}\t\t{value[col_A]}\t\t{value[col_B]}\t\t{value[col_C]}\n")
    print("\n")


def check_empty_symbols():
    empty_symbols = 0
    for dat in game_field.values():
        for d in dat.values():
            if d == empty_dot:
                empty_symbols += 1
    return empty_symbols


def run_game():
    print("Игра крестики-нолики")
    print_game_field()
    current_player = "X"
    while check_win():
        if check_empty_symbols() != 0:
            player_turn(current_player)
            check_win()
        else:
            print("Ничья")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    print("Игра окончена.")

run_game()
