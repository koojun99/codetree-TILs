n, t = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    temp = bottom[n-1]
    
    for i in range(n-1, 0, -1):
        bottom[i] = bottom[i-1]
    bottom[0] = right[n-1]

    for i in range(n-1, 0, -1):
        right[i] = right[i-1]
    right[0] = left[n-1]
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]
    left[0] = temp

for elem in left:
    print(elem, end=" ")
print()
for elem in right:
    print(elem, end=" ")
print()
for elem in bottom:
    print(elem, end=" ")