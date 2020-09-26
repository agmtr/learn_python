#!/usr/bin/env python3

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input("Введите время в секундах: "))

hours = user_seconds // 60 // 60
minutes = user_seconds // 60 % 60
seconds = user_seconds % 60

print(f"{hours}:{minutes}:{seconds}")
