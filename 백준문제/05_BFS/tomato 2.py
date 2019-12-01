import collections


def confirm():
    global count
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] ==0 and not visited[h][n][m]:
                    return -1

    return count-1

M, N, H = map(int, input().split())

def BFS():
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dh = [-1, 1]
    while queue:

        count += 1
        for _ in range(len(queue)):
            temp = queue.popleft()
            for i in range(4):
                idx = temp[1]+dx[i]
                idy = temp[2]+dy[i]

                if idx < 0 or idy < 0 or idx > N-1 or idy > M-1:
                    pass
                elif tomatoes[temp[0]][idx][idy]== 0 and not visited[temp[0]][idx][idy]:
                    visited[temp[0]][idx][idy] = 1

                    queue.append([temp[0], idx, idy])

            for h in range(2):
                idh = temp[0]+dh[h]
                if idh < 0 or idh > H-1:
                    continue
                elif tomatoes[idh][temp[1]][temp[2]] == 0 and not visited[idh][temp[1]][temp[2]]:
                    visited[idh][temp[1]][temp[2]] = 1
                    queue.append([idh, temp[1], temp[2]])


tomatoes = [[0]*N for _ in range(H)]
for h in range(H):
    for n in range(N):
        tomatoes[h][n] = list(map(int, input().split()))

visited = [[[0]*M for _ in range(N)] for _ in range(H)]

queue = collections.deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append([h, n, m])

count = 0
BFS()
print(confirm())


