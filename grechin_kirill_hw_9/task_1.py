import time


# 1. Создать класс TrafficLight (светофор):
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.__settings = {'red': 5, 'yellow': 2, 'green': 5}

    def manual_running(self, color):
        if color not in self.__settings:
            raise ValueError(f'Wrong color: "{color}"')
        if self.__color == 'red' and color != 'yellow' or \
                self.__color == 'yellow' and color != 'green' or \
                self.__color == 'green' and color != 'red':
            raise ValueError(f'Wrong color order. Current color: {self.__color}')
        self.__color = color
        self.__waiting()

    def auto_running(self):
        for color, wait_time in self.__settings.items():
            self.__color = color
            self.__waiting()

    def change_waiting_time(self, color, wait_time):
        if color not in self.__settings:
            raise ValueError(f'Wrong color {color}!')
        self.__settings[color] = wait_time

    def __waiting(self):
        print(f'{self.__color} light for {self.__settings[self.__color]} seconds.')
        time.sleep(self.__settings[self.__color])


try:
    # auto running
    traffic_light = TrafficLight()
    traffic_light.auto_running()
    traffic_light.change_waiting_time('green', 10)
    traffic_light.auto_running()

    # manual running
    traffic_light.manual_running('red')
    traffic_light.manual_running('yellow')
    traffic_light.manual_running('green')
    traffic_light.manual_running('yellow')
except ValueError as ve:
    print(ve)
