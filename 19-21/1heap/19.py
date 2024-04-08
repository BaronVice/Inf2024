# https://inf-ege.sdamgia.ru/problem?id=28242

# Победа при target и больше
target = 101
# Будем перебирать в нем числа от 1 до target (по условию задачи)
number = 0
# Здесь лежат ответы на задачу
answers = []

def check_if_vanya_wins(petya1):
    global target
    # Все ходы, при которых Петя выигрывает отбрасываем (используем, если в задаче просят найти максимальный number, здесь он не нужен)
    for i in range(len(petya1)):
        if petya1[i] >= target:
            petya1[i] = -1000

    return max(petya1) * 5 >= target

# Перебираем количество камней в куче
for number in range(1, target+1):
    # Петя делает ход (возможные вырианты)
    var1 = number + 1
    var2 = number * 5

    # Проверим, сможет ли Ваня победить после неудачного хода Пети
    if check_if_vanya_wins([var1, var2]):
        answers.append(number)

# Из ответов берем минимальный
print(min(answers))