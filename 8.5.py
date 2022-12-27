# 8.5 Последовательность x1, x2,... образована по закону:
# Дано действительное E>0. Записать в файл h члены последовательности
# x1, x2,..., остановившись после первого члена, для которого выполнено |xi|<E.

import math

while True:
    E = input('Введите действительное положительное число число: ')

    try:
        E = float(E)
    except ValueError:
        print('Введено не число!')
        continue
    else:
        if E > 0:
            break
        else:
            print('Введено не положительное число!')

subsequence = []
i = 1
while True:
    x = (i - 0.1)/(i**3 + abs(math.tan(2*i)))
    if abs(x) >= E:
        subsequence.append(str(x))
    else:
        break
    i += 1

if len(subsequence) != 0:
    myFile = open("h.txt", "w")
    myFile.write(', '.join(subsequence))
    myFile.close()
else:
    print('Такой последовательности нет')

input()