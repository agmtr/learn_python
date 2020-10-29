#!/usr/bin/env python3

"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


class Date:
    date: str

    def __init__(self, date):
        Date.date = date

    @classmethod
    def extract(cls):
        return list(map(int, cls.date.split("-")))

    @staticmethod
    def validation(date):
        Date(date)
        day, month, year = Date.extract()
        if 1 <= day <= 31 and 1 <= month <= 12 and 1970 <= year <= 2999:
            print("Дата верна")
        else:
            print("Дата некорректна")


Date.validation("30-10-2020")
Date.validation("32-10-2020")
Date.validation("30-13-2020")
Date.validation("30-12-1000")
