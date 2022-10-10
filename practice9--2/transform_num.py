from fractions import Fraction


def check_complex(check_value):
    if '+' in check_value and 'j' in check_value:
        temp = check_value.split('+')
    elif '-' in check_value and 'j' in check_value:
        temp = check_value.split('-')
    elif 'j' in check_value:
        temp = ['0', check_value]
    else:
        return False
    first = temp[0]
    second = temp[1]
    if temp[1] == 'j':
        second = '1j'

    if first.isdigit() and second[:-1].isdigit():
        return True
    else:
        return False


def transform_complex(value1, value2):
    value1 = complex(value1)
    value2 = complex(value2)
    return value1, value2


def check_rational(check_value):
    if '/' in check_value:
        temp = check_value.split('/')
        if temp[0].isdigit() and temp[1].isdigit():
            if temp[1] != 0:
                return True
    else:
        return False


def transform_rational(value1, value2):
    value1 = Fraction(int(value1[0: value1.index('/')]), int(value1[value1.index('/')+1:len(value1)]))
    value2 = Fraction(int(value2[0: value2.index('/')]), int(value2[value2.index('/')+1:len(value2)]))
    return value1, value2


