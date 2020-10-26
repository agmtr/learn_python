#!/usr/vib/env python3

"""3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В
его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****. """


class Cell:
    quantity: int

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if isinstance(other, Cell) and self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return f"Невозможно выполнить операцию"

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.quantity // other.quantity)

    def make_order(self, count):
        a = self.quantity // count
        b = self.quantity % count
        return ("*" * count + "\n") * a + ("*" * b + "\n")


one = Cell(18)
two = Cell(10)

print(one + two)
print(one - two)
print(one * two)
print(one / two)

print(one.make_order(5))
