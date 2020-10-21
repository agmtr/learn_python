#!/usr/bin/env python3

"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт. """

from time import sleep


class TrafficLight:
    __color = str

    def running(self):
        modes = {"red": 7, "yellow": 2, "green": 10}
        for mode, timer in modes.items():
            self.__color = mode
            print(f"\nswitch to {self.__color}")
            for i in range(timer, 0, -1):
                print(i, end="..")
                sleep(1)


tl = TrafficLight()
tl.running()
