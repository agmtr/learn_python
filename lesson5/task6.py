#!/usr/bin/env python3

"""6. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста."""

import json

with open("task6.txt") as firms_file:
    profit = {}
    for line in firms_file:
        name, ownership, proceeds, costs = line.split()
        profit[name] = int(proceeds) - int(costs)
    with_profit = {k: v for k, v in profit.items() if v > 0}
    average_profit = {"average_profit": sum([v for v in with_profit.values()]) / len(with_profit)}
    result = [profit, average_profit]

with open("task6_result.txt", "w") as result_file:
    json.dump(result, result_file)
