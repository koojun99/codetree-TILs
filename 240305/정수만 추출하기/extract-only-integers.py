a, b = input().split()

for i in range(len(a)):
    if not a[i].isdigit():
        numA = int(a[:i])
        break
for i in range(len(b)):
    if not b[i].isdigit():
        numB = int(b[:i])
        break

print(numA+numB)