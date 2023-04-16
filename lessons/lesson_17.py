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

users_mark = {
    "иван": [
        (date_now - datetime.timedelta(days=1), 9),
        (date_now - datetime.timedelta(days=3), 8),
        (date_now - datetime.timedelta(days=5), 7)
    ]
}

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


def check_is_user_registered():
    login = False

    while not login:
        login = check_login()

    while not check_password(login):
        print("Неверный пароль")

    return login.lower()


def run_program():
    user_access = users[check_is_user_registered()][1]
    print(f"Ваш уровень доступа: {user_access}")
    if user_access == ADMIN_ACCESS:
        pass
    elif user_access == STUDENT_ACCESS:
        pass


def generate_test():
    znak = ["+", "-", "*", "/"][random.randint(0, 3)]
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {znak} {num2}"
    return question, eval(question)


run_program()

print(users_mark)
