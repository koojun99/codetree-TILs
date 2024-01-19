arr = ["apple", "banana", "grape", "blueberry", "orange"]
letter = input()
count = 0
for word in arr:
    if word[2] == letter or word[3] == letter:
        print(word)
        count += 1
print(count)