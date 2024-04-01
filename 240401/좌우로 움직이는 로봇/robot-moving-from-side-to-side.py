n, m = map(int, input().split())
spotA = []
spotB = []
currentA = 0
currentB = 0
count = 0

spotA.append(currentA)
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    for _ in range(distance):
        if direction == "R":
            currentA += 1
        elif direction == "L":
            currentA -= 1
        spotA.append(currentA)

spotB.append(currentB)
for _ in range(m):
    distance, direction = input().split()
    distance = int(distance)
    for _ in range(distance):
        if direction == "R":
            currentB += 1
        elif direction == "L":
            currentB -= 1
        spotB.append(currentB)

length = max(len(spotA), len(spotB))

# 더 짧은 리스트를 더 긴 리스트의 길이에 맞게 확장
spotA += [spotA[-1]] * (length - len(spotA))
spotB += [spotB[-1]] * (length - len(spotB))

for i in range(1, length):
    if spotA[i-1] != spotB[i-1] and spotA[i] == spotB[i]:
        count += 1

print(count)