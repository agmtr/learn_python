#!/usr/bin/env python3

"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """


class Complex:
    real: float
    imag: float

    def __init__(self, real: float, imag: float = 0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"Complex{self.real, self.imag}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: 'Complex'):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: 'Complex'):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)


one = Complex(2, 3)
two = Complex(4, 5)

print(one + two)
print(one * two)
