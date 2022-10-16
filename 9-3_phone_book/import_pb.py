import storage


def import_contacts():
    with open('new_contact_list.txt', 'r') as f:
        text = f.readlines()
        for k in range(len(text)):
            a = text[k]
            text[k] = a.replace(' ', '')
            text[k] = a.replace(',', '')

        import_contact_list = []

        i = 0
        while i < len(text):
            contact = text[i]
            contact = contact[3:]
            contact_info = contact.split()
            import_contact_list.append(contact_info)
            i += 1
        storage.store_contacts(import_contact_list)

    return import_contact_list


# imported = import_contacts()
# storage.store_contacts(imported)

