n = int(input())
movements = []
colors = {}
current = 0

for _ in range(n):
    dist, direction = input().split()
    dist = int(dist)
    if direction == "R":
        movements.append((current, current + dist, "B"))
        current += dist
        
    elif direction == "L":
        movements.append((current - dist, current, "W"))
        current -= dist

for start, end, color in movements:
    for point in range(start, end):  # 모든 이동에 대해 범위 처리
        if point not in colors:
            colors[point] = {'B': 0, 'W': 0, 'last': None}
        colors[point][color] += 1  # 해당 색깔 횟수 증가
        colors[point]['last'] = color  # 마지막 색깔 기록

grey_count = 0
black_count = 0
white_count = 0

for color_counts in colors.values():
    if color_counts['B'] >= 2 and color_counts['W'] >= 2:
        grey_count += 1
    elif color_counts['last'] == "B":
        black_count += 1
    elif color_counts['last'] == "W":
        white_count += 1

print(white_count, black_count, grey_count)