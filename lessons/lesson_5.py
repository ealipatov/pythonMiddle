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
    pass


def check_empty(row, column):
    if game_field[row][column] == empty_dot:
        return True
    else:
        print("Выбранная ячейка занята, повторите ввод")
        return False


def check_symbol(value):
    allow_symbol = ["X", "O"]
    if value in allow_symbol:
        return True
    else:
        print("Выбран неверный символ, повторите ввод")
        return False


def check_row(row):
    allow_row = [row_1, row_2, row_3]
    if row in allow_row:
        return True
    else:
        print("Такой строки нет, повторите ввод")
        return False


def check_column(column):
    allow_column = [col_A, col_B, col_C]
    if column in allow_column:
        return True
    else:
        print("Такой колонки нет, повторите ввод")
        return False


def check_input(dot_input):
    if len(dot_input) == 4 and dot_input[2] == "-":
        column = dot_input.split("-")[0][1]
        row = dot_input.split("-")[0][0].lower()
        value = dot_input.split("-")[1].upper()

        if check_row(row) and check_column(column) and check_symbol(value) and check_empty(row, column):
            return [row, column, value]
    else:
        print("Ошибка ввода")
        return False


def player_turn():
    input_dot_turn(input("Сделайте ход (формат 1а-Х): "))
    print_game_field()


def input_dot_turn(dot_input):
    if check_input(dot_input):
        row, column, value = check_input(dot_input)
        game_field[row][column] = value
    else:
        player_turn()


def print_game_field():
    print(f"\t\ta\t\tb\t\tc\n")
    for key, value in game_field.items():
        print(f"{key}\t\t{value[col_A]}\t\t{value[col_B]}\t\t{value[col_C]}\n")
    print("\n")


def run_game():
    print("Игра крестики-нолики")
    print_game_field()


run_game()
# game_field["1"]["a"] = "X"
player_turn()
player_turn()
