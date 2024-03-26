n = int(input())
space = [0]*100

for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start-1, end):
        space[i] += 1

print(max(space))