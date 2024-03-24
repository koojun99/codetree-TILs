m1, d1, m2, d2 = map(int, input().split())
month, day = m1, d1
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 1

while (month, day) != (m2, d2):
    total += 1
    day += 1

    if day > days[month]:
        month += 1
        day = 1
print(total)