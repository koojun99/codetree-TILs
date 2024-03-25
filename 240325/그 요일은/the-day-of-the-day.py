m1, d1, m2, d2 = map(int, input().split())
target = input()
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
count = 0
day = 0
def total_days(m,d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(1, m):
        total += days[i]
    total += d
    return total

diff = total_days(m1, d1) - total_days(m2, d2)
diff = abs(diff)
while day != diff+1:
    day += 1
    weekday = day_of_week[day%7]
    if weekday == target:
        count += 1
print(count)