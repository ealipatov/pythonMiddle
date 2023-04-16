# def sum_x2(num1, num2):
#     return (num1 + num2) * 2
#
# sum_x2_lambda = lambda num1, num2: (num1 + num2) * 2
#
#
# print(sum_x2(3, 2))
# print(sum_x2_lambda(3, 2))

def filter_function(number):
    return number % 2 == 0


numbers = list(range(1, 100))
print(numbers)

# Запись функции filter  помощью лямбды и простой функции
numbers_2 = list(filter(lambda element: element % 2 == 0, numbers))
numbers_3 = list(filter(filter_function, numbers))
print(numbers_2)

# Использование функции sorted
print(sorted(numbers_3, reverse=True))

# Используем map
print(list(map(lambda number: number + 1, numbers)))
