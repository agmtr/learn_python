#!/usr/bin/env python3

"""2. Реализовать функцию, принимающую несколько
параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def user(name, surname, birth_year, city, email, phone_number):
    return locals()


print(user(name="a", surname="b", birth_year=1990, city="spb", email="test", phone_number=911))
