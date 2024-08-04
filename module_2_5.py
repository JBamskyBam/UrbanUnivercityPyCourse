# module_2_5

def get_matrix(n, m, value):
    # Проверка на данных на то что они больше либо равны 0
    if n <= 0 or m <= 0:
        return []

    matrix = []  # Создание пустого списка для матрицы
    for i in range(n):  # Внешний цикл для строк в пределах значения n
        list_ = []  # Создаем пустой список для строки n
        for j in range(m):  # Внутренний цикл для столбцов в пределах значений m
            list_.append(value)  # Добавляем значение value в строку
        matrix.append(list_)  # Добавляем строку в матрицу

    return matrix  # Возвращаем полученную матрицу


# Примеры вызова функции из задания
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата в консоль
print(result1)
print(result2)
print(result3)