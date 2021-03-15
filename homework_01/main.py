"""
Домашнее задание №1
Функции и структуры данных
"""

<<<<<<< HEAD

=======
>>>>>>> 15f3d3b4d5158969d2adf3cd7e56768ce2987b1d
def power_numbers(NumList):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
<<<<<<< HEAD

    return [i**i if isinstance(i, int) else i for i in NumList]
=======
    
    return [i**i if isinstance(i,int) else i for i in NumList]
>>>>>>> 15f3d3b4d5158969d2adf3cd7e56768ce2987b1d

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
<<<<<<< HEAD

=======
>>>>>>> 15f3d3b4d5158969d2adf3cd7e56768ce2987b1d
    return []
