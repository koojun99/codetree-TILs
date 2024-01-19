arr = [input() for _ in range(10)]
char = input()
count = 0
for string in arr:
    if string[-1] == char:
        print(string)
        count += 1
if count == 0:
    print(None)