import numpy as np

"""Угадывание числа. Аргумент - целое число от 1 до 100. 
Функция принимает загаданное число и возвращает число попыток (int)"""
def game_core_v3(number):
    """сount - число попыток. guess_numm - текущее проверяемое число. add_num - подстроечное число.
    В каждой итерации подстроечное число уменьшается в 2 раза и складывается, либо вычитается из текущего проеверяемого.
    Начинаем угадывать с максимального значения - 100. Стартовое значение подстроеченого числа в два раза меньше. """
    count = 1
    gues_num = 100
    add_num = gues_num / 2

    while number != gues_num:
        count+=1
        if number > gues_num:
            gues_num = gues_num + add_num
        else:
            gues_num = gues_num - add_num

        #Делим подстроечное число на 2 и округляем до ближайшего четного (банковское округление).
        add_num = round(add_num/2)

    #Возвращаем число попыток
    return(count)



def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

# запускаем
score_game(game_core_v3)
