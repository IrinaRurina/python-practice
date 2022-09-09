# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = float(input("Введите вещественное число: "))
# sum = 0
# while (num != int(num)):
#     num *= 10
# if num < 0:
#     num = -num
# while (num != 0):
#     sum += int(num % 10)
#     num = num // 10
# print(sum)

# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите целое число: '))
# def fact(n):
#     f = 1
#     for i in range(n):
#         f *= i + 1
#         print(f)
# fact(n)

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример: Для n = 6 -> 14.072

# n = 1 + int(input('Введите целое число: '))
# numbers = list(range(0, n))
# sum = 0
# for i in range(n):
#     if i == 0:
#         continue
#     numbers[i] = (1 + 1/i)**i
#     sum += numbers[i]
# print(round(sum,3))

# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.

# n = int(input('Введите N для промежутка [-N, N]: '))
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
#
# if a < 0 or a > (2 * n + 1) or b < 0 or b > (2 * n + 1):
#     print(f'В списке номера элементов от 0 до {n * 2 +1}, введите правильные номера]')
# else:
#     numbers = list(range(-n,n+1))
#     print(numbers)
#     mult = numbers[a] * numbers[b]
#     print(mult)

# Задание 5 Реализуйте алгоритм перемешивания списка.
# numbers = list(range(5))

# import time
# def random_num(n):
#    random=int(time.time()*1000)
#    random %= n
#    return random
# n = int(input())
# numbers = list(range(n))
# print(numbers)
# for i in range(n):
#     temp = numbers[i]
#     numbers[i] = numbers[random_num(n)]
#     numbers[random_num(n)] = temp
# print(numbers)

# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример: -Для "abababb" и "aba" -> 2

line = 'abababb'
findline = 'aba'
n = len(line) - len(findline)
count = 0
i = 0
while i <= n:
    if line[0] == findline[0]:
        if findline in line:
            count += 1
    line = line[1:]
    i += 1
print(count)