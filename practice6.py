# # 1. Задайте строку из набора чисел. Напишите программу, которая покажет наибольшее и наименьшее число. Разделитель пробел
# # a = input("Write numbers with space: ").split()
# # min = int(a[0])
# # max = int(a[0])
# # for i in a:
# #     b = int(i)
# #     if b < min:
# #         min = b
# #     if b > max:
# #         max = b
# # print(min, max)
#
# # numbers = list(map(int, input("Write numbers with space: ").split()))
# # min_max = [item for item in numbers if item == min(numbers) or item == max(numbers)]
# # print(sorted(min_max))
#
#
# # 2. Задайте два числа. Найти наименьшее общее кратное
# #
# from math import gcd
# # def my_gcd(a, b):
# #     if a == b:
# #         return a
# #     elif a > b:
# #         return my_gcd(a - b, b)
# #     else:
# #         return my_gcd(b - a, a)
# #
# # print(my_gcd(27, 18))
#
#
# # def lcm(a, b):
# #     return abs(a * b) / gcd(a, b)
# #
# #
# # print(lcm(27, 18))
#
# my_gcd = lambda a, b: a if a == b else (my_gcd(a - b, b) if a > b else my_gcd(b - a, a))
# print(my_gcd(27, 18))
# my_lcm = lambda a, b: abs(a * b) / gcd(a, b)  # не скажу что проще, зато с лямбдой
# print(my_lcm(27, 18))
#
#
# # 3. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов -3 в степени N
# # for i in range(int(input())):
# #     print((-3) ** i)
#
# print([(-3)**i for i in range(int(input()))])
#
# # 4. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции. Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# # a = [2, 3, 5, 9, 3]
# # def odd_sum(n):
# #     count_odd_sum = 0
# #     for i in range(len(n)):
# #         if i % 2 == 1:
# #             count_odd_sum += n[i]
# #     return count_odd_sum
# #
# # print(odd_sum(a))
#
# a = [2, 3, 5, 9, 3, 6, 1]
# print(sum([a[i] for i in range(len(a)) if a[i] % 2 == 1]))
#
#
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# k = 8
#
# fib_list = [0]
# negafib_list = []
# for i in range(1, k + 1):
#     fib_list.append(fib(i))
# for i in range(-k, 0):
#     negafib_list.append(fib_list[-i] * (-1)**(-i + 1))
#
# print(negafib_list + fib_list)


k = 8

fib_list = [0]
negafib_list = []

fib = lambda n: 1 if (n == 1 or n == 2) else (fib(n-1) + fib(n-2))

for i in range(1, k + 1):
    fib_list.append(fib(i))

for i in range(-k, 0):
    negafib_list.append(fib_list[-i] * (-1)**(-i + 1))

print(negafib_list + fib_list)
