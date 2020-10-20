#!/usr/bin/env python3

"""3.2 Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """

with open("task3_2.txt") as my_file:
    rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    content = my_file.read()
    for k, v in rus.items():
        content = content.replace(k, v)

with open("task3_2_rus.txt", "w") as rus_file:
    rus_file.writelines(content)
