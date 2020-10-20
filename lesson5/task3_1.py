#!/usr/bin/env python3

"""3.1 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников. Пример файла:

Иванов 23543.12
Петров 13749.32 """


# Создаем файл, требуется не программно, но так быстрее и интереснее =)
def gen_file(count):
    from russian_names import RussianNames
    from random import randrange

    with open("task3_1.txt", "w") as my_file:
        rn = RussianNames(count=count, name=False, patronymic=False, )
        for person in rn:
            print(f"{person} {randrange(10000, 50000)}", file=my_file)


# Для динамической генерации файла нужно активировать venv в корне проекта
# (или установить модуль russian-names через pip) и раскомментировать строку ниже
# gen_file(15)

with open("task3_1.txt") as my_file:
    employee_dict = {k: int(v) for k, v in [line.split() for line in my_file]}
    employee = [name for name, salary in employee_dict.items() if salary < 20000]
    avg_salary = round(sum(employee_dict.values()) / len(employee_dict), 2)
    print(f"Оклад менее 20000 имеют: {', '.join(employee)}", f"Средний оклад: {avg_salary}", sep="\n")
