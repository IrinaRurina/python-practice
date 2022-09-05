# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# print('Введите номер дня недели, а я скажу, выходной ли это.')
# day = int(input())
#
# if day < 1 or day > 7:
#     print('Такого дня недели нет')
# elif day < 6:
#     print('нет')
# else:
#     print('да!')

# 2 Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
print('Проверка истинности выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x, y, z = 0, 0, 0
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 0, 0, 1
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 0, 1, 0
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 0, 1, 1
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 1, 0, 0
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 1, 0, 1
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

x, y, z = 1, 1, 1
print(x, y, z, end='    ')
if (-(x or y or z)) == (-x and -y and -z):
    print('Истинно')
else:
    print('Ложно')

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# print('Введите координату X')
# x = int(input())
# print('Введите координату Y')
# y = int(input())
#
# if x == 0 and y == 0:
#     print('Точка ({},{}) в начале координат' .format(x, y))
# elif x == 0:
#     print('Точка ({},{}) на оси Y' .format(x, y))
# elif y == 0:
#     print('Точка ({},{}) на оси X' .format(x, y))
# elif x > 0 and y > 0:
#     print('Точка ({},{}) в 1 координатной четверти'.format(x, y))
# elif x < 0 and y > 0:
#     print('Точка ({},{}) во 2 координатной четверти'.format(x, y))
# elif x < 0 and y < 0:
#     print('Точка ({},{}) в 3 координатной четверти'.format(x, y))
# else:
#     print('Точка ({},{}) в 4 координатной четверти'.format(x, y))

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

# print('Напишите номер четверти')
# quater = int(input())
# if quater == 1:
#     print ('X > 0, Y > 0')
# elif quater == 2:
#     print ('X < 0, Y > 0')
# elif quater == 3:
#     print ('X < 0, Y < 0')
# elif quater == 4:
#     print ('X > 0, Y < 0')
# else:
#     print ('Неправильно! Напишите 1, 2, 3 или 4')


# 5 Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

# print('Введите координаты первой точки через пробел: X1 Y1')
# x1, y1 = map(int, input().split())
# print('Введите координаты второй точки через пробел: X2 Y2')
# x2, y2 = map(int, input().split())
#
# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(distance)
# print('Расстояние между точкой 1 ({},{}) и точкой 2 ({}, {}) равно {}' .format(x1, y1, x2, y2, distance))
