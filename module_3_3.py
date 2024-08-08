# module_3_3
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Примеры вызовов функции
print_params()  # Все параметры по умолчанию
print_params(b=25)  # Переопределяем только 'b'
print_params(c=[1, 2, 3])  # Переопределяем только 'c'

# Список
values_list = [10, "другая строка", False]

# Словарь
values_dict = {'a': 100, 'b': 'новая строка', 'c': [4, 5, 6]}

# Распаковка списка
print_params(*values_list)

# Распаковка словаря
print_params(**values_dict)

# Список с двумя элементами
values_list_2 = [54.32, 'Строка']

# Распаковка с дополнительным параметром
print_params(*values_list_2, 42)