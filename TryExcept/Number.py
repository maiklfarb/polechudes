# 1. Задача написать код, в котором у пользователя запрашивают число и он его вводит
# 2. Попробовать ввести не число в консоли - посмотреть ошибку в трассировке
# 3. Отловить ошибку, если ошибка поймана - написать сообщение пользователю, что он ввел неверные данные

try:
    age = int(input('введите возраст: '))
    print(age)
except ValueError as ex: # в ex будет лежать объект ошибки
    print('Неверные данные')
    print(f'Ошибка: {ex}')
