line, char = input().split()

if line.find(char) == -1:
    print("No")
else:
    print(line.find(char))