def calc(value1, value2, do):
    if do == '+':
        return value1 + value2
    if do == '-':
        return value1 - value2
    if do == '*':
        return value1 * value2
    if (do == '/') and (value2 != 0):
        return value1 / value2
