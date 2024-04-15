n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

count = 0

def isValid(arr, m):
    consecutive = 1
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            consecutive += 1
        else:
            consecutive = 1
    if consecutive >= m:
        return True
    return False

for row in grid:
    if isValid(row, m):
        count += 1
    
for col in range(n):
    # 열을 배열로 만들어 함수에 전달
    column = [grid[row][col] for row in range(n)]
    if isValid(column, m):
        count += 1

print(count)