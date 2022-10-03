import storage
import menu


def show_s():
    pupils_list = storage.read_pupils()
    id_ = input('Введите ID ученика: ')
    id_int = menu.return_int(id_, 0, (len(pupils_list)-1))

    pupil = f'{pupils_list[id_int][1]} {pupils_list[id_int][2]} {pupils_list[id_int][3]}'
    print(f'Оценки ученика {pupil}:')
    score_russian = storage.read_russian()
    score_math = storage.read_math()
    score_sport = storage.read_sport()

    print(f'Оценки по русскому языку: {score_russian[id_int]}')
    print(f'Оценки по математике: {score_math[id_int]}')
    print(f'Оценки по физкультуре: {score_sport[id_int]}')


# show_s()
