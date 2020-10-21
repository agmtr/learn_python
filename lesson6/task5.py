#!/usr/bin/env python3

"""5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. """

from lesson6.task4 import *

audi = WorkCar("audi")
print(audi.name, audi.color)
audi.show_speed()
audi.go(40)
audi.show_speed()
audi.stop()
audi.show_speed()
audi.go(60)
audi.show_speed()

bmv = PoliceCar("bmv")
print(bmv.name, bmv.color)
bmv.go(80)
bmv.show_speed()
print(f"{bmv.name} is police: {bmv.is_police}")

vw = TownCar("vw", "blue")
print(vw.name, vw.color)
print(f"{vw.name} is police: {bmv.is_police}")
vw.go(80)
vw.show_speed()
vw.turn("налево")

ferrari = SportCar("ferrari", "red")
print(ferrari.name, ferrari.color)
ferrari.go(200)
ferrari.show_speed()
