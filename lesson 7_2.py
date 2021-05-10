# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_lst(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        for n in range(i, len(left)):
            result.append(left[n])
    if j < len(right):
        for m in range(j, len(right)):
            result.append(right[m])
    return result


def sort_merge(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left_array = sort_merge(array[:middle])
    right_array = sort_merge(array[middle:])
    return merge_lst(left_array, right_array)


lst = []
n = 10
for el in range(n):
    lst.append(random.randint(0, 50))
print(lst)
print(sort_merge(lst))
