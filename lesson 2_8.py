# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите количество чисел последовательности '))
digit = int(input('Введите цифру, которую нужно считать '))
sum_digit = 0
for i in range(n):
    number = input('Введите число последовательности ')
    for j in number:
        if int(j) == digit:
            sum_digit += 1
print(sum_digit)
