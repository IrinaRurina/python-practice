import storage
from statistics import mean


def average_performance():
    pupils_list = storage.read_pupils()
    score_russian = storage.read_russian()
    score_math = storage.read_math()
    score_sport = storage.read_sport()

    russian_avr = list(map(mean, score_russian))
    russian_avr_round = []
    for item in russian_avr:
        russian_avr_round.append(round(item, 1))
    print(f'Средняя успеваемость по русскому языку: {round(mean(russian_avr_round), 1)}')

    math_avr = list(map(mean, score_math))
    math_avr_round = []
    for item in math_avr:
        math_avr_round.append(round(item, 1))
    print(f'Средняя успеваемость по математике: {round(mean(math_avr_round), 1)}')

    sport_avr = list(map(mean, score_sport))
    sport_avr_round = []
    for item in sport_avr:
        sport_avr_round.append(round(item, 1))
    print(f'Средняя успеваемость по физкультуре: {round(mean(sport_avr_round), 1)}')

    avr = list(zip(russian_avr_round, math_avr_round, sport_avr_round))
    pupil_avr = [round(mean(item), 1) for item in avr]
    avr = round(mean(pupil_avr), 1)

    pupils_list_res = pupils_list
    for i in range(len(pupils_list_res)):
        pupils_list_res[i].append(pupil_avr[i])

    res_1a = []
    res_1b = []
    sum_1a = 0
    sum_1b = 0

    for i in range(len(pupils_list_res)):
        if pupils_list_res[i][3] == '1A':
            res_1a.append(pupils_list_res[i])
            sum_1a += pupils_list_res[i][4]
        else:
            res_1b.append(pupils_list_res[i])
            sum_1b += pupils_list_res[i][4]
    avr_1a = round((sum_1a / len(res_1a)), 1)
    avr_1b = round((sum_1b / len(res_1b)), 1)

    print(f'САМАЯ СРЕДНЯЯ ИЗ ВСЕХ СРЕДНИХ УСПЕВАЕМОСТЕЙ =) {avr}')
    print(f'Средняя успеваемость учеников 1А: {avr_1a}')
    # print(*res_1a, sep='\n')
    print(f'Средняя успеваемость учеников 1В: {avr_1b}')
    # print(*res_1b,  sep='\n')

    return avr, russian_avr_round, math_avr_round, sport_avr_round, res_1a, avr_1a, res_1b, avr_1b, pupils_list_res


# average_performance()
