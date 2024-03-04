line = input()
first = line[0]
second = line[1]
toList = list(line)

for i in range(len(toList)):
    if toList[i] == second:
        toList[i] = first

print(''.join(toList))