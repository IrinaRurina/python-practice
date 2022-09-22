 # 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# Напишите программу, удабвляющую из текстабв абвсе слова, содержащие абв

# with open('practice5-1.txt', 'r') as fr:
#     line = fr.readline()
#
# with open('practice5-1.txt', 'w') as fw:
#     fw.write(" ".join(filter(lambda x: 'абв' not in x, line.split())))


# 2. Создайте программу для игры с конфетами человек против человека.
 # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
 # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
 # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
 # чтобы забрать все конфеты у своего конкурента?
 #  # a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного
 #  или больше чем имеется в куче.
 #  # b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать
 #  29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.

# 2.1 Человек против человека
# from random import randint
#
# total_sweets = 2021
# max_take = 28
# flag = randint(0, 1)
# player = flag + 1
# print(f"На столе {total_sweets} конфет. Первый ходит игрок {player}")
#
# while total_sweets > 0:
#     take = int(input(f"Игрок {player}, Возьмите от 1 до {max_take} конфет: "))
#     while take < 1 or take > max_take or take > total_sweets:
#         take = int(input(f"Игрок {player}, Возьмите правильное количество конфет!"))
#     if take > total_sweets:
#         print(f"Возьмите не более {total_sweets} конфет")
#     total_sweets -= take
#     print(f"Игрок {player} взял {take} конфет. На столе осталось {total_sweets} конфет")
#     if total_sweets == 0:
#         print(f"Выиграл игрок {player}")
#     flag = not flag
#     player = flag + 1

#  2.2 Человек против бота
#
# from random import randint
#
# total_sweets = 2021
# max_take = 28
# player = 1
# flag = randint(0, 1)
#
# if flag == 0:
#     print(f"На столе {total_sweets} конфет. Первый ходит игрок.")
# else:
#     print(f"На столе {total_sweets} конфет. Первый ходит бот.")
#
# while total_sweets > 0:
#     if (flag + 1) == player:
#         take = int(input(f"Игрок {player}, Возьмите от 1 до {max_take} конфет: "))
#         while take < 1 or take > max_take or take > total_sweets:
#             take = int(input(f"Игрок {player}, Возьмите правильное количество конфет!"))
#         total_sweets -= take
#         print(f"Игрок взял {take} конфет. На столе осталось {total_sweets} конфет")
#         if total_sweets == 0:
#             print("Поздравляю! Игрок выйграл!")
#         flag = not flag
#     else:
#         if total_sweets < max_take:
#             take = total_sweets
#         else:
#             take = randint(0, max_take)
#             # take = (total_sweets - total_sweets // 28 * 28) - 1  # smart bot
#             # if take == 0:
#             #     take = randint(0, max_take)
#             # elif take == -1:
#             #     take = 28
#         total_sweets -= take
#         print(f"Бот взял {take} конфет. На столе осталось {total_sweets} конфет")
#         if total_sweets == 0:
#             print("Бот выйграл")
#         flag = not flag

# 3. Создайте программу для игры в ""Крестики-нолики"".
#
# Пример интерфейса:
#
#    |   | 0
# -----------
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).''

def make_move():
    x = int(input("Введите координату X, где X - номер столбца от 1 до 3\n"))
    y = int(input("Введите координату Y, где Y - номер строки от 1 до 3\n"))
    while x < 1 or x > 3:
        x = int(input("X - номер столбца от 1 до 3. Повторите ввод.\n"))
    while y < 1 or y > 3:
        y = int(input("Y - номер строки от 1 до 3. Повторите ввод.\n"))
    return x, y

def print_game(lst):
    lststring = ''.join(lst)
    print(lststring)


def check_win(game_turn, game_lst):
    if game_turn < 5:
        win = 0
    elif game_turn < 10:
        win_coord = ((1, 3, 5), (10, 12, 14), (19, 21, 23), (1, 10, 19), (3, 12, 21), (5, 14, 23), (1, 12, 23), (5, 12, 19))
        for (a, b, c) in win_coord:
            check = [a, b, c]
            if game_lst[check[0]] == game_lst[check[1]] == game_lst[check[2]] != " ":
                print(f'Победили {game_lst[check[0]]}!')
                win = 1
                break
            else:
                win = 0
    return win


lst = ["  ", " ", " | ", " ", " | ", " ", "  ", "\n", "-------------", "\n"
       "  ", " ", " | ", " ", " | ", " ", "  ", "\n", "-------------", "\n"
       "  ", " ", " | ", " ", " | ", " ", "  "]
# 1 3 5 10 12 14 19 21 23

turn = 0
win = 0

while win == 0:
    print_game(lst)
    x, y = make_move()
    index = x * 10 + y

    find_position = {11: 1, 12: 3, 13: 5, 21: 10, 22: 12, 23: 14, 31: 19, 32: 21, 33: 23}
    check_cell = find_position[index]
    print(lst[check_cell])

    if lst[check_cell] == " ":
        if turn % 2 == 1:
            put = "O"
        else:
            put = "X"
        lst[check_cell] = put
    else:
        print("На этой клетке уже есть запись\n")
        turn -= 1
    turn += 1
    win = check_win(turn, lst)
    if turn == 9 and win == 0:
        print("Победила дружба!")
        break
    if win == 1:
        break

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def coding(data):
#     count = 1
#     res = ''
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + data[i]
#             count = 1
#     if count > 1 or (data[len(data)-2] != data[-1]):
#         res = res + str(count) + data[-1]
#     return res
#
# def decoding(data):
#     number = ''
#     res = ''
#     for i in range(len(data)):
#         if not data[i].isalpha():
#             number += data[i]
#         else:
#             res = res + data[i] * int(number)
#             number = ''
#     return res
#
# with open('practice5-4r.txt', 'r') as fr:
#     text = fr.readline()
#
# with open('practice5-4w.txt', 'w') as fw:
#     fw.write(f"Текст после кодировки: {coding(text)}\n"
#              f"Текст после дешифровки: {decoding(coding(text))}")
#
# # ffffffhhjjjjjjkjkjkkkkkkkk
