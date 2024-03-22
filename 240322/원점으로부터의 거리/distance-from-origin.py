n = int(input())
points = []

for i in range(n):
    x, y = tuple(map(int, input().split()))
    num = i+1
    points.append((abs(x), abs(y), num))
points.sort(key=lambda x: x[0]+x[1])

for point in points:
    print(f"{point[2]}")