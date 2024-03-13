def samyookgu(n):
    if "3" in n or "6" in n or "9" in n:
        return True
    else:
        return False

def isValid(n):
    if n % 3 == 0:
        return True
    num = str(n)
    if samyookgu(num):
        return True
    return False
a, b = map(int, input(). split())
count = 0
for i in range(a, b+1):
    if isValid(i):
        count += 1

print(count)