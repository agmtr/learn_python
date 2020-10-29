#!/usr/bin/env python3

"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП. """


class OfficeEquipment:
    vendor: str
    price: int

    def __init__(self, name, price):
        self.vendor = name
        self.price = price

    def __str__(self):
        return f"{type(self).__name__}({self.vendor})"

    def __repr__(self):
        return self.__str__()


class Printer(OfficeEquipment):
    color: bool

    def __init__(self, name, price, color=True):
        super().__init__(name, price)
        self.color = color


class Scanner(OfficeEquipment):
    dpi: int

    def __init__(self, name, price, dpi):
        super().__init__(name, price)
        self.dpi = dpi


class Copier(OfficeEquipment):
    speed: int

    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed


class QuantityError(Exception):
    def __str__(self):
        return "Неверное количество"


class Stock:
    items: dict

    def __init__(self):
        self.items = {}

    def add(self, obj: 'OfficeEquipment', quantity=1):
        if not isinstance(quantity, int):
            raise QuantityError
        self.items[obj] = quantity

    def move(self, obj: 'OfficeEquipment', dest, units=1):
        if self.items[obj] - units < 0:
            raise QuantityError
        self.items[obj] -= units
        return f"{obj}: {units} шт., перемещен в {dest}"


printer = Printer("HP", 200)
scanner = Scanner("Brother", 100, 800)
copier = Copier("Xerox", 500, 10)

print(printer)
print(scanner)
print(copier)

stock = Stock()

try:
    stock.add(printer, 2)
    stock.add(scanner, 5)
    stock.add(copier, 10)
    stock.add(printer, "test")
except QuantityError as err:
    print(err)

print(stock.items)
print(stock.move(copier, "Бухгалтерия", 3))

try:
    print(stock.move(copier, "Бухгалтерия", 20))
except QuantityError as err:
    print(err)

print(stock.items)
