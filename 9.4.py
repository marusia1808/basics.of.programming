# 9.4 Построить треугольник по сторонам a, b и углу между ними C (в градусах).

from PIL import Image, ImageDraw
import math

# Функция для проверки ввода натурального числа и угла
def naturalNumberInput(massage, isAngle):
    while True:
        number = input(f'{massage}: ')

        try:
            number = int(number)
        except ValueError:
            print('Введено не число!')
        else:
            if number <= 0:
                print('Введено не положительное число!')
            elif isAngle:
                if number < 180:
                    return number
                else:
                    print('Введите угол меньше 180!')
            else:
                return  number

# Ввод данных
sideA = naturalNumberInput('Введите сторону A', False)
sideB = naturalNumberInput('Введите сторону B', False)
angle = naturalNumberInput('Введите угол между сторонами', True)

# Рассчеты 3 стороны, полупериметра, высоты от заданого угла до противоположной углу стороне и сдвига координаты x
sideC = (sideB**2 + sideA**2 - 2*sideB*sideA*math.cos(math.radians(angle)))**(1/2)
semiPerimeter = (sideA + sideB + sideC)/2
heigthC = ((2*((semiPerimeter*(semiPerimeter - sideC)*(semiPerimeter - sideB)*(semiPerimeter - sideA))**(1/2)))/sideC)
shiftX = (sideB**2 - heigthC**2)**(1/2)

# Рассчеты окна и его центра
windowSize = int(max(sideA, sideB, sideC, heigthC) * 3)
center = windowSize / 2

img = Image.new ("RGB", (windowSize, windowSize), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Рассчет координат
xyAngles = ()
xyAngles += (center, center)
xyAngles += (center + shiftX, center + heigthC)
xyAngles += (center - sideC + shiftX, center + heigthC)

draw.polygon((xyAngles), fill=(0, 0, 0))

img.show()