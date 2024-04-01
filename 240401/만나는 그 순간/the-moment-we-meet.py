n, m = map(int, input().split())
spotA = []
spotB = []
currentA = 0
currentB = 0

spotA.append(currentA)
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    for _ in range(distance):
        if direction == "R":
            currentA += 1
        elif direction == "L":
            currentA -= 1
        spotA.append(currentA)

spotB.append(currentB)
for _ in range(m):
    direction, distance = input().split()
    distance = int(distance)
    for _ in range(distance):
        if direction == "R":
            currentB += 1
        elif direction == "L":
            currentB -= 1
        spotB.append(currentB)
i = 0
while True:
    if i > min(len(spotA), len(spotB)):
        print(-1)
        break
    if i > 0 and spotA[i] == spotB[i]:
        print(i)
        break
    i += 1