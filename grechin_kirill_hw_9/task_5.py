# 5. Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Pen is drawing')


class Pencil(Stationery):
    def draw(self):
        print('Pencil is drawing')


class Handle(Stationery):
    def draw(self):
        print('Handle is drawing')


Stationery('stationery').draw()
Pen('pen').draw()
Pencil('pencil').draw()
Handle('handle').draw()
