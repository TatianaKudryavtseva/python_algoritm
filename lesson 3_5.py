# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 30
MIN_ITEM = - 50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

new_array = []
for i in range(0, len(array)):
    if array[i] < 0:
        new_array.append(array[i])
num = 0
for i in range(1, len(new_array)):
    if new_array[i] < new_array[num]:
        num = i
print(f'максимальный отрицательный элемент {new_array[num]}, его позиция {array.index(new_array[num])}')