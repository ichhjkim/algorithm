N, M = map(int, input().split())
hear = {input() for _ in range(N)}
see = {input() for _ in range(M)}
result = list(hear & see)
print(len(result))
result.sort()
for r in result: print(r)





