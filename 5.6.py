# 5.6 Найти значение переменной z, заданной суммой
# функций: z = f(|x|, y) + f(a, b) + f(|x| +1, -y) + f(|x| - |y|, x) + f(x + y, a + b)

def f(u, t):
    if u >= 0:
        return u + 2*t
    if u <= -1:
        return u + t
    if -1 < u < 0:
        return u**2 - 2*t + 1

x = 1
y = -5
a = 12
b = 9

z = f(abs(x), y) + f(a, b) + f(abs(x) + 1, -y) + f(abs(x) - abs(y), x) + f (x / y, a + b)

print(f'Результат: {z}')
