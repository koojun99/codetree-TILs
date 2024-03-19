word1 = input()
word2 = input()
chars1 = list(word1)
chars2 = list(word2)

chars1.sort()
chars2.sort()

if chars1 != chars2:
    print("No")
else:
    print("Yes")