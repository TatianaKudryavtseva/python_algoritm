# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a, b = 5, 6

# оператор И
print(f'побитовый "И" = {a & b}')

# оператор ИЛИ
print(f'побитовый "ИЛИ" = {a | b}')

# оператор НЕ
print(f'побитовый "НЕ" = {~a}')
print(f'побитовый "НЕ" = {~b}')

# оператор XOR
print(f'побитовый "XOR" = {a ^ b}')

# побитовый сдвиг вправо
print(f'побитовый сдвиг вправо = {a >> 2}')

# побитовый сдвиг влево
print(f'побитовый сдвиг влево = {a << 2}')