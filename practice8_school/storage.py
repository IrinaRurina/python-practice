import pickle

# pupils_list = [[0, 'Azarova', 'Elena', '1A'], [1, 'Vlasov', 'Roman', '1B'], [2, 'Lavrov', 'Andrey', '1A'], [3, 'Makarova', 'Ekaterina', '1A'], [4, 'Nestruev', 'Mikhail', '1A'], [5, 'Romashina', 'Svetlana', '1B'], [6, 'Chepalova', 'Yulia', '1B']]
#
# russian = [[4, 3, 3, 5, 5], [4, 4, 3, 5, 2], [5, 5, 3, 5, 4], [4, 4, 5, 3, 5, 5], [2, 3, 3, 2], [5, 5, 5, 5, 5], [5, 5, 4, 5, 5]]
# math = [[5, 5, 3, 5, 5], [4, 5, 3, 5, 3], [5, 4, 3, 5, 4], [5, 4, 5, 3, 5, 5], [3, 2, 3, 2], [5, 5, 5, 5, 5], [5, 5, 5, 4, 5, 5]]
# sport = [[4, 4, 3, 5, 5], [3, 4, 3, 5, 4], [4, 4, 4, 5, 4], [5, 4, 5, 5, 5, 5], [4, 3, 3], [5, 5, 5, 5, 5], [4, 5, 3, 5, 5]]


def store_pupils(pup):
    with open("pickle_pupils", "wb") as p:
        pickle.dump(pup, p)


def store_russian(rus):
    with open("pickle_russian", "wb") as p:
        pickle.dump(rus, p)


def store_math(ma):
    with open("pickle_math", "wb") as p:
        pickle.dump(ma, p)


def store_sport(spo):
    with open("pickle_sport", "wb") as p:
        pickle.dump(spo, p)


# store_pupils(pupils_list)
# store_russian(russian)
# store_math(math)
# store_sport(sport)


def read_pupils():
    with open("pickle_pupils", "rb") as p:
        pup = pickle.load(p)
        return pup


def read_russian():
    with open("pickle_russian", "rb") as p:
        rus = pickle.load(p)
        return rus


def read_math():
    with open("pickle_math", "rb") as p:
        ma = pickle.load(p)
        return ma


def read_sport():
    with open("pickle_sport", "rb") as p:
        spo = pickle.load(p)
        return spo


# russian = read_russian()
# math = read_math()
# sport = read_sport()
#
#
# print(russian)
# print(math)
# print(sport)
