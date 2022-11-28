# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Таблица истинности для данного выражения:
#   X  |  Y  |  Z  |! ( X + Y + Z )|! X * ! Y * ! Z
# -----+-----+-----+---------------+---------------
#   0  |  0  |  0  |       1       |       1
#   0  |  0  |  1  |       0       |       0
#   0  |  1  |  0  |       0       |       0
#   0  |  1  |  1  |       0       |       0
#   1  |  0  |  0  |       0       |       0
#   1  |  0  |  1  |       0       |       0
#   1  |  1  |  0  |       0       |       0
#   1  |  1  |  1  |       0       |       0

values = [True, False]
for x in values:
    for y in values:
        for z in values:
            print(x, y, z)
            result = (not (x or y or z)) == (not x and not y and not z)
            print(f'{result}\n')
