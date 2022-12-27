# 3.11 (Покер) Задан список из пяти чисел. Если одинаковы 5 чисел,
# то напечатайте число 1, иначе если одинаковы 4 числа, то напечатайте число 2,
# иначе если одинаковы 3 и 2 числа, то напечатайте число 3,
# иначе если одинаковы 3 числа, то напечатайте число 4, иначе если одинаковы 2 и 2 числа,
# то напечатайте число 5, иначе если одинаковы 2 числа, то напечатайте 6, иначе напечатайте число 7.

numbers = []
print('Введите 5 чисел')

# Проверка на ввод чисел
while len(numbers) < 5:
    text = input('Введите целое число: ')

    try:
        numbers.append(int(text))
    except ValueError:
        print('Введите число!')

count = len(list(set(numbers)))

if count == 1:
    print(1, '(Если одинаковы 5 чисел)')
elif count == 2:
    if (numbers.count(numbers[0]) == 4) or (numbers.count(numbers[1]) == 4):
        print(2, '(Если одинаковы 4 числа)')
    elif (numbers.count(numbers[0]) == 3) or (numbers.count(numbers[0]) == 2):
        print(3, '(Если одинаковы 3 и 2 числа)')
elif count == 3:
    if (numbers.count(numbers[0]) == 3) or (numbers.count(numbers[1]) == 3) or (numbers.count(numbers[2]) == 3):
        print(4, '(Если одинаковы 3 числа)')
    elif ((numbers.count(numbers[0]) == 2) and (numbers.count(numbers[1]) == 2)) or ((numbers.count(numbers[1]) == 2) and (numbers.count(numbers[2]) == 2)) or ((numbers.count(numbers[0]) == 2) and (numbers.count(numbers[2]) == 2)):
        print(5, '(Если одинаковы 2 и 2 числа)')
elif count == 4:
    if (numbers.count(numbers[0]) == 2) or (numbers.count(numbers[1]) == 2) or (numbers.count(numbers[2]) == 2) or (numbers.count(numbers[3]) == 2):
        print(6, '(Если одинаковы 2 числа)')
else:
    print(7, '(Иначе)')

print(numbers)
input()