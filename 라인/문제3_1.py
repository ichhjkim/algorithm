N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]
people.sort()
count = 1
visited = [0]* 200
for p in people:
    for t in range(p[0], p[1]):
        visited[t] += 1

print(max(visited))