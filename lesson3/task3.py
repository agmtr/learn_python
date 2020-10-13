#!/usr/bin/env python

"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов."""


def my_func(num1, num2, num3):
    nums = list(locals().values())
    nums.remove(min(nums))
    return sum(nums)


var1, var2, var3 = input("Введите 3 числа через запятую: ").split(",")
print(my_func(int(var1), int(var2), int(var3)))
