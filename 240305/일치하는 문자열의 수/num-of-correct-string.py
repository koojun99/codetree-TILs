n, string = input().split()
count = 0
for _ in range(int(n)):
    sample = input()
    if string == sample:
        count += 1
print(count)