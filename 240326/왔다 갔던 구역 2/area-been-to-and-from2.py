n = int(input())
current = 0
movements = []

# 이동 명령 처리
for _ in range(n):
    dist, direction = input().split()
    dist = int(dist)
    if direction == "R":
        movements.append((current, current + dist))
        current += dist
    elif direction == "L":
        movements.append((current - dist, current))
        current -= dist

# 각 구간의 방문 횟수를 기록할 딕셔너리
visited = {}

# 각 이동에 대해 방문 횟수 업데이트
for start, end in movements:
    for point in range(start, end):
        if point in visited:
            visited[point] += 1
        else:
            visited[point] = 1

# 2번 이상 방문한 구간의 길이 계산
overlapped_length = sum(1 for visit in visited.values() if visit > 1)

print(overlapped_length)