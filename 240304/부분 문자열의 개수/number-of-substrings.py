line = input()
subline = input()
count = 0
for i in range(len(line) - 1):
    if line[i:i+2] == subline:
        count += 1

print(count)