
def DFS(v):

    if not visited[v]:
        print(v, end=' ')
        visited[v] = 1
        for n in numbers[v]:
            DFS(n)


N, M, V = map(int, input().split())

numbers = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    # append안쓰려고 이렇게 리스트에 담았어요
    numbers[a] += [b]
    numbers[b] += [a]

for i in range(1, N+1):
    numbers[i].sort()

DFS(V)
print()

visited = [0]*(N+1)
queue = [V]
while queue:
    temp = queue.pop(0)
    if not visited[temp]:
        print(temp, end=' ')
        visited[temp] = 1
        queue.extend(numbers[temp])

print()
