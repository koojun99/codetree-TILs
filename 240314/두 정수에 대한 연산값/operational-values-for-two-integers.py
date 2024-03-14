def calculate(a, b):
    if a < b:
        a = a * 2
        b = b + 25
        print(a, b)
    else:
        calculate(b, a)

a, b = map(int, input().split())
calculate(a, b)