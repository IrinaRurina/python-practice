def view_data(title, result):
    print(f'{title} {result}')


def input_data():
    num_type = input('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами: ')
    if num_type == '1':
        value1 = input('Введите первое число (формат: "2+3j"): ')
        value2 = input('Введите второе число (формат: "2+3j"): ')
        do = input('Выберите операцию +, -, *, /: ')
    elif num_type == '2':
        value1 = input('Введите первое число (формат: "2/3"): ')
        value2 = input('Введите второе число (формат: "2/3"): ')
        do = input('Выберите операцию +, -, *, /: ')
    else:
        input_data()
    return num_type, value1, value2, do
