#!/usr/bin/env python3

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict. """

user_input = int(input("Введите номер месяца (от 1 до 12): "))
if user_input not in range(1, 13):
    print("Неверный ввод!")
    exit()

# Решение через list
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
index = user_input // 3 % 4
print("# list", seasons_list[index], sep="\n")

# Решение через dict
seasons_dict = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for season, month in seasons_dict.items():
    if user_input in month:
        print("# dict", season, sep="\n")
