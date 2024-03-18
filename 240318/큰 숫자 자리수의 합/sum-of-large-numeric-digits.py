a, b, c = map(int, input().split())
num = a*b*c

def add(num):
    if num < 10:
        return num
    return add(num//10) + num % 10

print(add(num))