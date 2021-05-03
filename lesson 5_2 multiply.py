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
num_1 = deque(x)
num_2 = deque(y)
sum_number, sum_deque = deque(), deque()
multiply_deque, num_multiply_1, num_multiply_2 = deque(), deque(), deque()
if len(num_1) < len(num_2):
    num_1, num_2 = num_2, num_1
for j in range(len(num_1)-1, -1, -1):
    num = hex_number[str(num_2[-1])] * hex_number[str(num_1[j])]
    num_multiply_1.appendleft(num)
for i in range(len(num_2)-2, -1, -1):
    for k in range(i+1):
        num_multiply_2.append(0)
    for j in range(len(num_1)-1, -1, -1):
        num = hex_number[str(num_2[i])] * hex_number[str(num_1[j])]
        num_multiply_2.appendleft(num)
    if len(num_multiply_1) > len(num_multiply_2):
        while len(num_multiply_2) < len(num_multiply_1):
            num_multiply_2.appendleft(0)
    else:
        while len(num_multiply_1) < len(num_multiply_2):
            num_multiply_1.appendleft(0)
    for el in range(len(num_multiply_1)):
        sum_number = num_multiply_1[el] + num_multiply_2[el]
        sum_deque.append(sum_number)
for j in range(len(sum_deque)-1, -1, -1):
    if j == len(sum_deque)-1:
        rest = sum_deque[j] % 16
        multiply_deque.appendleft(int_number[rest])
    else:
        if j != 0:
            if sum_deque[j+1] > 15:
                rest = (sum_deque[j] + (sum_deque[j+1] // 16)) % 16
                multiply_deque.appendleft(int_number[rest])
            if sum_deque[j+1] <= 15:
                rest = sum_deque[j] % 16
                multiply_deque.appendleft(int_number[rest])
        else:
            if sum_deque[j+1] > 15:
                num_int = (sum_deque[j] + (sum_deque[j+1] // 16)) // 16
                rest = (sum_deque[j] + (sum_deque[j+1] // 16)) % 16
                multiply_deque.appendleft(int_number[rest])
                if num_int > 0:
                    multiply_deque.appendleft(int_number[num_int])
            if sum_deque[j + 1] <= 15:
                num_int = sum_deque[j] // 16
                rest = sum_deque[j] % 16
                multiply_deque.appendleft(int_number[rest])
                if num_int > 0:
                    multiply_deque.appendleft(int_number[num_int])

print(f'произведение чисел равно{multiply_deque}')