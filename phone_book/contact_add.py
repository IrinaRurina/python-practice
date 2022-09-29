import storage


def add_new_contact():
    full_contact_list = storage.read_contacts()
    name = input('Введите Имя: ')
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    full_contact_list.append([name, surname, phone, comment])
    storage.store_contacts(full_contact_list)
    print('Новый контакт добавлен')
