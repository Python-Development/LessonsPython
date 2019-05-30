import sys
import math

# Програма розрахунку кореня квадратного рівняння:

a = int(input("Введіть коефіцієнт - A: "))
b = int(input("Введіть коефіцієнт - B: "))
c = int(input("Введіть коефіцієнт - C: "))

d = b ** 2 - 4 * a * c

if d < 0:
    print("Квадратне рівняння рязв'язку не має!")
    sys.exit()

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print("X1 = ", x1)
print("X2 = ", x2)
