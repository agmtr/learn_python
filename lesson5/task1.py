#!/usr/bin/env python3

"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка. """


with open("task1.txt", "w") as my_file:
    print("Вводите строки разделенные клавишей Enter, для выхода оставьте пустую строку и нажмите Enter:")
    while True:
        user_input = input()
        if user_input:
            print(user_input, file=my_file)
        else:
            break
