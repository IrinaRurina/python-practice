import storage


def add_new_contact(name, surname, phone, comment):
    full_contact_list = storage.read_contacts()
    full_contact_list.append([name, surname, phone, comment])
    storage.store_contacts(full_contact_list)
