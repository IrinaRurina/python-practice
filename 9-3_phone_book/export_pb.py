import storage


def export_contacts():

    e_lst = storage.read_contacts()

    with open("my_contacts.txt", "w") as f:
        for i in range(len(e_lst)):
            f.write("{0}: {1}, {2}, {3}, {4}\n".format(i, e_lst[i][0], e_lst[i][1], e_lst[i][2], e_lst[i][3]))



