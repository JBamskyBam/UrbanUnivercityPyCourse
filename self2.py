company_name = 'VENEV'
product_name = 'SOSNA'
product_how = 100000
product_price_bye = 100
balance = 200000
product_how_full = 0
product_price_full = product_how_full * product_price_bye
product_price_sell = 500
cash_full = product_price_full * product_price_bye
cash_pure = cash_full - product_price_full

b = ' '
b = input()
while b == '':
    b = ' '
    print('__________________________________________')
    print('__________________________________________')
    print('__________________________________________')
    print('Название кампании:               ', company_name)
    print('__________________________________________')
    print('Продукт:                         ', product_name)
    print('Количество:                      ', product_how)
    print('Цена по себестоимости:           ', product_price_bye)
    print('__________________________________________')
    print('Баланс:                          ', balance)
    print('__________________________________________')
    print('Количество купленных единиц:     ', product_how_full)
    print('Общая цена купленных единиц:     ', product_price_full)
    print('Цена по которой будут проданы:   ',product_price_sell)
    print('Общая прибыль при продаже:       ', cash_full)
    print('Чистая прибыль при продаже:      ', cash_pure)
    print('__________________________________________')
    print('__________________________________________')
    print('__________________________________________')
    b = input()

    product_how = product_how - 1
    balance = balance - product_price_bye
    product_how_full = product_how_full + 1
    product_price_full = product_how_full * product_price_bye
    cash_full = product_how_full * product_price_sell
    cash_pure = cash_full - product_price_full
