sentence = input()
letter = input()
count = 0
for char in sentence:
    if char == letter:
        count += 1

print(count)