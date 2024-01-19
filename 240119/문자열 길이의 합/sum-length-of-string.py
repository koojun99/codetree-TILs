n = int(input())
arr = [input() for _ in range(n)]
total = 0
count = 0
for string in arr:
    total += len(string)
    if string[0] == 'a':
        count += 1
print(total, end = " ")
print(count)