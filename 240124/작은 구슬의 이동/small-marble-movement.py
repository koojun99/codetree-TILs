n, t = map(int, input().split())
r, c, direction = input().split()
r, c = int(r), int(c)

dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]

d = {'D': 0, 'R': 1, 'L': 2, 'U': 3}

dir_num = d[direction]

def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= n

for i in range(t):
    nr = r + dr[dir_num]
    nc = c + dc[dir_num]
    if in_range(nr, nc):
        r = nr
        c = nc
    else:
        dir_num = 3 - dir_num


print (r, c)