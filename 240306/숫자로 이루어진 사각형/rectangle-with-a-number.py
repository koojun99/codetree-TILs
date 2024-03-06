n = int(input())
num = 1
for _ in range(n):
    for _ in range(n):
        print(num % 9 if num % 9 != 0 else 9, end=" ")
        num += 1
    print()