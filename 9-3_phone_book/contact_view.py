import storage


def contact_search_by_surname(find):
    cap_find = find.capitalize()
    full_contact_list = storage.read_contacts()
    count = 0
    find_list = []
    for i in range(len(full_contact_list)):
        if full_contact_list[i][1].startswith(cap_find):
            find_list.append(full_contact_list[i])
            count += 1
    return find_list, count


