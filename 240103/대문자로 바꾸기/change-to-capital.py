temp = []
for _ in range(5):
    temp.append(input().split())
for i in range(5):
    upper_case_words = [word.upper() for word in temp[i]]
    print(' '.join(upper_case_words))