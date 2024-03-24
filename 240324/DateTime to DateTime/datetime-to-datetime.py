a, b, c = map(int, input().split())
day, hour, mins = 11, 11, 11
total = 0
if a < 11 or (a == 11 and (b < 11 or (b == 11 and c < 11))):
    print(-1)
else:
    while (day, hour, mins) != (a, b, c):
        total += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0
    
        if hour == 24:
            day += 1
            hour = 0

    print(total)