# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите 3 разных числа')
a, b, c = input(), input(), input()
if a < b:
    if b > c:
        if c > a:
            print(f'{c} является средним числом')
        else:
            print(f'{a} является средним числом')
    else:
        print(f'{b} является средним числом')
else:
    if c > a:
        print(f'{a} является средним числом')
    else:
        if b > c:
            print(f'{b} является средним числом')
        else:
            print(f'{c} является средним числом')