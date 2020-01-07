R, C, T = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(R)]

air = []

for i in range(R):
    for j in range(C):
        if area[i][j] == -1:
            air.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while T:
    visited = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if area[x][y] > 0:
                count= 0
                for i in range(4):
                    idx = x + dx[i]
                    idy = y + dy[i]

                    if idx < 0 or idy < 0 or idx > R-1 or idy > C-1:
                        continue
                    elif area[idx][idy] == -1:
                        continue
                    else:
                        count += 1
                        visited[idx][idy] += area[x][y]//5
                visited[x][y] += area[x][y] - (area[x][y]//5*count)

    for a in range(R):
        for b in range(C):
            if visited[a][b]:
                area[a][b] = visited[a][b]

    visited = [[0]*C for _ in range(R)]
    # 공기청정기 바람
    for i in range(1, C):
        # 반시계 방향
        if area[air[0][0]][i]:
            if i < C-1:
                visited[air[0][0]][i+1] = area[air[0][0]][i]
            else:
                if air[0][0]-1 > 0:
                    visited[air[0][0]-1][i] = area[air[0][0]][i]
            area[air[0][0]][i] = 0
        if area[air[1][0]][i]:
            if i < C-1:
                visited[air[1][0]][i+1] = area[air[1][0]][i]
            else:
                if air[1][0]+1 < R:
                    visited[air[1][0]+1][i] = area[air[1][0]][i]
            area[air[1][0]][i] = 0
    for j in range(air[0][0]-1, 0, -1):
        if area[j][C-1]:
            visited[j-1][C-1] = area[j][C-1]
            area[j][C-1] = 0

    for j in range(air[1][0]+1, R-1):
        if area[j][C-1]:
            visited[j+1][C-1] = area[j][C-1]
            area[j][C-1] = 0


    for i in range(C-1, -1, -1):
        if area[0][i]:
            if i-1 >= 0:
                visited[0][i-1] = area[0][i]
            else:
                if area[1][i] != -1:
                    visited[1][i] = area[0][i]
            area[0][i] = 0
        if area[R-1][i]:
            if i-1>= 0:
                visited[R-1][i-1] = area[R-1][i]
            else:
                if area[R-2][i] != -1:
                    visited[R-2][i] = area[R-1][i]
            area[R-1][i] = 0
    for j in range(1, air[0][0]):
        if area[j][0]:
            if area[j+1][0] != -1:
                visited[j+1][0] = area[j][0]
            area[j][0] = 0
    for j in range(R-1, air[1][0], -1):
        if area[j][0]:
            if area[j-1][0] != -1:
                visited[j-1][0] = area[j][0]
            area[j][0] = 0

    for n in range(R):
        for m in range(C):
            if visited[n][m]:
                area[n][m] = visited[n][m]

    T -= 1

result = 0
for i in range(R):
    for j in range(C):
        if area[i][j] > 0:
            result += area[i][j]

print(result)
