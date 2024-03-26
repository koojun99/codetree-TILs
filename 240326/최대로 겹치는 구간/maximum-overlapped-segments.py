n = int(input())
lines = []
for _ in range(n):
    line = tuple(map(int, input().split()))
    if line[0] < 0 or line[1] < 0:
        line[0], line[1] = line[0] + 100, line[1] + 100
    lines.append(line)
base = [0]*200

for a, b in lines:
    for i in range(a-1, b-1):
        base[i] += 1
    
print(max(base))