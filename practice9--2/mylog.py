from datetime import datetime as dt
from time import time


def write_msg(chat_id, msg):
    calc_time = dt.now().strftime('%m.%d\t%H:%M')
    with open('calc_bot.log', 'a') as file:
        file.write(f'{calc_time}\t{chat_id}\t{msg}\n')


def write_calc(chat_id, value1, do, value2, result):
    data = f'{value1} {do} {value2} = {result}'
    calc_time = dt.now().strftime('%m.%d\t%H:%M')
    with open('calc_bot.log', 'a') as file:
        file.write(f'{calc_time}\t{chat_id}\t{data}\n')

