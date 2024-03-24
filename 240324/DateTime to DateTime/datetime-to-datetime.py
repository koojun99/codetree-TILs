a, b, c = map(int, input().split())
day, hour, mins = 11, 11, 11
total = 0

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