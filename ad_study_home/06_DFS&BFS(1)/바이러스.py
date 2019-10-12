def DFS(v):
    if not visited[v]:
        visited[v] = 1

        for i in computers[v]:
            if not visited[i]:
                DFS(i)


N = int(input())
connect = int(input())
computers = [[] for _ in range(N+1)]
V = 1
visited = [0] * (N+1)
for i in range(connect):
    a, b = map(int, input().split())

    computers[a] += [b]
    computers[b] += [a]

DFS(1)
print(sum(visited)-1)
