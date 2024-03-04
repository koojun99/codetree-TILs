line = input()

count1 = 0
count2 = 0
for i in range(len(line) - 1):
    if line[i] == "e":
        if line[i+1] == "e":
            count1 += 1
        elif line[i+1] == "b":
            count2 += 1

print(count1, end=" ")
print(count2)