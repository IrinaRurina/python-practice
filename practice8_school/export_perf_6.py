from performance_5 import average_performance as p
from statistics import mean


def export_p():
    avr, russian_avr_round, math_avr_round, sport_avr_round, res_1a, avr_1a, res_1b, avr_1b, pupils_list_res = p()
    names = []
    for i in range(len(pupils_list_res)):
        names.append(f'{pupils_list_res[i][1]} {pupils_list_res[i][2]}')

    names_1a = []
    for i in range(len(res_1a)):
        names_1a.append(f'{res_1a[i][1]} {res_1a[i][2]}')
    names_1b = []
    for i in range(len(res_1b)):
        names_1b.append(f'{res_1b[i][1]} {res_1b[i][2]}')

    with open("report.txt", "w") as f:

        f.write(f'Успеваемость: {avr}\n\n')
        f.write(f'Средняя успеваемость учеников 1А: {avr_1a}\n')
        for i in range(len(res_1a)):
            f.write("{0}: {1} {2} - {3}\n".format(res_1a[i][0], res_1a[i][1], res_1a[i][2], res_1a[i][4]))

        f.write(f'\nСредняя успеваемость учеников 1B: {avr_1b}\n')
        for i in range(len(res_1b)):
            f.write("{0}: {1} {2} - {3}\n".format(res_1b[i][0], res_1b[i][1], res_1b[i][2], res_1b[i][4]))

        f.write(f'\nСредняя успеваемость учеников по русскому языку: {round(mean(russian_avr_round), 1)}\n')
        for i in range(len(names)):
            f.write(f'{names[i]} {russian_avr_round[i]} \n')

        f.write(f'\nСредняя успеваемость учеников по математике: {round(mean(math_avr_round), 1)}\n')
        for i in range(len(names)):
            f.write(f'{names[i]} {math_avr_round[i]} \n')

        f.write(f'\nСредняя успеваемость учеников по физкультуре: {round(mean(sport_avr_round), 1)}\n')
        for i in range(len(names)):
            f.write(f'{names[i]} {sport_avr_round[i]} \n')



# export_p()
