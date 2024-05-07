# https://inf-ege.sdamgia.ru/problem?id=64938

s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Для каждой цифры (first) найдем такие цифры (second), что у этих пар выполняется хотя бы одно из условий:
# 1) сумма цифр чётна и вторая цифра больше первой;
# 2) сумма цифр нечётна и вторая цифра меньше первой.
pairs = dict()
for first in s:
    pairs[first] = []
    pairs[first] = []
    for second in s:
        if (first + second) % 2 == 0 and second > first:
            pairs[first].append(second)
        if (first + second) % 2 == 1 and second < first:
            pairs[first].append(second)

# Посмотрим на допустимые пары для каждой цифры:
for p in pairs:
    print(p, pairs[p])

# Зная допустимые пары цифр можно составлять числа, подцепляя цифры одну за другой согласно значениям в словаре
# Например начнем с единицы:
# 1 - 0 - (подцепляем цифры по pairs[0])
# 1 - 3 - (подцепляем цифры по pairs[3])
# 1 - 5 - (подцепляем цифры по pairs[5])
# 1 - 7 - (подцепляем цифры по pairs[7])
cnt = 0
for a in pairs.keys():
    # С 0 число не начинается
    if a == 0: continue
    for l in pairs[a]:
        for g in pairs[l]:
            for o in pairs[g]:
                for r in pairs[o]:
                    for i in pairs[r]:
                        for t in pairs[i]:
                            for m in pairs[t]:
                                for x in pairs[m]:
                                    for y in pairs[x]:
                                        for z in pairs[y]:
                                            # Числа можно не записывать - достаточно посчитать количество
                                            cnt += 1
print(cnt)
