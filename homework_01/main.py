"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(NumList):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [i*i if isinstance(i, int) else i for i in NumList]

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
        result = list(filter(lambda i: i % 2 != 0, NumList))
    
    if condition == EVEN:
        result = list(filter(lambda i: i % 2 == 0, NumList))

    return result
