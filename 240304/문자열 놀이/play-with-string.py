line, n = input().split()
toList = list(line)
for _ in range(int(n)):
    
    query = list(input().split())
    if query[0] == "1":
        toList[int(query[1])-1], toList[int(query[2])-1] = toList[int(query[2])-1], toList[int(query[1])-1]
    elif query[0] == "2":
        for i in range(len(line)):
            if toList[i] == query[1]:
                toList[i] = query[2]
    print(''.join(toList))