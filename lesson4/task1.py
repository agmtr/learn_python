#!/usr/bin/env python3

"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. """

from sys import argv as std_argv


def salary(hours, rate, award):
    return hours * rate + award


def main():
    try:
        file, hours, rate, award = std_argv
    except ValueError:
        print("Неверные аргументы")
        exit()
    return print(salary(int(hours), int(rate), int(award)))


main()
