N = int(input())

def dfs(depth, s, result):
    global max_result
    global j

    if depth == 3:
        if result % 10 > max_result:
            max_result = result % 10

    else:
        for x in range(s, 5):
            dfs(depth+1, x+1, result+player[j][x])

max_results = []
player = [0]*(N+1)
for i in range(1, N+1):
    player[i] = list(map(int, input().split()))


max_idx = -1
for j in range(1, N+1):
    result = 0
    max_result = 0
    dfs(0, 0, result)
    max_results += [[max_result, j]]

max_results.sort()
print(max_results[-1][1])

