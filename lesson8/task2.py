#!/usr/bin/env python3

"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        dividend = int(input("Введите делимое: "))
        divider = int(input("Введите делитель: "))
        if divider == 0:
            raise OwnError("На ноль делить нельзя!")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f"Все хорошо. Результат: {dividend / divider}")
