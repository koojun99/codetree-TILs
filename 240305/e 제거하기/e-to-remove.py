line = input()
pos = line.find('e')

print(line[:pos] + line[pos+1:])