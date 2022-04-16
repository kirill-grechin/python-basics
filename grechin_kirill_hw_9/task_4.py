# 4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('car go')

    def stop(self):
        print('car stop')

    def turn(self, direction):
        print(f'car turn to {direction}')

    def show_speed(self):
        print(f'car speed: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'over speed! car speed: {self.speed}')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'over speed! car speed: {self.speed}')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


car = Car(100, 'red', 'bmw', False)
print(car.speed, car.color, car.name, car.is_police, sep='\n')
car.go()
car.show_speed()
car.turn('right')
car.stop()

town_car = TownCar(70, 'black', 'mercedes', False)
town_car.show_speed()
town_car.speed = 59
town_car.show_speed()

work_car = WorkCar(45, 'blue', 'nissan', False)
work_car.show_speed()
work_car.speed = 35
work_car.show_speed()
