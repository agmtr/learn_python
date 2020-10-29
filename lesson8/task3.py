#!/usr/bin/env python3

"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
только числами. Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводеп ользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться. """


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        user_input = input("Введите число или stop для выхода: ")
        if user_input == "stop":
            break
        if not user_input.isdigit():
            raise OwnError("Вы ввели не число!")
    except OwnError as err:
        print(err)
    else:
        my_list.append(int(user_input))
        print(my_list)
