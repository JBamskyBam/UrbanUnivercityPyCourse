# module_3_5

def get_multiplied_digits(number):
    # Преобразуем переданное число в строку для обработки его цифр
    str_number = str(number)

    # Проверяем, состоит ли строка из более чем одной цифры
    if len(str_number) > 1:
        # Извлекаем первую цифру и преобразуем её в целое число
        first = int(str_number[0])

        # Рекурсивно вызываем функцию для оставшейся части строки
        # (все цифры, кроме первой) и перемножаем её с первой цифрой
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если только одна цифра, тогда возвращаем её как целое число
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)
