import random

import xlsxwriter
import datetime

ADMIN_ACCESS = "admin_access"
STUDENT_ACCESS = "student_access"

date_now = datetime.datetime.now()

users = {
    "admin": ("12345", ADMIN_ACCESS),
    "мария": ("12345", STUDENT_ACCESS),
    "иван": ("12345", STUDENT_ACCESS),
    "витя": ("12345", STUDENT_ACCESS)
}

users_mark = {}

MENU = {
    ADMIN_ACCESS: {
        1: "Просмотр статистики по предмету",
        2: "Просмотр статистики по дате",
        10: "Выход"
    },
    STUDENT_ACCESS: {
        1: "Пройти тест",
        2: "Просмотр оценок",
        10: "Выход"
    },

}


def check_login():
    login = input("Введите логин: ")
    if login.lower() in users.keys():
        return login.lower()
    else:
        print(f"Логин: {login} не найден")
        return False


def check_password(login):
    password = input("Введите пароль: ")
    if password == users[login.lower()][0]:
        print("Доступ разрешен.")
        return True
    else:
        return False


def check_user_authentication():
    login = False

    while not login:
        login = check_login()

    while not check_password(login):
        print("Неверный пароль")

    return login.lower()


def save_data():
    workbook = xlsxwriter.Workbook('test_files/students_mark.xlsx')
    bold = workbook.add_format({"bold": True})

    for user, marks in users_mark.items():
        counter = 2
        worksheet = workbook.add_worksheet(user)
        worksheet.write("A1", "Дата", bold)
        worksheet.write("B1", "Оценка", bold)

        for mark in marks:
            worksheet.write(f"A{counter}", str(mark[0])[:10])
            worksheet.write(f"B{counter}", mark[1])
            counter += 1

    workbook.close()


def start_test(login):
    right_answer = 0
    for i in range(1, 6):
        question, answer = generate_test()
        try:
            user_answer = int(input(f"Реши пример: {question} = "))
            if user_answer == answer:
                right_answer += 1
                print("Правильный ответ")
            else:
                print(f"Ошибка. Правильный ответ: {answer}")
        except Exception as error:
            print(error)
            print(" Ошибка. Введенный ответ не целое число")
    mark = right_answer * 2
    users_mark[login] = users_mark.get(login, []) + [(date_now, mark)]

    print(f"Правильных ответов: {right_answer}, оценка: {mark}")


def print_dist(dist):
    for key, value in dist.items():
        print(key, ':')
        for i in value:
            print(i)


def show_menu(user_access, login):
    while True:
        current_menu = MENU[user_access]
        print(f"\nМеню пользователя: ")
        print("=" * 80)
        for item in current_menu:
            print(f"{item}", current_menu[item])
        print("=" * 80)

        chosen_item = int(input("Выберете пункт меню: "))
        if user_access == STUDENT_ACCESS and chosen_item == 1:
            start_test(login)
        elif user_access == STUDENT_ACCESS and chosen_item == 2:
            pass
        elif user_access == ADMIN_ACCESS and chosen_item == 1:
            pass
        elif user_access == ADMIN_ACCESS and chosen_item == 2:
            pass
        elif chosen_item == 10:
            if user_access == STUDENT_ACCESS:
                save_data()
                print("данные сохранены")
            print("Работы программы завершена.")
            return
        else:
            print("Выбран некорректный пункт меню")


def run_program():
    login = check_user_authentication()
    user_access = users[login][1]
    print(f"Ваш уровень доступа: {user_access}")
    show_menu(user_access, login)


def generate_test():
    znak = ["+", "-", "*"][random.randint(0, 2)]
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {znak} {num2}"
    return question, eval(question)


run_program()
