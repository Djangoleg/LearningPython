from itertools import islice


def odd_nums(number):
    """
    Генератор нечётных чисел от 1 до n (включительно),
    не используя ключевое слово yield
    :param number:
    :return:
    """
    return (num for num in range(1, number + 1, 2))


# Поверка.
test_number = 15
odd_to_15 = odd_nums(test_number)

# Можно как в закоментированном коде, вызывая ф-ию Next
"""for x in range(1, test_number + 1):
    if x % 2 != 0:
        print(next(odd_to_15), end=", ")"""

print(*islice(odd_to_15, test_number))

