N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
chess = [0]*K
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):visited[i][j] = []

for k in range(K):
    x, y, z = map(int, input().split())
    chess[k] = [x-1, y-1, z-1]
    visited[x-1][y-1].append(k)

# 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def withmoving(x, y, k, board):
    global visited
    klocation = -1
    for i in range(len(visited[x][y])):
        if visited[x][y][i] == k:
            klocation = i
            zusammen = [0]*(len(visited[x][y])-i)
            break
    i = klocation
    if (board==0) or (board==2):
        zindex = 0
        for j in range(i, len(visited[x][y])):
            zusammen[zindex] = visited[x][y][j]
            zindex += 1
        ## 빼기
        for j in range(i, len(visited[x][y])):
            visited[x][y].pop()

    elif board==1:
        zindex = 0
        for j in range(len(visited[x][y])-1, i-1, -1):
            zusammen[zindex] = visited[x][y][j]
            zindex += 1
        for j in range(i, len(visited[x][y])):
            visited[x][y].pop()

    return visited[x][y][:], zusammen[:]

def working():
    time = 0
    while True:
        time += 1
        if time > 1000: return -1
        for k in range(K):
            x, y, z = chess[k]
            idx = x + dx[z]
            idy = y + dy[z]

            # 이동하려는 칸 벽
            if idx < 0 or idy < 0 or idx > N-1 or idy > N-1 or board[idx][idy]==2:
                # 이동방향을 반대로 하고
                if z % 2: z -= 1
                else: z += 1
                idx = x + dx[z]
                idy = y + dy[z]

                if idx < 0 or idy < 0 or idx > N-1 or idy > N-1 or board[idx][idy]==2:
                    chess[k] = [x, y, z]
                elif board[idx][idy] == 0:
                     visited[x][y], zusammen= withmoving(x, y, k, 0)
                     visited[idx][idy]+= zusammen
                     if len(visited[idx][idy])>=4: return time

                     for i in range(len(zusammen)):
                         temp = zusammen[i]
                         chess[temp][0], chess[temp][1] = idx, idy
                     chess[k] = [idx, idy, z][:]
                elif board[idx][idy] == 1:
                    visited[x][y], zusammen = withmoving(x, y, k, 1)
                    visited[idx][idy] += zusammen
                    if len(visited[idx][idy]) >= 4: return time

                    for i in range(len(zusammen)):
                        temp = zusammen[i]
                        chess[temp][0], chess[temp][1] = idx, idy
                    chess[k] = [idx, idy, z][:]



            elif board[idx][idy] == 0:
                visited[x][y], zusammen = withmoving(x, y, k, 0)

                visited[idx][idy] += zusammen
                if len(visited[idx][idy]) >= 4: return time
                chess[k] = [idx, idy, z][:]

                for i in range(len(zusammen)):
                    temp = zusammen[i]
                    chess[temp][0], chess[temp][1] = idx, idy

            else:
                visited[x][y], zusammen = withmoving(x, y, k, 1)
                visited[idx][idy] += zusammen
                if len(visited[idx][idy]) >= 4: return time
                chess[k] = [idx, idy, z][:]
                for i in range(len(zusammen)):
                    temp = zusammen[i]
                    chess[temp][0], chess[temp][1] = idx, idy


print(working())







