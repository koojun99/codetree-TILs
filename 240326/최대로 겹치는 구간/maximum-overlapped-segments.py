n = int(input())
lines = []
for _ in range(n):
    line = tuple(map(int, input().split()))
    lines.append(line)
base = [0]*max(lines, key=lambda x: x[1])[1]

for a, b in lines:
    for i in range(a-1, b-1):
        base[i] += 1
    
print(max(base))