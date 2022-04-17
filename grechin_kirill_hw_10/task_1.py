from copy import deepcopy


# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
# виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


class Matrix:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError('Initialize error: matrix must be list')
        if len(matrix) == 0:
            raise ValueError('Initialize error: matrix not be empty')
        if sum(1 for row in matrix if isinstance(row, list)) != len(matrix):
            raise TypeError('Initialize error: matrix elements must be lists')
        if len(set([len(row) for row in matrix])) != 1:
            raise ValueError('Initialize error: matrix lens of all rows must be equal')
        self.__rows_count = len(matrix)
        self.__cols_count = len(matrix[0])
        self.__matrix = matrix

    @property
    def matrix(self):
        return deepcopy(self.__matrix)

    @property
    def rows_count(self):
        return self.__rows_count

    @property
    def cols_count(self):
        return self.__cols_count

    def __str__(self):
        return '\n'.join([''.join([f'{val:<5}' for val in row]) for row in self.__matrix])

    def __add__(self, other):
        if self.__rows_count != other.__rows_count or self.__cols_count != other.__cols_count:
            raise ValueError('Matrices for addition must be identical in size')
        return Matrix([[val_1 + val_2 for val_1, val_2 in zip(row_1, row_2)]
                       for row_1, row_2 in zip(self.__matrix, other.__matrix)])


matrix_1 = [
    [1, 2, 3, 4, 5],
    [2, 4, 7, 9, 3],
    [1, 8, 3, 3, 9]
]

matrix_2 = [
    [1, 8, 3, 3, 9],
    [1, 2, 3, 4, 5],
    [2, 4, 7, 9, 3]
]

matrix_object_1 = Matrix(matrix_1)
matrix_object_2 = Matrix(matrix_2)
matrix_object_3 = matrix_object_1 + matrix_object_2
print(matrix_object_3, matrix_object_3.cols_count, matrix_object_3.cols_count, sep='\n')
matrix_3 = matrix_object_3.matrix
matrix_3.clear()
print(matrix_3, matrix_object_3.matrix, sep='\n')
