import storage
import menu


def add_p():
    pupils = storage.read_pupils()
    russian = storage.read_russian()
    math = storage.read_math()
    sport = storage.read_sport()

    id_ = len(pupils)
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    class_number = input('1 - 1А, 2 - 1В. Введите цифру 1 или 2: ')
    class_number_int = menu.return_int(class_number, 1, 2)

    if class_number_int == 1:
        class_num = '1A'
    else:
        class_num = '1B'

    pupils.append([id_, surname, name, class_num])
    russian.append([])
    math.append([])
    sport.append([])

    storage.store_pupils(pupils)
    storage.store_russian(russian)
    storage.store_math(math)
    storage.store_sport(sport)
    print('Новый ученик добавлен')


# add()
