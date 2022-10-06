from datetime import datetime as dt
from time import time


def write_log(value1, do, value2, result):
    data = f'{value1} {do} {value2} = {result}'
    calc_time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{calc_time}\t{data}\n')

