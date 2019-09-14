def backtrack(a, result):
    global N
    global visited
    global results
    global days
    origin_a = a
    origin_r = result
    c = [1, 0]
    if a > N-1:
        # print(a)
        if a == N:
            if a+days[a][0] < N+2:
                result += days[a][1]
                return results.append(result)
            else:
                return results.append(result)

        else:
            return results.append(result)

    for r in c:
        a = origin_a
        result = origin_r
        visited[a] = r
        if visited[a]:
            if a+days[a][0] < N+2:  # 일종의 가지치기!
                    # for m in range(a+1, a+days[a][0]):
                    #     visited[m] = 1
                result += days[a][1]
                a += days[a][0]
                backtrack(a, result)
            else:
                a += 1
                backtrack(a, result)

        else:
            a += 1
            backtrack(a, result)

N = int(input())

days = [0]*(N+1)
visited = [0]*(N+1)

for i in range(1, N+1):
    m, n = map(int, input().split())
    days[i] = [m, n]

result = 0
results = []
standard = 1
backtrack(standard, result)
print(max(results))