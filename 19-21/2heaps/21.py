# https://inf-ege.sdamgia.ru/problem?id=27780

# Особенности задач с двумя кучами:
# 1) Завершение игры: в одной из куч target камней, сумма в кучах = target, ...
# 2) Добавление камней в кучи: нет ограничений, добавляю с минимальным количеством, ...
# 3) Обычно нам дается количество камней в одной из куч (ищем начальное количество для другой)

# Победа при target и больше
target = 74
# Будем перебирать в нем числа от 1 до 61 (по условию задачи)
number = 0
# Здесь лежат ответы на задачу
answers = []
# Количество в первой куче
first = 12


def check_if_vanya_wins(value):
    global target
    # Первый ход Вани (одним из них он должен выиграть вторым ходом при любом ходе Пети)
    vanya1 = [
        [value[0] + 1, value[1]],
        [value[0] * 2, value[1]],
        [value[0], value[1] + 1],
        [value[0], value[1] * 2]
    ]

    # Ваня может победить и первым ходом, проверим
    for var in vanya1:
        if sum(var) >= target:
            return True
    # Еще это можно записать как
    # if any([sum(var) >= target for var in vanya1]):
    #   return True

    for var in vanya1:
        # Проверим, что Петя не победит вторым ходом
        if max(var) * 2 + min(var) >= target:
            continue

        # Петя делает второй ход (возможные варианты)
        petya2 = [
            [var[0] + 1, var[1]],
            [var[0] * 2, var[1]],
            [var[0], var[1] + 1],
            [var[0], var[1] * 2]
        ]

        # Ваня сейчас должен победить при любом ходе Пети
        combinations = 0
        for var in petya2:
            if max(var) * 2 + min(var) >= target:
                combinations += 1
        # Все комбинации привели Ваню к победе - значение подходит
        if combinations == len(petya2):
            return True
    
    # Иначе не подходит
    return False


def check_if_petya_loses(petya1):
    global target

    # Проверим, что Петя не выиграл первым ходом
    for value in petya1:
        if sum(value) >= target:
            return False

    # И проверим, что Ваня не может гарантированно выиграть первым ходом (по условию)
    combinations = 0
    for value in petya1:
        if max(value) * 2 + min(value) >= target:
            combinations += 1
    # Все комбинации первого хода Пети привели Ваню к победе первым ходом -> не подходит по условию
    if combinations == len(petya1):
        return False

    # petya1 - первый ход Пети, любой его ход при правильном следующем ходе Вани приведет Петю к поражению 
    # Проверим это
    for value in petya1:
        # Один из первых ходов Пети не позволяет Ване выиграть первым или вторым ходом
        if not check_if_vanya_wins(value):
            return False
        
    # Иначе независимо от ходов Пети Ваня имеет выигрышную стратегию - подходит
    return True


# Перебираем количество камней во второй куче
for number in range(1, 62): 
    # Проверим, проиграет ли Петя при любом своем ходе
    # Здесь уже пары значений, поскольку и куч две
    if check_if_petya_loses(
            [
                [first + 1, number],
                [first * 2, number],
                [first, number + 1],
                [first, number * 2]
            ]
        ):
        answers.append(number)

print(answers)