#!/usr/bin/env python3

"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено. """

from itertools import count, cycle


def count_func(start, stop):
    for item in count(start):
        if item > stop:
            break
        else:
            print(item)


count_func(int(input("Введите начальное число: ")), int(input("Введите конечное число: ")))


def cycle_func(my_list, iters):
    counter = 0
    for item in cycle(my_list):
        if counter >= iters:
            break
        else:
            print(item)
            counter += 1


cycle_func(['foo', 'bar'], int(input("Введите количество итераций: ")))