n, k = map(int, input().split())
space = [0]*n

for _ in range(k):
    start, end = map(int, input().split())
    for i in range(start-1, end):
        space[i] += 1

print(max(space))