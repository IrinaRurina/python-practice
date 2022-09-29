import storage


def import_contacts():
    # file_name = input('Имя файла импорта txt, без расширения: ')
    # with open(f"{file_name}.txt", "r") as f:
    with open('my_export.txt', 'r') as f:
        text = f.readlines()
        for k in range(len(text)):
            a = text[k]
            text[k] = a.replace(' ', '')
            text[k] = a.replace('\n', '')

        import_contact_list = []

        if int(text[0]) == 1:
            i = 2
            while i < len(text):
                contact = text[i]
                contact = contact[3:]
                contact_info = contact.split()
                import_contact_list.append(contact_info)
                i += 1
        elif int(text[0]) == 2:
            j = 3
            while j < len(text):
                contact_info = [text[j], text[j+1], text[j+2], text[j+3]]
                import_contact_list.append(contact_info)
                j += 6
        print(f'Импорт контактов завершен')
        print(import_contact_list)

    return import_contact_list


# imported = import_contacts()
# storage.store_contacts(imported)

