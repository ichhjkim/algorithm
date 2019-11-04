N = int(input())

see = [list(map(int, input().split())) for _ in range(N)]

baby = 0

# 시작 크기는 2
for i in range(N):
    for j in range(N):
        if see[i][j] == 9:
            baby = [i, j, 2]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
def bfs():
    global count
    queue = []
    queue.append(baby)
    visited = [[0] * N for _ in range(N)]
    flag = False
    result = 0
    fisch = []
    visited[baby[0]][baby[1]] = 1
    same_size = 0
    while queue:
        for _ in range(len(queue)):
            temp = queue.pop(0)

            for i in range(4):
                idx = temp[0] + dx[i]
                idy = temp[1] + dy[i]

                if idx < 0 or idy < 0 or idx > N-1 or idy > N-1:
                    continue
                elif 0 < see[idx][idy] < 7 and see[idx][idy] < baby[2] and not visited[idx][idy]:
                    visited[idx][idy] = 1
                    queue.append([idx, idy])
                    fisch.append([idx, idy])
                elif (see[idx][idy] == 0 or see[idx][idy] == baby[2] or see[idx][idy] == 9) and not visited[idx][idy]:
                    visited[idx][idy] = 1
                    queue.append([idx, idy])

        result += 1
        if fisch:
            fisch.sort()
            fish = fisch.pop(0)
            same_size += 1
            if same_size == baby[2]:
                baby[2] += 1
                same_size = 0
            baby[0] = fish[0]
            baby[1] = fish[1]
            see[fish[0]][fish[1]] = 0
            queue = []
            queue.append(baby)
            count += result
            result = 0
            fisch = []
            visited = [[0] * N for _ in range(N)]
            visited[baby[0]][baby[1]] = 1

bfs()
print(count)




