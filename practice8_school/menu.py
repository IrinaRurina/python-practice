def select_menu():
    print('\nУченики. Успеваемость.\n\n'
          '1. Показать всех учеников\n'
          '2. Добавить ученика\n'
          '3. Посмотреть оценки ученика\n'
          '4. Добавить оценку ученика\n'
          '5. Посмотреть среднюю успеваемость \n'
          '6. Выгрузить отчет по успеваемости\n'
          '7. Выход\n')
    select = input('Введите цифру с 1 по 7: ')
    action = return_int(select, 1, 7)
    return action



def return_int(select, minimum, maximum):

    while not select.isdigit() or (int(select) < minimum) or (int(select) > maximum):
        select = input(f'Некорректный ввод. Введите цифру с {minimum} по {maximum}: ')
    select_int = int(select)
    return select_int



#
# def current_quarter():
#     q = input('Введите номер текущей четверти от 1 до 4: ')
#     while not q.isdigit() or (int(q) < 1) or (int(q) > 4):
#         q = input('Некорректный ввод. Введите цифру с 1 по 4: ')
#
#     q_int = int(q)
#     return q_int
