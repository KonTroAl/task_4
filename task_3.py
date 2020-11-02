"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile, timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main(enter_num):
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


enter_num = 4567897465

cProfile.run('main(enter_num)')
cProfile.run('revers(enter_num)')
cProfile.run('revers_2(enter_num)')
cProfile.run('revers_3(enter_num)')

print(timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num"))
print(timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num"))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num"))

"""Первая реализация самая медленная в связи с перебором каждого элемента введеннго числа
Вторая реализация использует цикл while, что позволяет ускорить работу программы, но всё равно происходит перебор
каждого элемента
Третья реализация самая быстра в связи с тем, что использует внутренню функцию среза списка, что многократно ускоряет
работу программы"""
