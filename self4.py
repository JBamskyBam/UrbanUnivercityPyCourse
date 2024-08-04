company_name = 'VENEV'
product_name = 'SOSNA'
product_how = 100000
product_price_bye = 100
balance = 200000
product_how_full = 0
product_price_sell = 500

# Константы для ширины форматирования
LABEL_WIDTH = 37
VALUE_WIDTH = 15
DIVIDER_LENGTH = 50


def calculate_financials():
    product_price_full = product_how_full * product_price_bye
    cash_full = product_how_full * product_price_sell
    cash_pure = cash_full - product_price_full
    return product_price_full, cash_full, cash_pure


def format_info(label, value):
    return f"{label:<{LABEL_WIDTH}} | {value:<{VALUE_WIDTH}} |"


def display_info():
    product_price_full, cash_full, cash_pure = calculate_financials()

    info_lines = [
        '-' * DIVIDER_LENGTH,
        format_info('Название компании:', company_name),
        format_info('Продукт:', product_name),
        '-' * DIVIDER_LENGTH,
        format_info('Количество на складе:', product_how),
        format_info('Цена по себестоимости:', product_price_bye),
        format_info('Баланс:', balance),
        format_info('Количество купленных единиц:', product_how_full),
        format_info('Общая цена купленных единиц:', product_price_full),
        format_info('Цена продаж:', product_price_sell),
        format_info('Общая прибыль при продаже:', cash_full),
        format_info('Чистая прибыль при продаже:', cash_pure),
        '-' * DIVIDER_LENGTH
    ]

    print("\n".join(info_lines))


while True:
    display_info()

    b = input("Нажмите Enter для продолжения или любую клавишу для выхода: ")

    if b:
        break

    if product_how <= 0 or balance < product_price_bye:
        print("Недостаточно товара или средств для покупки.")
        break

    product_how -= 1
    balance -= product_price_bye
    product_how_full += 1