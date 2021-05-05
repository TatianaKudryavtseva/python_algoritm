# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import sys

num = input('Введите натуральное число ')
sum_even, sum_uneven = 0, 0
for i in num:
    if int(i) % 2 == 0:
        sum_even += 1
    else:
        sum_uneven += 1
print(f'Число {num} содержит {sum_even} четных цифр, {sum_uneven} нечетных цифр')


lst_even, lst_uneven = [], []
for j in num:
    if int(j) % 2 == 0:
        lst_even.append(j)
    else:
        lst_uneven.append(j)
print(f'Число {num} содержит {len(lst_even)} четных цифр, {len(lst_uneven)} нечетных цифр')


num_dict = {'even': 0, 'uneven': 0}
for el in num:
    if int(el) % 2 == 0:
        num_dict['even'] += 1
    else:
        num_dict['uneven'] += 1
print(f'Число {num} содержит {num_dict["even"]} четных цифр, {num_dict["uneven"]} нечетных цифр')
print(sys.getsizeof(num_dict["even"]))
print(sys.getsizeof(num_dict["uneven"]))
print(sys.getsizeof(num_dict))

# Windows 10 64 bit, Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]
# Для числа 34560
# Для первого варианта с увеличением счетчика - 160 байт, для варианта со списками - 530 байт,
# для варианта со словарем - 336 байт
# Вариант со счетчиком лучше, т.к счетчик является целым числом и не ссылается на другие объекты.

