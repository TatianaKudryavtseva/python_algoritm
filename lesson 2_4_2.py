# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры

def func(a, b):
    if b == 1:
        return a
    return a + func(a / -2, b - 1)


el = 1
n = int(input('Введите количество элементов '))
res = func(el, n)
print(res)
