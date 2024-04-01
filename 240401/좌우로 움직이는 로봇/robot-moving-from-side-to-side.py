n, m = map(int, input().split())
movementsA = []
movementsB = []

# 로봇 A의 움직임 입력 받기
for _ in range(n):
    distance, direction = input().split()
    movementsA.append((int(distance), direction))

# 로봇 B의 움직임 입력 받기
for _ in range(m):
    distance, direction = input().split()
    movementsB.append((int(distance), direction))

# 각 시간 단위별 로봇 A와 B의 위치 추적
positionA = positionB = 0
time = 0
meet_count = 0
previous_meet = False

# 로봇 A와 B의 움직임을 시뮬레이션
while movementsA or movementsB:
    if movementsA:
        distance, direction = movementsA.pop(0)
        while distance > 0:
            positionA += 1 if direction == 'R' else -1
            distance -= 1
            time += 1
            if positionA == positionB:
                if not previous_meet:
                    meet_count += 1
                    previous_meet = True
            else:
                previous_meet = False
    
    if movementsB:
        distance, direction = movementsB.pop(0)
        while distance > 0:
            positionB += 1 if direction == 'R' else -1
            distance -= 1
            time += 1
            if positionA == positionB:
                if not previous_meet:
                    meet_count += 1
                    previous_meet = True
            else:
                previous_meet = False

print(meet_count)