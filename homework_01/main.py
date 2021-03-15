#!/usr/bin/python3

"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*num_list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    Result = list()
    for i in num_list:
        if isinstance(i, int):
            Result.append(i*i)
        else:
            Result.append(i)
    return Result

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(NumList, condition):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if condition == ODD:
        Result = list(filter(lambda i: i % 2 != 0, NumList))

    if condition == EVEN:
        Result = list(filter(lambda i: i % 2 == 0, NumList))

    if condition == PRIME:
        Result = list()
        for i in NumList:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                Result.append(i)

    return Result
