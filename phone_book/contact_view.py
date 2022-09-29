import storage


def contact_search_by_surname():
    find = input('Введите букву алфавита, начальные буквы фамилии или фамилию полностью: ')
    cap_find = find.capitalize()
    full_contact_list = storage.read_contacts()
    count = 0
    for i in range(len(full_contact_list)):
        if full_contact_list[i][1].startswith(cap_find):
            print(*full_contact_list[i])
            count += 1
    if count == 0:
        print('По вашему поиску контакты не найдены')

