game_field = {
    "1": {
        "a": "●",
        "b": "●",
        "c": "●"
    },
    "2": {
        "a": "●",
        "b": "●",
        "c": "●"
    },
    "3": {
        "a": "●",
        "b": "●",
        "c": "●"
    }
}


def check_win():
    pass


def check_empty(row, column):
    if game_field[row][column] == "●":
        return True
    else:
        print("Выбранная ячейка занята, повторите ввод")
        return False


def check_symbol(value):
    if value == "X" or value == "O":
        return True
    else:
        print("Выбран неверный символ, повторите ввод")
        return False


def check_row(row):
    if row == "1" or row == "2" or row == "3":
        return True
    else:
        print("Такой строки нет, повторите ввод")
        return False


def check_column(column):
    if column == "a" or column == "b" or column == "c":
        return True
    else:
        print("Такой колонки нет, повторите ввод")
        return False


def check_input(dot_input):
    if len(dot_input) == 4 and dot_input[2] == "-":
        column = dot_input.split("-")[0][1]
        row = dot_input.split("-")[0][0]
        value = dot_input.split("-")[1]

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
        print(f"{key}\t\t{value['a']}\t\t{value['b']}\t\t{value['c']}\n")
    print("\n")


def run_game():
    print("Игра крестики-нолики")
    print_game_field()


run_game()
# game_field["1"]["a"] = "X"
player_turn()
player_turn()
