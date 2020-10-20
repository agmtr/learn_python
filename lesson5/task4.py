#!/usr/bin/env python3

"""4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from random import randint

with open("task4.txt", "w") as my_file:
    content = [str(randint(1, 100)) for i in range(1, 50)]
    my_file.write(' '.join(content))

with open("task4.txt") as my_file:
    nums = [int(num) for num in my_file.read().split()]
    print(nums, f"Сумма: {sum(nums)}", sep="\n")
