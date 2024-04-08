# https://inf-ege.sdamgia.ru/problem?id=28243

# Победа при target и больше
target = 101
# Будем перебирать в нем числа от 1 до target (по условию задачи)
number = 0
# Здесь лежат ответы на задачу
answers = []

def check_if_vanya_loses(petya1):
    global target
    # values - первый ход Пети, если одним из них он приведет Ваню к поражению, то подобранный number нам подходит
    for value in petya1:
        # Все ходы, при которых Петя выигрывает первым ходом не рассматриваем (по условию)
        if value >= target:
            continue

        # Сперва проверим, что Ваня не выиграет после хода Пети
        # (Ваня возьмет операцию, которая даст ему наибольшее количество камней: *5)
        if value * 5 >= target:
            continue

        # Ваня делает ход (возможные варианты)
        var1 = value + 1
        var2 = value * 5

        # Проверим, что Ваня при любом своем ходе приведет Петю к победе (оба хода проигрывают)
        # Как и с Ваней, Петя умножает на 5
        if (var1 * 5 >= target) and (var2 * 5 >= target):
            return True
    

# Перебираем количество камней в куче
for number in range(1, target+1):
    # Петя делает ход (возможные вырианты)
    var1 = number + 1
    var2 = number * 5

    # Проверим, проиграет ли Ваня при любом своем ходе
    if check_if_vanya_loses([var1, var2]):
        answers.append(number)

print(answers)