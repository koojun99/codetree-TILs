word, n = input().split()

for _ in range(int(n)):
    command = input()
    if command == "1":
        word = word[1:] + word[0]

    elif command == "2":
        word = word[-1] + word[:-1]

    else:
        word = word[::-1]
    print(word)