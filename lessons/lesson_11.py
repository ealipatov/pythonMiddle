import os.path

ZNAK = ["+", "-", "/", "*"]
OPERATION_HISTORY = "operation_history.txt"

menu = {
    1: "Запустить калькулятор",
    2: "Показать историю операций",
    3: "Выход"
}

operation_log = []


def calculate():
    number1 = int(input("Введите первое значение: "))
    znak = input("Введите действие: ")
    number2 = int(input("Введите второе значение: "))

    if znak == ZNAK[0]:
        res = (f"{number1} {znak} {number2} = {number1 + number2}")
    elif znak == ZNAK[1]:
        res = (f"{number1} {znak} {number2} = {number1 - number2}")
    elif znak == ZNAK[2]:
        if number2 == 0:
            res = ("Ошибка ввода. Делить на ноль нельзя.")
        else:
            res = (f"{number1} {znak} {number2} = {number1 / number2}")
    elif znak == ZNAK[3]:
        res = (f"{number1} {znak} {number2} = {number1 * number2}")
    else:
        res = (f"Выбрано неверное действие, доступные действия: {ZNAK}")
    print(res)
    operation_log.append(res)


def show_history_operation():
    print("=" * 80)
    for cont, operation in enumerate(operation_log):
        print(f"{cont + 1}: {operation}".replace("\n", ""))
    print("=" * 80)


def read_file(file_name):
    with open(file_name) as file:
        operation_log.extend(file.readlines())  # extend - добавить элементы одного списка в другой


def write_to_file(file_name):
    with open(OPERATION_HISTORY, "w") as file:
        for operation in operation_log:
            # file.write(f"{count}: {operation}")
            file.write(operation.replace("\n", "") + "\n")


def run():
    if os.path.isfile(OPERATION_HISTORY):
        read_file(OPERATION_HISTORY)
    while True:
        print(f"Меню: {menu}")
        selected_menu = int(input(f"Выберете пункт меню: "))
        if selected_menu == 1:
            calculate()
        elif selected_menu == 2:
            show_history_operation()
        elif selected_menu == 3:
            write_to_file(OPERATION_HISTORY)
            print("Работа завершена.")
            break
        else:
            print("Ошибка ввода.")


run()
