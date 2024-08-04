# homework5
immutable_var = (0, 1, 2, 3, 4, 5)
print(immutable_var)
# immutable_var.append(6)
# попытка изменить кортеж, а именно добавить цифру "6" не получилась и вызывает ошибку, так как кортеж это неизмениемая
# структура, но если например в кортеже будет присутствовать список то его наполнение можно будет изменить.
mutable_list = [1993, 'год рождения', 'месяц рождения', 'день рождения']
print(mutable_list)
mutable_list.append('дата свадьбы')
print(mutable_list)
mutable_list.extend('много букв')
print(mutable_list)
mutable_list.remove(1993)
print(mutable_list)

