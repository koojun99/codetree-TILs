a, b = map(int, input().split())
num = a + b
count = 0
string = str(num)
for char in string:
    if char == "1":
        count += 1

print(count)