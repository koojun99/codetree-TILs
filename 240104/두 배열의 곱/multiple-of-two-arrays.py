arr1 = []
arr2 = []

for _ in range(3):
    arr1.append(list(map(int, input().split())))
input()
for _ in range(3):
    arr2.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j], end=" ")
    print()