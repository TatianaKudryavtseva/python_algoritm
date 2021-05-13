# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры

n = int(input('Введите количество элементов '))
element = 1
sum_element = 0
for i in range(n):
    sum_element += element
    element /= -2
    i += 1
print(f'Сумма элементов = {sum_element}')
