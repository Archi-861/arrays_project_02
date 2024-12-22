from random import randint

from logger import log_action

array1 = []
array2 = []

num1 = int(input('Введите количество элементов первого массива >> '))
value1 = int(input('Введите значение-критерий для последующего отбора первого массива >> '))
num2 = int(input('Введите количество элементов второго массива >> '))
value2 = int(input('Введите значение-критерий для последующего отбора второго массива >> '))

for i in range(num1):
    a = randint(-10, 11)
    array1.append(a)

for i in range(num2):
    a = randint(-10, 11)
    array2.append(a)

def sum_1d(array):
    summ = 0
    for i in array:
        summ += i
    return summ


def prod_1d(array):
    prod = 1
    for i in array:
        prod *= i
    return prod


def mean_1d(array):
    mean = sum_1d(array) / len(array)
    mean = round(mean, 2)
    return mean


def max_1d(array):
    max_elem = array[0]
    for i in range(len(array)):
        if array[i] > max_elem:
            max_elem = array[i]
    return max_elem


def min_1d(array):
    min_elem = array[0]
    for i in range(len(array)):
        if array[i] < min_elem:
            min_elem = array[i]
    return min_elem


def check_array(array1, array2):
    if len(array1) == len(array2):
        check = True
    else:
        check = False
    return check


def sum_arrays(array1, array2):
    name = 'sum_arrays'
    log_action(name)
    array_res = []
    if check_array(array1, array2) == True:
        array_res = [array1[i] + array2[i] for i in range(len(array1))]
    else:
        array_res = 'Заданные массивы имеют разное количество элементов'
    return array_res


def diff_arrays(array1, array2):
    name = 'diff_arrays'
    log_action(name)
    array_res = []
    if check_array(array1, array2) == True:
        array_res = [array1[i] - array2[i] for i in range(len(array1))]
    else:
        array_res = 'Заданные массивы имеют разное количество элементов'
    return array_res


def prod_arrays(array1, array2):
    name = 'prod_arrays'
    log_action(name)
    array_res = []
    if check_array(array1, array2) == True:
        array_res = [array1[i] * array2[i] for i in range(len(array1))]
    else:
        array_res = 'Заданные массивы имеют разное количество элементов'
    return array_res


def compare_arrays(array1, array2):
    name = 'compare_arrays'
    log_action(name)
    arrays_same = []
    array1_larger = []
    array2_larger = []
    if check_array(array1, array2) == True:
        for i in range(len(array1)):
            arrays_same.append(array1[i] == array2[i])
            array1_larger.append(array1[i] > array2[i])
            array2_larger.append(array1[i] < array2[i])
    else:
        print('Заданные массивы имеют разное количество элементов')

    return arrays_same, array1_larger, array2_larger


def filter_greater(array1, array2, value1, value2):
    name = 'filter_greater'
    log_action(name)
    array1_larger_filter = []
    array2_larger_filter = []
    for i in range(len(array1)):
        if array1[i] > value1:
            array1_larger_filter.append(array1[i])
    for i in range(len(array2)):
        if array2[i] > value2:
            array2_larger_filter.append(array2[i])
    return array1_larger_filter, array2_larger_filter


def filter_equal(array1, array2, value1, value2):
    name = 'filter_equal'
    log_action(name)
    array1_smaller_filter = []
    array2_smaller_filter = []
    for i in range(len(array1)):
        if array1[i] > value1:
            array1_smaller_filter.append(array1[i])
    for i in range(len(array2)):
        if array2[i] > value2:
            array2_smaller_filter.append(array2[i])
    return array1_smaller_filter, array2_smaller_filter
# print(sum_1d(array1))
# print(prod_1d(array1))
# print(mean_1d(array1))
# print(max_1d(array1))
# print(min_1d(array1))



# matrix_row = int(input("Введите количество строчек >> "))
# matrix_col = int(input("Введите количество столбцов >> "))
#
# matrix = [[randint(-10,11) for i in range(matrix_col)] for j in range(matrix_row)]
#
#
# def sum_2d(matrix):
#     summ_matr = 0
#     for row in matrix:
#         for elem in row:
#             summ_matr += elem
#     return summ_matr
#
#
# def prod_2d(matrix):
#     prod_matr = 1
#     for  row in matrix:
#         for elem in row:
#             prod_matr *= elem
#     return prod_matr
#
#
# def mean_2d(matrix):
#     lenn_matr = matrix_row * matrix_col
#     mean_matr = sum_2d(matrix) / lenn_matr
#     mean_matr = round(mean_matr, 2)
#     return mean_matr
#
#
# def max_2d(matrix):
#     max_elem_matr = 0
#     for i in range(matrix_row):
#         for j in range(matrix_col):
#             if max_elem_matr < matrix[i][j]:
#                 max_elem_matr = matrix[i][j]
#     return max_elem_matr
#
#
# def min_2d(matrix):
#     min_elem_matr = 0
#     for i in range(matrix_row):
#         for j in range(matrix_col):
#             if min_elem_matr > matrix[i][j]:
#                 min_elem_matr = matrix[i][j]
#     return min_elem_matr
#
#
# for i in matrix:
#     print(*i)
# print(sum_2d(matrix))
# print(prod_2d(matrix))
# print(mean_2d(matrix))
# print(max_2d(matrix))
# print(min_2d(matrix))