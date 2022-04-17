# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
# числа деления клеток соответственно.


class Cell:
    def __init__(self, cells_count):
        self.cells_count = cells_count

    @property
    def cells_count(self):
        return self.__cells_count

    @cells_count.setter
    def cells_count(self, cells_count):
        if not isinstance(cells_count, int) or cells_count <= 0:
            raise ValueError('Initialize error: cells count must be positive int value')
        self.__cells_count = cells_count

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        if self.cells_count < other.cells_count:
            print('Subtraction error: right argument is greater than left')
        else:
            return Cell(self.cells_count - other.cells_count)

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __floordiv__(self, other):
        return Cell(self.cells_count // other.cells_count)

    def make_order(self, cells_in_row_count):
        if not (1 < cells_in_row_count <= self.__cells_count):
            raise ValueError('Cells count in row must be: 1 < x <= cells count')
        for _ in range(self.cells_count // cells_in_row_count):
            print('*' * cells_in_row_count)
        print('*' * (self.cells_count % cells_in_row_count))


cell_1 = Cell(50)
cell_2 = Cell(100)
cell_3 = cell_1 + cell_2
print(cell_3.cells_count)
cell_3 = cell_1 - cell_2
cell_3 = cell_2 - cell_1
print(cell_3.cells_count)
cell_3 = cell_1 * cell_2
print(cell_3.cells_count)
cell_3 = cell_2 // cell_1
print(cell_3.cells_count)
cell_2.make_order(33)
