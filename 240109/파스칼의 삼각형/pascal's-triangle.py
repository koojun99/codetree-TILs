n = int(input())
triangle = [[1 for j in range(i+1)] for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

for row in triangle:
    for elem in row:
        print(elem, end=" ")
    print()