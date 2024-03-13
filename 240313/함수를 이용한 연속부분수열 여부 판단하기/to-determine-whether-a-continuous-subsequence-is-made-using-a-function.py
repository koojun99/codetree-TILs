n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
isValid = False
def is_partial(a, b, pos):
    if a[pos:len(b)+1] == b:
        return True
    return False

for i in range(n1):
    if a[i] == b[0] and is_partial(a, b, i):
        isValid = True
        break

if isValid:
    print("Yes")
else:
    print("No")