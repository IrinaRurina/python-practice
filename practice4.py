# 1 Вычислить число π c заданной точностью d
# *Пример:* - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import math
from math import pi
print(pi)

d = float(input("Задайте точность вычисления числа Пи: "))

calc_pi = 4
i = 1
add = 1
while abs(add) > d:
    add = 4 * (1 / ((2 * i + 1) * (-1)**i))
    calc_pi += add
    i += 1

print(calc_pi)

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Введите число N: "))
# i = 2
# simple_mult = []
# calc_simple_mult = n
# while i <= calc_simple_mult:
#     if calc_simple_mult % i == 0:
#         simple_mult.append(i)
#         calc_simple_mult //= i
#     else:
#         i += 1
# print(f"Простые множители числа {n}: {simple_mult}")

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# numbers = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Ваш список: {numbers}")
# unique_numbers = []
# for n in numbers:
#     if numbers.count(n) == 1:
#         unique_numbers.append(n)
#
# print(f"Список неповторяющихся элементов: {unique_numbers}")

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
#
# def random_polynomial(k, min=0, max=100):
#     k_list = [random.randint(min, max)]
#     while k_list[0] == 0:
#         k_list[0] = random.randint(min, max)
#     for i in range (1, k+1):
#         k_list.append(random.randint(min, max))
#     return k_list
#
#
# def write_polynomial(koeff_list, k):
#     with open('my_file.txt', 'a') as p:
#         p.write(f'{koeff_list}\n')
#         if koeff_list[0] == 1:
#             p.write(f'x^{k}')
#         else:
#             p.write(f'{koeff_list[0]}x^{k}')
#         for i in range(1,k+1):
#             if koeff_list[i] != 0:
#                 p.write('+')
#                 if koeff_list[i] != 1:
#                     p.write(f'{koeff_list[i]}')
#                 if i != k and i != k-1:
#                     p.write(f'x^{k-i}')
#                 elif i == k-1:
#                     p.write('x')
#                 elif i == k and koeff_list[i] == 1:
#                      p.write('1')
#         p.write('=0\n')
#
# # k = int(input('Задайте натуральную степень многочлена: '))
# k = 4
# k_list = random_polynomial(k)
# k_list1 = [2, 3, 1, 0, 3]
# k_list2 = [2, 0, 3, 0, 2]
# k_list3 = [1, 0, 0, 1, 0]
# write_polynomial(k_list, k)
# write_polynomial(k_list1, k)
# write_polynomial(k_list2, k)
# write_polynomial(k_list3, k)

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#
# def make_even_polynom(my_file1, my_file2):
#     s1 = int(my_file1[my_file1.find('^') + 1])  #stepen mnogochlena
#     s2 = int(my_file2[my_file2.find('^') + 1])
#     # k1 = []
#     # k2 = []
#
#     while s1 != s2:
#         if s1 > s2:
#             # k2.append(0)
#             s2 += 1
#         elif s1 < s2:
#             # k1.append(0)
#             s1 += 1
#     s = s1
#
#     return(s)
#
# def get_koeff_list(my_file, s):
#     k = []
#     for i in range(s+1):
#         if i < s - 1:
#             if f'x^{s-i}' in my_file:
#                 k.append(int(my_file.split(f'x^{s-i}')[0]))  # k with x^3, x^2
#                 my_file = my_file[my_file.find(f'x^{s-i}') + 3:]  # cut out first x il line
#             else:
#                 k.append(0)
#         elif i == s - 1:
#             if 'x' in my_file:
#                 k.append(int(my_file.split('x')[0]))
#                 my_file = my_file[my_file.find('x') + 1:]  # cut out first x in line
#             else:
#                 k.append(0)
#         else:
#             k.append(int(my_file.split('=')[0]))
#     return k
#
# def write_polynomial(sum_k_list, s):
#     with open('sum_polynom.txt', 'w') as p:
#         if sum_k_list[0] == 1:
#             p.write(f'x^{s}')
#         else:
#             p.write(f'{sum_k_list[0]}x^{s}')
#         for i in range(1,s+1):
#             if sum_k_list[i] != 0:
#                 if sum_k_list[i] > 0:
#                     p.write('+')
#                 if sum_k_list[i] != 1:
#                     p.write(f'{sum_k_list[i]}')
#                 if i != s and i != s-1:
#                     p.write(f'x^{s-i}')
#                 elif i == s-1:
#                     p.write('x')
#                 elif i == s and sum_k_list[i] == 1:
#                      p.write('1')
#         p.write('=0\n')
#
# with open('my_file1.txt', 'r') as f1:
#     my_file1 = f1.readline()
#     print(my_file1)
# with open('my_file2.txt', 'r') as f2:
#     my_file2 = f2.readline()
#     print(my_file2)
#
# s = make_even_polynom(my_file1, my_file2)
#
# k_list1 = get_koeff_list(my_file1, s)
# print(k_list1)
# k_list2 = get_koeff_list(my_file2, s)
# print(k_list2)
#
# sum_k_list = []
# for i in range(s+1):
#     sum_k_list.append(k_list1[i] + k_list2[i])
# print(sum_k_list)
# write_polynomial(sum_k_list, s)




# import Func_fill_missing_coeff as fm
# tp1 = fm.fill_missing_coeff(p1)
# tp2 = fm.fill_missing_coeff(p2)
#
# import Func_sum_polinom as fs
# result = fs.sum_polinom(tp1, tp2)
#
# my_file_result='f_polinom4_5_result.txt'
# import Func_call_record_func as fc
# fc.call_record_func(len(result)-1, result, my_file_result)
