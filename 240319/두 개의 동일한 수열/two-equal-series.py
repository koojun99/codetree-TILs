n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
is_same = True
for i in range(n):
    if a[i] not in b:
        is_same = False

if is_same:
    print("Yes")
else:
    print("No")