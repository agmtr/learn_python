#!/usr/bin/env python3

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. """

with open("task2.txt") as my_file:
    for idx, line in enumerate(my_file, 1):
        print("Line {} has {} words".format(idx, len(line.split())))
