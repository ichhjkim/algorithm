import collections

def BFS():
    global result, staat
    queue = collections.deque([])
    # staat 에 잇는거 하나씩 넣어서 복사가 되게 함, 처음에 모든 staat에
    # 있는 인덱스를 확인할 수 있돍
    copy_staat = []
    for i in range(N):
        copy_staat.append(staat[i])

    visited = [[0] * N for _ in range(N)]

    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            umzug = []
            queue.append([i, j])
            while queue:
        # visited를 매번 while이 돌떄마다 새로 생성될 수 있또록 함
                for _ in range(len(queue)):
                    temp = queue.popleft()
            # 근데 staat의 모든 인덱스를 bfs 돌면 시간 터지니까
            # 앞서 방문했던 애면 continue
                    confirm = False
                    for x in range(4):
                        idx = temp[0] + dx[x]
                        idy = temp[1] + dy[x]

                        if idx < 0 or idy < 0 or idx > N-1 or idy > N-1:
                            continue
                        elif not visited[idx][idy] and L <= abs(copy_staat[idx][idy]-copy_staat[temp[0]][temp[1]]) <= R:
                            queue.append([idx, idy])
                            umzug.append([idx, idy])
                            visited[idx][idy] = 1
                            confirm = True

                    if confirm and not visited[temp[0]][temp[1]]:
                        visited[temp[0]][temp[1]] = 1
                        umzug.append([temp[0], temp[1]])
                        confirm = False


            if umzug:
                # print(umzug, '이주')
                flag = True
                avg_umzug = 0
                for x in range(len(umzug)):
                    # umzug에 저장된 idx, idy 값으로 해당 staat 값 찾기
                    avg_umzug += staat[umzug[x][0]][umzug[x][1]]
                # 나눔
                avg_umzug //= len(umzug)

                # 나눈 후 값 저장
                for x in range(len(umzug)):
                    staat[umzug[x][0]][umzug[x][1]] = avg_umzug

    if flag:
        return True
    else:
        return False

N, L, R = map(int, input().split())

staat = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
flag = False
while BFS():
    # for i in range(N):
    #     print(staat[i])
    # print()
    result += 1
    continue

print(result)

