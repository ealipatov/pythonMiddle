numbers = [1, 2, 3]


def get_from_numbers(index):
    try:
        return numbers[index]
    except Exception as e:
        return 0


print (get_from_numbers(0))
