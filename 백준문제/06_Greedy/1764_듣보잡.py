N, M = map(int, input().split())
hear = {}
for _ in range(N):
    hear[input()] = 1
result = []
for _ in range(M):
    t = input()
    if hear.get(t): result.append(t)
result.sort()
print(len(result))
for r in result: print(r)