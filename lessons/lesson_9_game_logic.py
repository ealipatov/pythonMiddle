empty_dot = "●"
row_1 = "1"
row_2 = "2"
row_3 = "3"
col_A = "a"
col_B = "b"
col_C = "c"

game_status = "Игра продолжается"

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
        return f"Победили {game_field[row_1][col_A]}"
    elif (game_field[row_2][col_A] == game_field[row_2][col_B]) and (
            game_field[row_2][col_A] == game_field[row_2][col_C]) and (game_field[row_2][col_A] != empty_dot):
        return f"Победили {game_field[row_2][col_A]}"
    elif (game_field[row_3][col_A] == game_field[row_3][col_B]) and (
            game_field[row_3][col_A] == game_field[row_3][col_C]) and (game_field[row_3][col_A] != empty_dot):
        return f"Победили {game_field[row_3][col_A]}"
    # Проверка по столбцам
    elif (game_field[row_1][col_A] == game_field[row_2][col_A]) and (
            game_field[row_1][col_A] == game_field[row_3][col_A]) and (game_field[row_1][col_A] != empty_dot):
        return f"Победили {game_field[row_1][col_A]}"
    elif (game_field[row_1][col_B] == game_field[row_2][col_B]) and (
            game_field[row_1][col_B] == game_field[row_3][col_B]) and (game_field[row_1][col_B] != empty_dot):
        return f"Победили {game_field[row_1][col_B]}"
    elif (game_field[row_1][col_C] == game_field[row_2][col_C]) and (
            game_field[row_1][col_C] == game_field[row_3][col_C]) and (game_field[row_1][col_C] != empty_dot):
        return f"Победили {game_field[row_1][col_C]}"
    # Проверка по диагоналям
    elif (game_field[row_1][col_A] == game_field[row_2][col_B]) and (
            game_field[row_1][col_A] == game_field[row_3][col_C]) and (game_field[row_1][col_A] != empty_dot):
        return f"Победили {game_field[row_1][col_A]}"
    elif (game_field[row_3][col_A] == game_field[row_2][col_B]) and (
            game_field[row_3][col_A] == game_field[row_1][col_C]) and (game_field[row_3][col_A] != empty_dot):
        return f"Победили {game_field[row_3][col_A]}"
    else:
        return game_status


def check_empty(row, column):
    if game_field[row][column] == empty_dot:
        return True
    else:
        return False


def check_row(row):
    allow_row = [row_1, row_2, row_3]
    if row in allow_row:
        return True
    else:
        return False


def check_column(column):
    allow_column = [col_A, col_B, col_C]
    if column in allow_column:
        return True
    else:
        return False


def check_input(dot_input, current_player):
    if len(dot_input) == 2:
        column = dot_input[1]
        row = dot_input[0].lower()

        if not check_empty(row, column):
            return f"Выбранная ячейка {game_field[row][column]} занята, повторите ввод"

        if not check_row(row):
            return f"Строки {row} нет, повторите ввод"

        if not check_column(column):
            return f"Колонки {column} нет, допустимые колонки {column}, повторите ввод"

        if check_row(row) and check_column(column) and check_empty(row, column):
            game_field[row][column] = current_player
            return f"{current_player} сделали ход в ячейку {row + column}"
    else:
        return "Ввод данных не верный."


def print_game_field():
    game_field_result = "Формат ввода: 1а\n"
    game_field_result += f"\t\ta\t\tb\t\tc\n"
    for key, value in game_field.items():
        game_field_result += f"{key}\t\t{value[col_A]}\t\t{value[col_B]}\t\t{value[col_C]}\n"
    game_field_result += "\n"
    return game_field_result


def check_empty_symbols():
    empty_symbols = 0
    for dat in game_field.values():
        for d in dat.values():
            if d == empty_dot:
                empty_symbols += 1
    return empty_symbols

