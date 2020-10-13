#!/usr/bin/env python3

"""5. Программа запрашивает у пользователя строку чисел,
разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но
если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после
нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
программу."""

num_sum = 0


def my_func(args):
    global num_sum
    for num in args:
        num_sum += int(num)
    print(num_sum)
    return num_sum


while True:
    user_input = input("Введите список чисел разделенных пробелом или q для завершения: ")
    nums = user_input.split(" ")
    if "q" in user_input:
        nums.remove("q")
        my_func(nums)
        break
    else:
        my_func(nums)










# def my_sum():
#     sum_res = 0
#     ex = False
#     while ex == False:
#         number = input('Input numbers or Q for quit - ').split()
#
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'q' or number[el] == 'Q':
#                 ex = True
#                 break
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
#
#
# my_sum()