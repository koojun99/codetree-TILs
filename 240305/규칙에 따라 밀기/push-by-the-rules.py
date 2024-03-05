word = input()
command = input()

for i in range(len(command)):
    if command[i] == "L":
        word = word[1:] + word[0]
    elif command[i] == "R":
        word = word[-1] + word[:-1]
print(word)