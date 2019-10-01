def calcul(result, depth):
    global min_result

    if depth == N:
        if sum(results) < min_result:
            min_result = sum(results)
    else:
        for i in range(N):
            if not visited[i] and sum(results)+result+times[i] < min_result:
                visited[i] = 1
                result += times[i]
                results[depth] = result
                depth += 1
                calcul(result, depth)
                depth -= 1
                result -= times[i]
                results[depth] = 0
                visited[i] = 0

N = int(input())

visited = [0]*(N)
times = list(map(int, input().split()))
results = [0]*N
result = 0
min_result = N*1000
calcul(0, 0)
print(min_result)