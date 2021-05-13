# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict
from collections import deque

num: int = int(input('Введите кол-во предприятий '))
data = []
for i in range(num):
    name = input('Введите название предприятия ')
    for j in range(1, 5):
        profit_for_quarter = float(input(f'Введите прибыль за {j}-й квартал '))
        data.append((name, profit_for_quarter))
sum_profit = 0
firms = defaultdict(float)
for name, profit in data:
    firms[name] += profit
    sum_profit += profit
average = sum_profit / num
more_average = deque()
less_average = deque()
for keys in firms:
    if firms[keys] > average:
        more_average.appendleft(keys)
    if firms[keys] < average:
        less_average.appendleft(keys)
print(f'Средняя прибыль для всех предприятий = {average}')
print(f'Список предприятий с прибылью больше средней: {more_average}')
print(f'Список предприятий с прибылью меньше средней: {less_average}')
