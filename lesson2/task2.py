#!/ysr/bin/env python3

"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input(). """

items = []
for _ in range(11):
    user_input = input("Введите новый элемент: ")
    items.append(user_input)
    if len(items) > 1:
        for index in range(1, len(items), 2):
            items[index - 1], items[index] = items[index], items[index - 1]
    print(*items)
