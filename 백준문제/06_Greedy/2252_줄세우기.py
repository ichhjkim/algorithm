import collections
N, M = map(int, input().split())
check = [[0]*N for n in range(N)]

for i in range(M):
    first, last = map(int, input().split())
    check[last-1][first-1] = 1



for i in range(N):
    for j in range(N):
        if check[i][j]:
            for x in range(N):
                if check[j][x]:
                    check[i][x] = 1

result = [[sum(check[n]), n+1] for n in range(N)]
result.sort()
for r in result:
    print(r[1], end=' ')




