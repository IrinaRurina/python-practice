import storage
import menu


def add_s():
    pupils_list = storage.read_pupils()

    score_russian = storage.read_russian()
    score_math = storage.read_math()
    score_sport = storage.read_sport()
    lesson = input('Выберите предмет: 1 - русский язык, 2 - математика, 3 - физкультура: ')
    lesson_int = menu.return_int(lesson, 1, 3)

    if lesson_int == 1:
        continue_ = True
        while continue_:
            id_ = input('Введите ID ученика: ')
            id_int = menu.return_int(id_, 0, (len(pupils_list)-1))
            pupil = f'{pupils_list[id_int][1]} {pupils_list[id_int][2]} {pupils_list[id_int][3]}'
            score = input('Введите оценку 1 - 5: ')
            score_int = menu.return_int(score, 1, 5)
            score_russian[id_int].append(score_int)
            print(f'{pupil} - добавлена оценка {score_int}')
            print(score_russian[id_int])
            plus = input('Продолжить ввод оценок для русского языка? 1 - да, 2 - нет')
            plus_int = menu.return_int(plus, 1, 2)
            if plus_int == 2:
                continue_ = False
        storage.store_russian(score_russian)

    elif lesson_int == 2:
        continue_ = True
        while continue_:
            id_ = input('Введите ID ученика: ')
            id_int = menu.return_int(id_, 0, (len(pupils_list)-1))
            pupil = f'{pupils_list[id_int][1]} {pupils_list[id_int][2]} {pupils_list[id_int][3]}'
            score = input('Введите оценку 1 - 5: ')
            score_int = menu.return_int(score, 1, 5)
            score_math[id_int].append(score_int)
            print(f'{pupil} - добавлена оценка {score_int}')
            print(score_math[id_int])
            plus = input('Продолжить ввод оценок для русского языка? 1 - да, 2 - нет')
            plus_int = menu.return_int(plus, 1, 2)
            if plus_int == 2:
                continue_ = False
        storage.store_math(score_math)

    elif lesson_int == 3:
        continue_ = True
        while continue_:
            id_ = input('Введите ID ученика: ')
            id_int = menu.return_int(id_, 0, (len(pupils_list)-1))
            pupil = f'{pupils_list[id_int][1]} {pupils_list[id_int][2]} {pupils_list[id_int][3]}'
            score = input('Введите оценку 1 - 5: ')
            score_int = menu.return_int(score, 1, 5)
            score_sport[id_int].append(score_int)
            print(f'{pupil} - добавлена оценка {score_int}')
            print(score_sport[id_int])
            plus = input('Продолжить ввод оценок для русского языка? 1 - да, 2 - нет')
            plus_int = menu.return_int(plus, 1, 2)
            if plus_int == 2:
                continue_ = False
        storage.store_sport(score_sport)


# add_s()
