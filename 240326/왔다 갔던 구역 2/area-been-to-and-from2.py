n = int(input())
space = [0]*10*n
current = 10*n // 2
for _ in range(n):
    dist, direction = input().split()
    if direction == "R":
        for _ in range(int(dist)):
            space[current] += 1
            current += 1
    if direction == "L":
        for _ in range(int(dist)):
            space[current] += 1
            current -= 1
count = 0

for num in space:
    if num >= 2:
        count += 1

print(count)