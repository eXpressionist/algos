'''Разделяет двумерные матрицы на словари, ключ - номер строки'''
def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return dict(enumerate(matrix, 1))

'''Циклический сдвиг массива на step'''
from collections import deque
def cyclic_shift(numbers:list[int|float],step:int) -> None:
    temp = deque(numbers)
    temp.rotate(step)
    numbers[:] = [c for c in temp]
