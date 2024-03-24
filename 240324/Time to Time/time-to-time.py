a, b, c, d = map(int, input().split())
hour, mins = a, b
total = 0
while (hour, mins) != (c, d):
    total += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
print(total)