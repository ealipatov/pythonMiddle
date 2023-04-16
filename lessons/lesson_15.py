
# def sum_x2(num1, num2):
#     return (num1 + num2) * 2
#
# sum_x2_lambda = lambda num1, num2: (num1 + num2) * 2
#
#
# print(sum_x2(3, 2))
# print(sum_x2_lambda(3, 2))

numbers = list(range(1, 100))

print(numbers)

numbers_2 = list(filter(lambda element: element % 2 == 0, numbers))
print(numbers_2)