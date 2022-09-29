# import controller


def select_menu():
    print('\nМой телефонный справочник. Что будем делать?\n\n'
          '1. Посмотреть контакты\n'
          '2. Добавить контакт\n'
          '3. Экспортировать контакты\n'
          '4. Импортировать контакты\n'
          '5. Выход\n')

    select = input('Введите цифру с 1 по 5: ')

    while not select.isdigit() or int(select) < 1 or int(select) > 5:
        select = input('Некорректный ввод. Введите цифру с 1 по 5: ')
    select = int(select)

    return select


