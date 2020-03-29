N, M = map(int, input().split())
check = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    check[b-1].append(a-1)

for i in range(N):
    if check[i]:
        for c in check[i]:
            if check[c]:
                for k in check[c]:
                    if k not in check[i]:
                        check[i].append(k)

result = [[len(check[n]), n+1] for n in range(N)]
result.sort()
for r in result:
    print(r[1], end=' ')



