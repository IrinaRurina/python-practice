# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
import emoji


def make_move():
    k_x = int(input("Введите координату X, где X - номер столбца от 1 до 3\n"))
    k_y = int(input("Введите координату Y, где Y - номер строки от 1 до 3\n"))
    while k_x < 1 or k_x > 3:
        print(emoji.emojize(':thinking_face:'))
        k_x = int(input("X - номер столбца от 1 до 3. Повторите ввод.\n"))
    while k_y < 1 or k_y > 3:
        print(emoji.emojize(':thinking_face:'))
        k_y = int(input("Y - номер строки от 1 до 3. Повторите ввод.\n"))
    return k_x, k_y


def print_game(ls):
    lstring = ''.join(ls)
    print(lstring)


def check_win(game_turn, game_lst):
    w = 0
    if game_turn < 5:
        w = 0
    elif game_turn < 10:
        win_coord = ((1, 3, 5), (10, 12, 14), (19, 21, 23), (1, 10, 19), (3, 12, 21), (5, 14, 23), (1, 12, 23), (5, 12, 19))
        for (a, b, c) in win_coord:
            check = [a, b, c]
            if game_lst[check[0]] == game_lst[check[1]] == game_lst[check[2]] != "  ":
                print(f'Победили {game_lst[check[0]]}!', emoji.emojize(':trophy:'))
                w = 1
                break
            else:
                w = 0
    return w


lst = [" ", "  ", " | ", "  ", " | ", "  ", " ", "\n", "--------------", "\n"
       " ", "  ", " | ", "  ", " | ", "  ", " ", "\n", "--------------", "\n"
       " ", "  ", " | ", "  ", " | ", "  ", " "]
# 1 3 5 10 12 14 19 21 23

turn = 0
win = 0

while win == 0:
    print_game(lst)
    x, y = make_move()
    print(x, y)
    index = x * 10 + y

    find_position = {11: 1, 12: 3, 13: 5, 21: 10, 22: 12, 23: 14, 31: 19, 32: 21, 33: 23}
    check_cell = find_position[index]
    print(lst[check_cell])

    if lst[check_cell] == "  ":
        if turn % 2 == 0:
            put = emoji.emojize(':cross_mark:')
        else:
            put = emoji.emojize(':hollow_red_circle:')
        lst[check_cell] = put
    else:
        print("На этой клетке уже есть запись\n", emoji.emojize(':thinking_face:'))
        turn -= 1
    turn += 1
    win = check_win(turn, lst)
    if turn == 9 and win == 0:
        print("Победила дружба!", emoji.emojize(':handshake:'))
        break
    if win == 1:
        break


