from math import inf
def divide():
    first = int(input('Введите делитель: '))
    second = int(input('Введите знаменатель: '))
    if second != 0:
        return 'Результат деления: ', first / second
    else:
        return inf


