import storage
import menu


def show_p():
    pupils_list = storage.read_pupils()

    select = input('1 - посмотреть 1А, 2 - посмотреть 1В, 3 - посмотреть всех. Введите цифру с 1 по 3: ')
    select_int = menu.return_int(select, 1, 3)

    if select_int == 1:
        for i in range(len(pupils_list)):
            if pupils_list[i][3] == '1A':
                line = pupils_list[i]
                print(*line)
    elif select_int == 2:
        for i in range(len(pupils_list)):
            if pupils_list[i][3] == '1B':
                line = pupils_list[i]
                print(*line)
    elif select_int == 3:
        for i in range(len(pupils_list)):
            line = pupils_list[i]
            print(*line)


# show_p()
