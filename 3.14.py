# 3.14 Напишите программу, меняющую местами пару элементов списка по их указанным индексам.

# Проверка ввода чисел
def naturalNumberInput(long):
    while True:
        number = input(f'Введите индекс(от 0 до {long-1}): ')

        try:
            number = int(number)
        except ValueError:
            print('Введено не число!')
        else:
            if number < 0 or number >= long:
                print('Введен не индекс!')
            else:
                return  number

simbols = [1, 2, 3, 4, 5]

id1 = naturalNumberInput(len(simbols))
id2 = naturalNumberInput(len(simbols))

print(f'Изначальный список: {simbols}')

exchange = simbols[id1]
simbols[id1] = simbols[id2]
simbols[id2] = exchange

print(f'Результирующий список: {simbols}')