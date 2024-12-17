from random import randint

array = []

num = int(input('Введите количество элементов массива >> '))

for i in range(num):
    a = randint(-10, 11)
    array.append(a)

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

print(array)
print(sum_1d(array))
print(prod_1d(array))
print(mean_1d(array))