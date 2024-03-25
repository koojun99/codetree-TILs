m1, d1, m2, d2 = map(int, input().split())
month, day = m1, d1
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
weekday_index = 1  # "Mon"에서 시작 (0부터 세면 "Sun")

if m2 < month or (m2 == month and d2 < day):
    while (month, day) != (m2, d2):
        day -= 1
        if day < 1:
            month -= 1
            day = days[month]
        weekday_index = (weekday_index - 1) % 7
else:
    while (month, day) != (m2, d2):
        day += 1
        if day > days[month]:
            month += 1
            day = 1
        weekday_index = (weekday_index + 1) % 7

weekday = day_of_week[weekday_index]
print(weekday)