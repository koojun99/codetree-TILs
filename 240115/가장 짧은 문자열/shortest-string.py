arr = []
for _ in range(3):
    arr.append(len(input()))

print(max(arr)-min(arr))