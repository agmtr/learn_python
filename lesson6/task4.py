#!/usr/bin/env python3

"""4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. """


class Car:
    speed = 0
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color="white"):
        self.name = name
        self.color = color

    def go(self, speed):
        self.speed = speed
        print(f"{self.name} начинает движение")

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановился")

    def turn(self, direction):
        print(f"{self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"Скорость {self.name} - {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Привышение скорости! Разрешенная скорость - 60!")
            super().show_speed()
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Привышение скорости! Разрешенная скорость - 40!")
            super().show_speed()
        else:
            super().show_speed()


class PoliceCar(Car):

    def __init__(self, name):
        super().__init__(name, "black")
        self.is_police = True
