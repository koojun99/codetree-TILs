matrix = []
for _ in range(4):
    matrix.append(map(int,input().split()))
for row in matrix:
    print(sum(row))