import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
import numpy as np  # Импорт библиотеки для работы с массивами

# Определение класса Company
class Company:
    # Инициализация объекта класса Company
    def __init__(self, name, product_name, initial_product_count, product_cost, balance, selling_price):
        # Инициализация атрибутов объекта
        self.name = name  # Название компании
        self.product_name = product_name  # Название продукта
        self.initial_product_count = initial_product_count  # Начальное количество продукта на складе
        self.product_cost = product_cost  # Себестоимость продукта
        self.balance = balance  # Баланс компании
        self.selling_price = selling_price  # Продажная цена продукта

        # Инициализация дополнительных атрибутов
        self.purchased_product_count = 0  # Количество купленных единиц продукта
        self.total_purchase_cost = 0  # Общая стоимость купленных единиц продукта
        self.total_potential_profit = 0  # Общая потенциальная прибыль
        self.net_profit = 0  # Чистая прибыль

        # Создание списков для хранения истории покупок и прибыли
        self.purchase_history = []  # История покупок
        self.profit_history = []  # История прибыли

    # Метод для покупки продукта
    def buy_product(self):
        # Проверка наличия товара на складе
        if self.initial_product_count > 0:
            # Уменьшение количества товара на складе
            self.initial_product_count -= 1
            # Уменьшение баланса на стоимость продукта
            self.balance -= self.product_cost
            # Увеличение количества купленных единиц
            self.purchased_product_count += 1
            # Обновление общей стоимости купленных единиц
            self.total_purchase_cost = self.purchased_product_count * self.product_cost
            # Обновление общей потенциальной прибыли
            self.total_potential_profit = self.purchased_product_count * self.selling_price
            # Вычисление чистой прибыли
            self.net_profit = self.total_potential_profit - self.total_purchase_cost

            # Добавление данных в историю покупок и прибыли
            self.purchase_history.append(self.purchased_product_count)
            self.profit_history.append(self.net_profit)
        else:
            # Вывод сообщения о том, что товара нет в наличии
            print("Товары закончились!")

    # Метод для вывода информации о компании
    def print_info(self):
        # Вывод разделительной линии
        print('__________________________________________')
        # Вывод информации о компании
        print('Название кампании:               ', self.name)
        print('Продукт:                         ', self.product_name)
        print('Количество на складе:            ', self.initial_product_count)
        print('Цена по себестоимости:           ', self.product_cost)
        print('Баланс:                          ', self.balance)
        print('Количество купленных единиц:     ', self.purchased_product_count)
        print('Общая стоимость купленных:     ', self.total_purchase_cost)
        print('Цена по которой будут проданы:   ', self.selling_price)
        print('Общая потенциальная прибыль:      ', self.total_potential_profit)
        print('Чистая прибыль:                 ', self.net_profit)
        # Вывод разделительной линии
        print('__________________________________________')

    # Метод для показа графика истории прибыли
    def show_history(self):
        # Создание графика
        plt.figure(figsize=(10, 6))
        # Построение графика истории чистой прибыли
        plt.plot(self.profit_history, label="Чистая прибыль")
        # Настройка подписей осей
        plt.xlabel("Количество купленных единиц")
        plt.ylabel("Чистая прибыль")
        # Настройка заголовка графика
        plt.title("История прибыли")
        # Отображение легенды
        plt.legend()
        # Включение сетки на графике
        plt.grid(True)
        # Отображение графика
        plt.show()

# Создание объекта компании
company = Company('VENEV', 'SOSNA', 100000, 100, 200000, 500)

# Основной цикл программы
while True:
    # Вывод информации о компании
    company.print_info()

    # Запрос на продолжение или выход из программы
    input('Нажмите Enter для продолжения или введите что-нибудь для выхода...')

    # Проверка на наличие товара на складе
    if company.initial_product_count == 0:
        # Вывод сообщения о том, что товара нет в наличии
        print("Товары закончились!")
        # Прерывание цикла
        break

    # Покупка продукта
    company.buy_product()

    # Вывод графика истории прибыли после каждой покупки
    company.show_history()