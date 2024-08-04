# homework6
# словарь
my_dict = {'Георгий' : [1993], 'Игорь':[1980], 'Алекс':[1999]}
print(my_dict)
print(my_dict.get('Георгий'))
print(my_dict.get('Иван', 'Такого ключа нет'))
my_dict.update({'Анна':[2000], 'Сюзанна':[2001]})
print(my_dict)
a = my_dict.pop('Сюзанна')
print(a)
print(my_dict)

# множество
my_set = {1, 1, 1, 1, 1, 2, 2, 2, 22, 2, 3, 3, 3, 3, 3, 3, 22, 333, 333, 4, 4, 4, 4, 4, 4444, 4444, 4444}
print(my_set)
my_set.add(555)
my_set.add(666)
print(my_set)
my_set.discard(4444)
print(my_set)