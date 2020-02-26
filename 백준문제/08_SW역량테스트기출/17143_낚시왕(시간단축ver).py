R, C, M = map(int, input().split())

sea = []
for _ in range(R):
    sea.append([[] for _ in range(C)])

for m in range(M):
    r, c, s, d, z = map(int, input().split())
    # 크기, 속력, 이동방향
    sea[r-1][c-1].append([z, s, d-1, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def work():
    time = 0
    result = 0
    while time < C:
        # 2. 낚시왕이 있는 열에 있는 상어중, x가 가장 적은 상어를 잡는다. 잡으면  상어는 사라짐
        for i in range(R):
            if sea[i][time]:
                result += sea[i][time][0][0]
                sea[i][time] = []
                break
        #
        # print(time, '------이동전========')
        # for i in range(R):
        #     print(sea[i])
        # 이동
        visited = [[0]*C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                if sea[x][y] and not sea[x][y][0][3]:
                    d = sea[x][y][0][2]
                    sd = sea[x][y][0][1]
                    idx = x
                    idy = y
                    # 3. 상어 이동 : 주어진 속도로 이동 1초에 3간이동,
                    if dx[d] != 0:
                        sd = sd % (2*(R-1))
                    else:
                        sd = sd % (2*(C-1))

                    while sd:
                        sd -= 1
                        if dx[d] != 0:
                            if idx + dx[d] < 0 or idx + dx[d] > R-1:
                                if d % 2:d -= 1
                                else: d += 1

                        else:
                            if idy + dy[d] < 0 or idy + dy[d] > C-1:
                                if d%2: d-=1
                                else: d+=1
                        idx += dx[d]
                        idy += dy[d]

                    temp = sea[x][y].pop(0)
                    temp[2] = d
                    visited[idx][idy] = 1
                    temp[3] = 1
                    sea[idx][idy].append(temp)


        # 이동 끝
        # 4. 이동이 끝난 후 한칸에 상어가 여러마리면, 크기가 제일 큰 상어가 나머

        for i in range(R):
            for j in range(C):
                if sea[i][j]:
                    sea[i][j].sort(reverse=True)
                    sea[i][j] = [sea[i][j][0]]
                    sea[i][j][0][3] = 0


        # print(time)
        # for i in range(R):
        #     print(sea[i])
        # print('--------------------')
        time += 1


    return result

print(work())
