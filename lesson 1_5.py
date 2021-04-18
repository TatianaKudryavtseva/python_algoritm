# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

# вариант 1
letter_1 = input('Введите первую букву алфавита в нижнем регистре')
letter_2 = input('Введите вторую букву алфавита в нижнем регистре')
num_1 = ord(letter_1) - ord('a') + 1
num_2 = ord(letter_2) - ord('a') + 1
num_between = num_2 - num_1 - 1
print(f'буква {letter_1} стоит на {num_1} месте алфавита')
print(f'буква {letter_2} стоит на {num_2} месте алфавита')
print(f'между буквой {letter_1} и буквой {letter_2} - {num_between} букв')

# вариант 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_1 = input('Введите первую букву алфавита')
letter_2 = input('Введите вторую букву алфавита')
num_1 = alphabet.index(letter_1) + 1
num_2 = alphabet.index(letter_2) + 1
num_between = num_2 - num_1 - 1
print(f'буква {letter_1} стоит на {num_1} месте алфавита')
print(f'буква {letter_2} стоит на {num_2} месте алфавита')
print(f'между буквой {letter_1} и буквой {letter_2} - {num_between} букв')
