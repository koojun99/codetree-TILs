def calculate(a, b):
    if a < b:
        a = a * 2
        b = b + 25
    else:
        a = a + 25
        b = b * 2
    return a, b

a, b = map(int, input().split())
a, b = calculate(a, b)
print(a, b)