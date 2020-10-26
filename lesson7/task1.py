#!/usr/bin/env python3

"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д. """


class Matrix:
    matrix: list

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        string = ""
        for line in self.matrix:
            string += " ".join(map(str, line)) + "\n"
        return string

    def __add__(self, other):
        return Matrix([list(map(sum, zip(*i))) for i in zip(self.matrix, other.matrix)])


one = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
two = Matrix([[1, 2, 10], [1, 2, 5], [1, 2, 4]])
print(one)
print(two)

three = one + two
print(three)
