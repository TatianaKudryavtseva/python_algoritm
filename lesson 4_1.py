# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры
import timeit
import cProfile
import sys

sys.setrecursionlimit(1500)


# Цикл
def func_sum_loop(n):
    element, sum_element = 1, 0
    for i in range(n):
        sum_element += element
        element /= -2
    return sum_element


print(timeit.timeit('func_sum_loop(5)', number=1000, globals=globals()))  # 0.0008776999999999952
print(timeit.timeit('func_sum_loop(10)', number=1000, globals=globals()))  # 0.0013931999999999972
print(timeit.timeit('func_sum_loop(20)', number=1000, globals=globals()))  # 0.0024845999999999965
print(timeit.timeit('func_sum_loop(40)', number=1000, globals=globals()))  # 0.004674299999999999
print(timeit.timeit('func_sum_loop(80)', number=1000, globals=globals()))  # 0.008113199999999994
print(timeit.timeit('func_sum_loop(160)', number=1000, globals=globals()))  # 0.015241899999999996
print(timeit.timeit('func_sum_loop(320)', number=1000, globals=globals()))  # 0.03385859999999999
print(timeit.timeit('func_sum_loop(640)', number=1000, globals=globals()))  # 0.0621333
print(timeit.timeit('func_sum_loop(1280)', number=1000, globals=globals()))  # 0.12571080000000004
print(timeit.timeit('func_sum_loop(2560)', number=1000, globals=globals()))  # 0.26291210000000004

cProfile.run('func_sum_loop(1000)')


# 4 function calls in 0.011 seconds

#  Ordered by: standard name

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#     1    0.010    0.010    0.010    0.010 lesson 4_1.py:13(func_sum_loop)
#     1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Рекурсия
def func(a, b):
    if b == 1:
        return a
    return a + func(a / -2, b - 1)


print(timeit.timeit('func(1, 5)', number=1000, globals=globals()))  # 0.000756699999999999
print(timeit.timeit('func(1, 10)', number=1000, globals=globals()))  # 0.0015102999999999922
print(timeit.timeit('func(1, 20)', number=1000, globals=globals()))  # 0.003338699999999986
print(timeit.timeit('func(1, 40)', number=1000, globals=globals()))  # 0.006904500000000008
print(timeit.timeit('func(1, 80)', number=1000, globals=globals()))  # 0.013651400000000008
print(timeit.timeit('func(1, 160)', number=1000, globals=globals()))  # 0.028310000000000002
print(timeit.timeit('func(1, 320)', number=1000, globals=globals()))  # 0.05803760000000002

cProfile.run('func(1, 1000)')


# 1003 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1000/1    0.001    0.000    0.001    0.001 lesson 4_1.py:33(func)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Массив и функция
def func_sum(n):
    el = 1
    lst = []
    for i in range(n):
        lst.append(el)
        el /= -2
    return sum(lst)


print(timeit.timeit('func_sum(5)', number=1000, globals=globals()))  # 0.0009799999999999809
print(timeit.timeit('func_sum(10)', number=1000, globals=globals()))  # 0.0016076999999999897
print(timeit.timeit('func_sum(20)', number=1000, globals=globals()))  # 0.002657699999999985
print(timeit.timeit('func_sum(40)', number=1000, globals=globals()))  # 0.0050034999999999386
print(timeit.timeit('func_sum(80)', number=1000, globals=globals()))  # 0.009460800000000047
print(timeit.timeit('func_sum(160)', number=1000, globals=globals()))  # 0.018902299999999927
print(timeit.timeit('func_sum(320)', number=1000, globals=globals()))  # 0.038109199999999954
print(timeit.timeit('func_sum(640)', number=1000, globals=globals()))  # 0.07671680000000003
print(timeit.timeit('func_sum(1280)', number=1000, globals=globals()))  # 0.15054960000000006
print(timeit.timeit('func_sum(2560)', number=1000, globals=globals()))  # 0.2964452000000001

cProfile.run('func_sum(1000)')

# 100005 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.025    0.025 <string>:1(<module>)
#         1    0.018    0.018    0.024    0.024 lesson 4_1.py:72(func_sum)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#    100000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Наблюдается линейная вычислительная сложность
# для данной задачи лучше вариант 1 с постепенным складыванием элементов. Рекурсия выигрывает
# максимум до 10 элемента, так же ограничения на глубину рекурсии. 3-й вариант с формированием массива и
# использованием встроенной функции sum также медленнее.
