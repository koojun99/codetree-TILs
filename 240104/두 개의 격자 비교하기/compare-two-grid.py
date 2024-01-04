arr1 = []
arr2 = []
n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            arr[i][j] = 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()