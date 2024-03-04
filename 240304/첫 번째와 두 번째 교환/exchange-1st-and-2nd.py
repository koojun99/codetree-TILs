line = input()
toList = list(line)

for i in range(len(toList)):
    if toList[i] == line[0]:
        toList[i] = line[1]
    elif toList[i] == line[1]:
        toList[i] = line[0]

print(''.join(toList))