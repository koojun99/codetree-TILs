n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

for k in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = k+1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()