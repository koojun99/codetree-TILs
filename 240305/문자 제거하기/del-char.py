word = input()
toList = list(word)
for _ in range(len(word) - 1):
    toDel = int(input())
    if toDel > len(toList):
        toDel = -1
    toList.pop(toDel)
    print(''.join(toList))