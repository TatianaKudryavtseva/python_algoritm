# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# # Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

lst = []
m = int(input('введите число '))
for k in range(2 * m + 1):
    lst.append(random.randint(0, 50))
print(lst)


def median_sort(array):
    result = []
    array_copy = array.copy()
    while len(result) <= len(array) // 2:
        num = min(array_copy)
        result.append(num)
        array_copy.remove(num)
    return result[-1]


def median(arr):
    for i in range(len(arr)):
        el = arr[i]
        count = 0
        for j in range(len(arr)):
            if arr[j] <= el and i != j:
                count += 1
        if count == len(arr) // 2:
            break
    return el
# не всегда срабатывает при большом количестве повторений


print(f'Медиана массива {median_sort(lst)}')
print(f'Медиана массива {median(lst)}')
