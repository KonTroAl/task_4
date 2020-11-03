"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

my_list = [1, 2, 3, 4, 5, 6]
#
# print(func_1(my_list))
# print(func_2(my_list))


print(timeit.timeit("func_1(my_list)", setup="from __main__ import func_1, my_list"))
print(timeit.timeit("func_2(my_list)", setup="from __main__ import func_2, my_list"))

"""Для оптимизации кода было решено отказаться от цикла и использовать comprehension, что ускоряет работу
программы"""