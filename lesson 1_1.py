# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/198z3I3W7rAAdba4qgvsbHFFD0o5rv6x2/view?usp=sharing - алгоритмы

num = int(input("Введите трехзначное число"))
sum_digit = num // 100 + num // 10 % 10 + num % 10
multiply_digit = (num // 100) * (num // 10 % 10) * (num % 10)
print(f'Сумма цифр = {sum_digit}')
print(f'Произведение цифр = {multiply_digit}')
