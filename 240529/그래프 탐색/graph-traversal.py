n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
# start_v = [] 
# end_v = []


def dfs(vertex):
    global count
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            count += 1
            dfs(curr_v)


for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

count = 0
starting_point = 1
visited[starting_point] = True
dfs(starting_point)
print(count)
# for start, end in zip(start_v, end_v):