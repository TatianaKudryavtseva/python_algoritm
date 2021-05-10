# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


def sort_bubble(array):
    m = len(array)
    while m > 1:
        flag = 0
        for el in range(m - 1):
            if array[el] < array[el + 1]:
                array[el], array[el + 1] = array[el + 1], array[el]
                flag = 1
        m -= 1
        if flag == 0:
            break
    return array


lst = []
n = 10
for i in range(n):
    lst.append(random.randint(-100, 100))
print(lst)
print(sort_bubble(lst))
