# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    sum_digit = 0
    for j in range(i, 100):
        if j % i == 0:
            sum_digit += 1
    print(f'для числа {i} в диапазоне от 2 до 99 кратно {sum_digit} чисел')