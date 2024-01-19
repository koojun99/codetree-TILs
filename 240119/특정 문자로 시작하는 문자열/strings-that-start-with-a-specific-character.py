n = int(input())
count = 0
total = 0
arr = [input() for _ in range(n)]
char = input()

for string in arr:
    if string[0] == char:
        count += 1
        total += len(string)
average = total / count
print(count, end=" ")
print(f"{average:.2f}")