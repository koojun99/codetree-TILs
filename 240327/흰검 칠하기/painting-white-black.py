n = int(input())
tiles = {}

current = 0
for _ in range(n):
    x, direction = input().split()
    distance = int(x)

    if direction == 'L':
        start = current - distance + 1
        end = current
        current =  current - distance + 1
    else:  # dir == 'R'
        start = current
        end = current + distance - 1
        current = current + distance - 1   # Update current position for 'R'

    for pos in range(start, end+1):
        if pos not in tiles:
            tiles[pos] = {'B': 0, 'W': 0, 'last': None}
        
        # Update color counts and last painted color
        if direction == 'R':
            tiles[pos]['B'] += 1
            tiles[pos]['last'] = 'B'
        else:  # dir == 'L'
            tiles[pos]['W'] += 1
            tiles[pos]['last'] = 'W'
            
        

# Initialize counts
white_count, black_count, grey_count = 0, 0, 0

# Determine counts based on last painted color and whether a tile turned grey
for tile in tiles.values():
    if tile['B'] >= 2 and tile['W'] >= 2:
        grey_count += 1
    elif tile['last'] == 'B':
        black_count += 1
    elif tile['last'] == 'W':
        white_count += 1

print(white_count, black_count, grey_count)