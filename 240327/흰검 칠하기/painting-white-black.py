n = int(input())
movements = []
colors = {}
current = 0

for _ in range(n):
    dist, direction = input().split()
    dist = int(dist)
    if direction == "R":
        movements.append((current, current + dist, direction))
        current += dist
        
    if direction == "L":
        movements.append((current - dist, current, direction))
        current -= dist

for start, end, direction in movements:
    for point in range(start, end):  # 모든 이동에 대해 범위 처리
        if point not in colors:
            colors[point] = [0, 0]  # 검은색과 흰색 횟수를 추적하기 위한 초기화
        if direction == "R":
            colors[point][0] += 1  # 오른쪽 이동(검은색) 횟수 증가
            colors[point].append("B")
        elif direction == "L":
            colors[point][1] += 1  # 왼쪽 이동(흰색) 횟수 증가
            colors[point].append("W")

grey_count = 0
black_count = 0
white_count = 0

for color_counts in colors.values():  # colors 딕셔너리의 모든 값에 대해 반복
    if color_counts[0] >= 2 and color_counts[1] >= 2:  # 검은색과 흰색이 모두 2 이상인 경우
        grey_count += 1  # grey_count 증가
    elif color_counts[-1] == "B":
        black_count += 1
    elif color_counts[-1] == "W":
        white_count += 1

print(white_count, black_count, grey_count)