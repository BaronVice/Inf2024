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

def check_if_vanya_loses(values):
    global target
    # values - первый ход Пети, если одним из них он приведет Ваню к поражению, то подобранный number нам подходит
    for value in values:
        # Все ходы, при которых Петя выигрывает первым ходом не рассматриваем (по условию)
        if sum(value) >= target:
            continue

        # Сперва проверим, что Ваня не выиграет после хода Пети
        # (Ваня возьмет операцию, которая даст ему наибольшее количество камней: удвоит наибольшую кучу)
        if max(value) * 2 + min(value) >= target:
            continue

        # Ваня делает ход (возможные варианты)
        vars = [
            [value[0] + 1, value[1]],
            [value[0] * 2, value[1]],
            [value[0], value[1] + 1],
            [value[0], value[1] * 2]
        ]

        # Проверим, что Ваня при любом своем ходе приведет Петю к победе 
        # (если хотя бы одним Петя не достигнет победы, то смотрим другие ходы Пети)
        if all(max(var) * 2 + min(var) >= target for var in vars):
            return True


# Перебираем количество камней во второй куче
for number in range(1, 62): 
    # Проверим, проиграет ли Ваня после одного из ходов Пети
    # Здесь уже пары значений, поскольку и куч две
    if check_if_vanya_loses(
            [
                [first + 1, number],
                [first * 2, number],
                [first, number + 1],
                [first, number * 2]
            ]
        ):
        answers.append(number)

print(answers)