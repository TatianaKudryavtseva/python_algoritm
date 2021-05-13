#Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
new_array = list(set(array))
sum_max = array.count(new_array[0])
number = new_array[0]
for i in range(1, len(new_array)):
    if array.count(new_array[i]) >= sum_max:
        sum_max = array.count(new_array[i])
        number = new_array[i]
print(f'чаще встречается число {number}')
