n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_partial(a, b, pos):
    if a[pos:len(b)+1] == b:
        print("Yes")
    else:
        print("No")

for i in range(n1):
    if a[i] == b[0]:
        is_partial(a, b, i)
        break