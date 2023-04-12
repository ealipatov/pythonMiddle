ZNAK = ["+", "-", "/", "*"]

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
    for cont, operation in enumerate(operation_log):
        print(f"{cont + 1}: {operation}")


def run():
    while True:
        print(f"Меню: {menu}")
        selected_menu = int(input(f"Выберете пункт меню: "))
        if selected_menu == 1:
            calculate()
        elif selected_menu == 2:
            show_history_operation()
        elif selected_menu == 3:
            print("Работа завершена.")
            break
        else:
            print("Ошибка ввода.")

run()