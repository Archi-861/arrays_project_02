from random import randint

array1 = []
array2 = []

num1 = int(input('Введите количество элементов первого массива >> '))
num2 = int(input('Введите количество элементов второго массива >> '))

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
    array_res = []
    if check_array(array1, array2) == True:
        array_res = [array1[i] + array2[i] for i in range(len(array1))]
    else:
        array_res = 'Заданные массивы имеют разное количество элементов'
    return array_res

print(array1)
print(array2)
print(sum_arrays(array1, array2))
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