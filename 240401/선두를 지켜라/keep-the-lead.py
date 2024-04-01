n, m = map(int, input().split())
placeA = [0]
placeB = [0]
first = []
currentA = 0
currentB = 0
count = 0

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        currentA += v
        placeA.append(currentA)
    
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        currentB += v
        placeB.append(currentB)

for i in range(1, min(len(placeA), len(placeB))):
    if placeA[i] >= placeB[i]:
        first.append("A")
    else:
        first.append("B")

for i in range(len(first)):
    if i > 0 and first[i] != first[i-1]:
        count += 1

print(count)