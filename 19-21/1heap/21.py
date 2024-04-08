# https://inf-ege.sdamgia.ru/problem?id=28244

# Победа при target и больше
target = 101
# Будем перебирать в нем числа от 1 до target (по условию задачи)
number = 0
# Здесь лежат ответы на задачу
answers = []


def check_if_vanya_wins(value):
    global target
    # Первый ход Вани (одним из них он должен выиграть вторым ходом при любом ходе Пети)
    vanya1 = [value + 1, value * 5]

    # Ваня может победить и первым ходом, проверим
    if vanya1[0] >= target or vanya1[1] >= target:
        return True

    for var in vanya1:
        # Проверим, что Петя не победит вторым ходом
        if var * 5 >= target:
            continue

        # Петя делает второй ход (возможные варианты)
        var1 = var + 1
        var2 = var * 5

        # Ваня сейчас должен победить при любом ходе Пети
        if (var1 * 5 >= target) and (var2 * 5 >= target):
            # Один из ходов Вани привел его к победе
            return True
    
    # Иначе не подходит
    return False


def check_if_petya_loses(petya1):
    global target

    # Проверим, что Петя не выиграл первым ходом
    if max(petya1) >= target:
        return False

    # И проверим, что Ваня не может гарантированно выиграть первым ходом (по условию)
    if min(petya1) * 5 >= target:
        return False

    # values - первый ход Пети, любой его ход при правильном следующем ходе Вани приведет Петю к поражению 
    # Проверим это
    return all([check_if_vanya_wins(value) for value in petya1])
    

# Перебираем количество камней в куче
for number in range(1, target+1):
    # Петя делает ход (возможные вырианты)
    var1 = number + 1
    var2 = number * 5

    # Проверим, проиграет ли Петя при любом своем ходе
    if check_if_petya_loses([var1, var2]):
        answers.append(number)

print(answers)