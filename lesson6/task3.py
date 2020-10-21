#!/usr/bin/env python3

"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Worker):
    position: str
    wage: int
    bonus: int

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname)
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


developer = Position("John", "Doe", "Developer", 100000, 5000)
developer.get_full_name()
print(developer.position)
developer.get_total_income()
