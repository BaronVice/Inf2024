# https://inf-ege.sdamgia.ru/problem?id=64938

s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
cnt = 0
for a1 in s:
    # С 0 число не начинается
    if a1 == 0: continue
    for a2 in s:
        if not(((a1 + a2) % 2 == 0 and a2 > a1) or ((a1 + a2) % 2 != 0 and a2 < a1)):
            continue
        for a3 in s:
            if not(((a2 + a3) % 2 == 0 and a3 > a2) or ((a2 + a3) % 2 != 0 and a3 < a2)):
                continue
            for a4 in s:
                if not(((a3 + a4) % 2 == 0 and a4 > a3) or ((a3 + a4) % 2 != 0 and a4 < a3)):
                    continue
                for a5 in s:
                    if not(((a4 + a5) % 2 == 0 and a5 > a4) or ((a4 + a5) % 2 != 0 and a5 < a4)):
                        continue
                    for a6 in s:
                        if not(((a5 + a6) % 2 == 0 and a6 > a5) or ((a5 + a6) % 2 != 0 and a6 < a5)):
                            continue
                        for a7 in s:
                            if not(((a6 + a7) % 2 == 0 and a7 > a6) or ((a6 + a7) % 2 != 0 and a7 < a6)):
                                continue
                            for a8 in s:
                                if not(((a7 + a8) % 2 == 0 and a8 > a7) or ((a7 + a8) % 2 != 0 and a8 < a7)):
                                    continue
                                for a9 in s:
                                    if not(((a8 + a9) % 2 == 0 and a9 > a8) or ((a8 + a9) % 2 != 0 and a9 < a8)):
                                        continue
                                    for a10 in s:
                                        if not(((a9 + a10) % 2 == 0 and a10 > a9) or ((a9 + a10) % 2 != 0 and a10 < a9)):
                                            continue
                                        for a11 in s:
                                            if not(((a10 + a11) % 2 == 0 and a11 > a10) or ((a10 + a11) % 2 != 0 and a11 < a10)):
                                                continue
                                            # Числа можно не записывать - достаточно посчитать количество
                                            cnt += 1
print(cnt)
