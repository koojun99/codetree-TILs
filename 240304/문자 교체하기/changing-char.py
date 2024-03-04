line1, line2 = input().split()

list1, list2 = list(line1), list(line2)

list2[0], list2[1] = list1[0], list1[1]

print(''.join(list2))