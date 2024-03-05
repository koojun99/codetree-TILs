a, b = input().split()
numA = 0
numB = 0
for i in range(len(a)):
    if not a[i].isdigit():
        numA = int(a[:i])
        break
else:
    numA = int(a)
for i in range(len(b)):
    if not b[i].isdigit():
        numB = int(b[:i])
        break
else:
    numB = int(b)

print(numA + numB)