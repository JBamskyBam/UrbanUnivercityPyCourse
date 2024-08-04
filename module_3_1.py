# module_3_1

calls = 0

# Функция count_calls подсчитывающая вызовы остальных функций
def count_calls():
    global calls
    calls += 1
    print('Количество вызовов:', calls)

def string_info(string ):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)






