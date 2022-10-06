from fractions import Fraction


def transform_numbers(num_type, value1, value2):

    if num_type == '1':
        value1 = complex(value1)
        value2 = complex(value2)

    elif num_type == '2':
        value1 = Fraction(int(value1[0: value1.index('/')]), int(value1[value1.index('/')+1:len(value1)]))
        value2 = Fraction(int(value2[0: value2.index('/')]), int(value2[value2.index('/')+1:len(value2)]))

    return value1, value2
