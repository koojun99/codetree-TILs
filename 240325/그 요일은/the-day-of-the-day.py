m1, d1, m2, d2 = map(int, input().split())
target = input()
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
count = 0
day = 0
def total_days(m,d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(1, m):
        total += days[i]
    total += d
    return total

diff = total_days(m1, d1) - total_days(m2, d2)
diff = abs(diff)
target_day_index = day_of_week.index(target)

for i in range(diff + 1):
    if (day + i) % 7 == target_day_index:
        count += 1
print(count)