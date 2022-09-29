import storage


def export_contacts():
    file_name = input('Введите название файла экспорта латинскими буквами: ')

    choose_format = int(input('Варианты форматирования:\n'
                              '1 - контакт одной строкой\n'
                              '2 - каждое поле контакта с новой строки\n'
                              'Выберите форматирование списка 1 или 2: '))
    e_lst = storage.read_contacts()

    with open(f"{file_name}.txt", "w") as f:
        f.write(f'{choose_format}\n\n')
        if choose_format == 1:
            for i in range(len(e_lst)):
                f.write("{0}: {1}, {2}, {3}, {4}\n".format(i, e_lst[i][0], e_lst[i][1], e_lst[i][2], e_lst[i][3]))
            print(f'Список контактов экспортирован в файл {file_name} в формате {choose_format}')
        elif choose_format == 2:
            for i in range(len(e_lst)):
                f.write("{0}\n{1}\n{2}\n{3}\n{4}\n\n".format(i, e_lst[i][0], e_lst[i][1], e_lst[i][2], e_lst[i][3]))
            print(f'Список контактов экспортирован в файл {file_name} в формате {choose_format}')
        else:
            print('Формат выбран неверно. Введите 1 или 2')



