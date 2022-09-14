# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# a = [2, 3, 5, 9, 3]
# def odd_sum(n):
#     count_odd_sum = 0
#     for i in range(len(n)):
#         if i % 2 == 1:
#             count_odd_sum += n[i]
#     return count_odd_sum
# print(odd_sum(a))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def mult_first_last(n):
#     mult_list = []
#     for i in range((len(n) + 1) // 2):
#         mult = n[i] * n[len(n)-1 - i]
#         mult_list.append(mult)
#     return mult_list
#
# a = [2, 3, 4, 5, 6]
# print(mult_first_last(a))
#
# b = [2, 3, 5, 6]
# print(mult_first_last(b))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def f(n):
#     min = 1
#     max = 0
#     for i in n:
#         if 0 < (i - int(i)) <= min:
#             min = i - int(i)
#         if (i - int(i)) >= max:
#             max = i - int(i)
#     return(round((max - min),3))
#
# a = [1.1, 1.2, 3.1, 5, 10.01]
# print(f(a))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def to_binary(n):
#     reverse = []
#     i = 0
#     while n > 0:
#         reverse.append(n % 2)
#         n = n // 2
#         i += 1
#     binary = reverse[0]
#     i = 1
#     while i < len(reverse):
#         binary += reverse[i] * 10 ** i
#         i += 1
#     return binary
# print(to_binary(46))
# print(to_binary(45))
# print(to_binary(3))
# print(to_binary(2))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

k = 8

fib_list = [0]
negafib_list = []
for i in range(1, k + 1):
    fib_list.append(fib(i))
for i in range(-8, 0):
    negafib_list.append(fib_list[-i] * (-1)**(-i + 1))

print(negafib_list + fib_list)