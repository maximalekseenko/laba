from math import sqrt
parameters = [
    {
        'name':'D',
        'values':[16.0, 16.1, 15.9, 16.1, 16.0],
        'toolmisscount':0.1
    },
    {
        'name':'H',
        'values':[59.8, 59.7, 59.7, 59.7, 59.7],
        'toolmisscount':0.1
    },
    {
        'name':'m',
        'values':[32.0, 33.0, 31.0, 32.0, 33.0],
        'toolmisscount':0.5
    }
]

for parameter in parameters:
    print()

    # 1 Вычислить среднее значение параметра
    parameter['middle'] = sum(parameter['values']) / len(parameter['values'])
    print(parameter['name'], "\tсреднее значение\t", parameter['middle'])

    # 2 По формуле (4) определить погрешности отдельных измерений
    parameter['misscount'] = [abs(value - parameter['middle']) for value in parameter['values']]
    print(parameter['name'], "\tпогрешности\t\t", parameter['misscount'])

    # 3 Рассчитать значения квадратов этих погрешностей
    parameter['misscountpow2'] = [value * value for value in parameter['misscount']]
    print(parameter['name'], "\tквадраты погрешностей\t", parameter['misscountpow2'])

    # 4 По формулам (5) и (6) рассчитать случайную погрешность (значение коэффициента взять из таблицы 1, выбрав доверительную вероятность 0,7).
    parameter['misscountsquare'] = sqrt(sum(parameter['misscountpow2']) / (len(parameter['misscountpow2']) * (len(parameter['misscountpow2']) - 1)))
    print(parameter['name'], "\tквадратичная пог-ость\t", parameter['misscountsquare'])

    apn = 1.19
    parameter['misscountrand'] = apn * parameter['misscountsquare']
    print(parameter['name'], "\tслучайная погрешность\t", parameter['misscountrand'])

    # 6 Определить окончательные значения абсолютных погрешностей всех измеренных величин.
    parameter['misscountabsolute'] = parameter['misscountrand'] + parameter['toolmisscount']
    print(parameter['name'], "\tабсолютная погрешность\t", parameter['misscountabsolute'])