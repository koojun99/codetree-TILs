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

meeting_time = -1  # 만나지 않으면 -1
for i in range(1, min(len(spotA), len(spotB))):
    if spotA[i] == spotB[i]:
        meeting_time = i
        break

print(meeting_time)