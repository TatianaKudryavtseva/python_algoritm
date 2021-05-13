# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9
import hashlib


def sub_hash(words):
    hash_full = hashlib.sha1(words.encode('UTF-8')).hexdigest()
    hash_space = hashlib.sha1(' '.encode('UTF-8')).hexdigest()
    array = []
    for i in range(len(words)):
        letter = str(words[i])
        letter_hash = hashlib.sha1(letter.encode('UTF-8')).hexdigest()
        if letter_hash not in array and letter_hash != hash_full and letter_hash != hash_space:
            array.append(str(letter_hash))
        for j in range(len(words), i, -1):
            if i != j:
                letter = str(words[i:j])
                letter_hash = hashlib.sha1(letter.encode('UTF-8')).hexdigest()
                if letter_hash not in array and letter_hash != hash_full and letter_hash != hash_space:
                    array.append(str(letter_hash))
    return len(array)


phrase = input('Введите фразу ')
print(sub_hash(phrase))