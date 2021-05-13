# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
int_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

x = input('введите первое шестнадцатеричное число ')
y = input('введите второе шестнадцатеричное число ')
sum_deque, num_sum = deque(), deque()
num_1 = deque(x)
num_2 = deque(y)
if len(num_1) > len(num_2):
    while len(num_2) < len(num_1):
        num_2.appendleft(0)
else:
    while len(num_1) < len(num_2):
        num_1.appendleft(0)
for i in range(len(num_1)):
    sum_number = hex_number[str(num_1[i])] + hex_number[str(num_2[i])]
    sum_deque.append(sum_number)
for j in range(len(sum_deque)-1, -1, -1):
    if j == len(sum_deque)-1:
        rest = sum_deque[j] % 16
        num_sum.appendleft(int_number[rest])
    else:
        if j != 0:
            if sum_deque[j+1] > 15:
                rest = (sum_deque[j] + (sum_deque[j+1] // 16)) % 16
                num_sum.appendleft(int_number[rest])
            if sum_deque[j+1] <= 15:
                rest = sum_deque[j] % 16
                num_sum.appendleft(int_number[rest])
        else:
            if sum_deque[j+1] > 15:
                num_int = (sum_deque[j] + (sum_deque[j+1] // 16)) // 16
                rest = (sum_deque[j] + (sum_deque[j+1] // 16)) % 16
                num_sum.appendleft(int_number[rest])
                if num_int > 0:
                    num_sum.appendleft(int_number[num_int])
            if sum_deque[j + 1] <= 15:
                num_int = sum_deque[j] // 16
                rest = sum_deque[j] % 16
                num_sum.appendleft(int_number[rest])
                if num_int > 0:
                    num_sum.appendleft(int_number[num_int])

print(f'Сумма чисел: {num_sum}')

