# 1. Написать функцию, которая принимает 2 параметра: число часов и число минут и выводит число секунд на экран
def get_seconds(hours, minutes):
    seconds = ((hours * 60) + minutes) * 60
    print(seconds)


# 2. Написать функцию, которая принимает 2 параметра и возвращает список чисел от первого до второго
def get_range(from_number, to_number):
    numbers = []
    if from_number > to_number:
        from_number, to_number = to_number, from_number
    while from_number <= to_number:
        numbers.append(from_number)
        from_number += 1
    return numbers


# 3. Написать функцию, которая принимает список чисел и возвращает наибольшее из чисел, встроенные функции
# использовать нельзя
def get_max(list_numbers):
    max_number = 0
    for number in list_numbers:
        if number > max_number:
            max_number = number
    return max_number


get_seconds(2, 60)
print(get_range(25, 2))
print(get_max([23, 15, 2, 46, 33, 64, 32]))
print(get_max(get_range(20, 50)))