N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

def wall(num, visited):
    global lab
    global N
    global M
    c = [1, 0]
    if num == 3:
        return findtwo()

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and not visited[i][j]:
                for v in c:
                    visited[i][j] = v
                    if visited[i][j]:
                        lab[i][j] = 1
                        num += 1
                        wall(num, visited)
                        # 백트래킹할 때 들어가기 전으로 만들어줘야 한다.
                        num -= 1
                        lab[i][j] = 0
                    else:
                        wall(num, visited)

def findtwo():

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                for d in range(4):
                    origin_i = i
                    origin_j = j
                    origin_i += dx[d]
                    origin_j += dy[d]

                    if origin_i < 0 or origin_j < 0 or origin_i > N-1 or origin_j > N-1:
                        pass
                    elif lab[origin_i][origin_j] == 0:
                        lab[origin_i][origin_j] = 2
                        findtwo()

    return countzero()

def countzero():
    global results
    result = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                result += 1

    return results.append(result)

b = 0
num = 0
results = []
wall(num, visited)
print(results)





