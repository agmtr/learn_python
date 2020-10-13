#!/usr/bin/env python3

"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль."""


def div(dividend, divider):
    try:
        result = int(dividend) / int(divider)
    except ValueError:
        return "Неверный ввод, попройте снова"
    except ZeroDivisionError:
        return "Делитель не должен быть 0"
    else:
        return result


var1, var2 = input("Ведите делимое и делитель, разделенные запятой: ").split(",")
print(div(var1, var2))
