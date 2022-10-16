import pickle

# contact_list = [['Name0', 'ivanov', '00000', 'Comment0'], ['name1', 'Grishin', '11111', 'Comment1'], ['Name2', 'Mihailov', '22222', 'Comment2'], ['Name3', 'Ivanchenko', '3333', 'Comment3']]


def store_contacts(lst):
    for i in range(len(lst)):
        lst[i][0] = lst[i][0].capitalize()
        lst[i][1] = lst[i][1].capitalize()
    with open("pickle_storage", "wb") as fp:
        pickle.dump(lst, fp)


def read_contacts():
    with open("pickle_storage", "rb") as fp:
        storage_list = pickle.load(fp)
        return storage_list


# store_contacts(contact_list)
# storage_list1 = read_contacts()
# print(storage_list1)

