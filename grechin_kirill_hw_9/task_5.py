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
        print('Pen drawing')


class Pencil(Stationery):
    def draw(self):
        print('Pencil drawing')


class Handle(Stationery):
    def draw(self):
        print('Handle drawing')


title = 'some_title'
Stationery(title).draw()
Pen(title).draw()
Pencil(title).draw()
Handle(title).draw()
