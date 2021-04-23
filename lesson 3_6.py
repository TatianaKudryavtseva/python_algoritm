# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 30
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
index_max, index_min = 0, 0
sum_element = 0
for i in range(1, len(array)):
    if array[i] > array[index_max]:
        index_max = i
    if array[i] < array[index_min]:
        index_min = i
if index_max < index_min:
    for i in range(index_max + 1, index_min):
        sum_element += array[i]
else:
    for i in range(index_min + 1, index_max):
        sum_element += array[i]
print(sum_element)
