# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».
import timeit
import cProfile


def sieve(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    return [item for item in a if item != 0]


def el_sieve(el):
    lst = sieve(el * 20)
    return lst[el - 1]


print(timeit.timeit('el_sieve(5)', number=1000, globals=globals()))  # 0.0296296
print(timeit.timeit('el_sieve(10)', number=1000, globals=globals()))  # 0.0584182
print(timeit.timeit('el_sieve(20)', number=1000, globals=globals()))  # 0.12941260000000004
print(timeit.timeit('el_sieve(40)', number=1000, globals=globals()))  # 0.2704581
print(timeit.timeit('el_sieve(80)', number=1000, globals=globals()))  # 0.5839798
print(timeit.timeit('el_sieve(160)', number=1000, globals=globals()))  # 1.1961597

cProfile.run('el_sieve(1000)')


# 6 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 lesson 4_2.py:11(sieve)
#         1    0.001    0.001    0.001    0.001 lesson 4_2.py:24(<listcomp>)
#         1    0.000    0.000    0.008    0.008 lesson 4_2.py:27(el_sieve)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def prime(n):
    lst = [2]
    count = 0
    for i in range(3, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
                if count > 1:
                    break
        if count == 1:
            lst.append(i)
        count = 0
    return lst


def el_prime(el):
    lst = prime(el * 20)
    return lst[el - 1]


print(timeit.timeit('el_prime(5)', number=1000, globals=globals()))  # 0.12751019999999968
print(timeit.timeit('el_prime(10)', number=1000, globals=globals()))  # 0.4025462000000002
print(timeit.timeit('el_prime(20)', number=1000, globals=globals()))  # 1.3614330000000003
print(timeit.timeit('el_prime(40)', number=1000, globals=globals()))  # 4.617886
print(timeit.timeit('el_prime(80)', number=1000, globals=globals()))  # 17.0248578
print(timeit.timeit('el_prime(160)', number=1000, globals=globals()))  # 63.99669680000001

cProfile.run('el_prime(1000)')

# 2266 function calls in 2.201 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.201    2.201 <string>:1(<module>)
#         1    2.201    2.201    2.201    2.201 lesson 4_2.py:55(prime)
#         1    0.000    0.000    2.201    2.201 lesson 4_2.py:70(el_prime)
#         1    0.000    0.000    2.201    2.201 {built-in method builtins.exec}
#      2261    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
