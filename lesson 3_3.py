# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 30
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
index_max, index_min = 0, 0
for i in range(1, len(array)):
    if array[i] > array[index_max]:
        index_max = i
    if array[i] < array[index_min]:
        index_min = i
array[index_max], array[index_min] = array[index_min], array[index_max]
print(array)