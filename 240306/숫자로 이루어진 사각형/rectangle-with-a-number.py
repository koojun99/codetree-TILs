n = int(input())
num = 1
for _ in range(n):
    for _ in range(n):
        if num > 9:
            print(num % 9, end= " ")
        else:
            print(num, end=" ")
        num += 1
    print()