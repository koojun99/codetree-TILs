def calculate(a, b):
    if a < b:
        a = a + 10
        b = b * 2
    elif a > b:
        a = a * 2
        b = b + 10
    return a, b

a, b = map(int, input().split())
a, b = calculate(a, b)
print(a, b)