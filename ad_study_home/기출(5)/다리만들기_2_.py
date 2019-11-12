N, M = map(int, input().split())

lands = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
islands = []
# 범위 확인
def is_wall(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False

# 일단 섬의 위치들을 저장
def find_island(x, y):
    global islands, island_num
    queue = [(x, y)]
    lands[x][y] = island_num
    island = [(x, y, island_num)]

    visited[x][y] = 1
    while queue:

        temp = queue.pop(0)

        for i in range(4):
            idx = temp[0] + dx[i]
            idy = temp[1] + dy[i]

            if is_wall(idx, idy):
                if not visited[idx][idy] and lands[idx][idy]:
                    visited[idx][idy] = 1
                    lands[idx][idy] = island_num
                    queue.append((idx, idy))
                    island.append((idx, idy, island_num))

    islands.append(island)

island_num = 0
for x in range(N):
    for y in range(M):
        if lands[x][y] and not visited[x][y]:
            island_num += 1
            find_island(x, y)


nodes = [[] for _ in range(island_num+1)]
def distance(x, y, num):
    global nodes
    # 섬 번호는 1부터 시작하니까
    candidates = [False]*(len(islands)+1)
    for d in range(4):
        idx = x + dx[d]
        idy = y + dy[d]
        count = 0
        while is_wall(idx, idy):
            # 만약 lands의 idx, idy 가 같은 섬이면 break
            if lands[idx][idy] == num:
                break
            # 만약 lands의 idx, idy 가 바다면
            elif not lands[idx][idy]:
                count += 1
                idx += dx[d]
                idy += dy[d]
            # 만약 lands의 idx, idy가 서로 다른 섬이면
            elif lands[idx][idy] != num:
                break

                # 만약 candidates에 한번도 들어온 적이 없다면,
        if count >= 2 and is_wall(idx, idy):
            if candidates[lands[idx][idy]] == False:
                candidates[lands[idx][idy]] = [num, lands[idx][idy], count]
            elif candidates[lands[idx][idy]][2] > count: # 만약 해당 다리와 이미 연결되어 있다면, 다리 길이를 비교
                candidates[lands[idx][idy]][2] = count

    for i in range(len(candidates)):
        if candidates[i] != False:
            nodes[num].append(candidates[i])

# while 문을 써서 하나하나 위치 확인
for n in range(len(islands)):
    for m in range(len(islands[n])):
        x, y, num = islands[n][m]
        distance(x, y, num)
        # islands 내 island 하나씩 꺼내고 좌표 꺼내고 함수 돌리기

v_nodes = [0]*(island_num+1)

min_distance = 10000000000000000
start = 1
v_nodes[start] = 1

print(nodes, '노드들 아오')

def backtrack(start, v_nodes, distanz, depth):
    global min_distance
    if depth > island_num-2:
        print('들어옴?', distanz)
        print(v_nodes)
        if min_distance > distanz:
            min_distance = distanz
    else:

        for i in range(len(nodes[start])):
            if not v_nodes[nodes[start][i][1]] or v_nodes[nodes[start][i][1]] > nodes[start][i][2]:
                ori = v_nodes[nodes[start][i][1]]
                v_nodes[nodes[start][i][1]] = nodes[start][i][2]
                print(nodes[start], ':', nodes[start][i])
            # 해당 노드 방문 처리
                if distanz + nodes[start][i][2] < min_distance:
                    backtrack(nodes[start][i][1], v_nodes, distanz+nodes[start][i][2])
                v_nodes[nodes[start][i][1]] = ori

#backtrack(start, v_nodes, 0, 0)

queue = list(range(1, island_num+1))

def bfs():

    while queue:
        for _ in range(len(queue)):
            temp = queue.pop(0)
            for i in range(len(nodes[temp])):
                if temp < nodes[temp][i][1] and (not v_nodes[nodes[temp][i][1]] or v_nodes[nodes[temp][i][1]] > nodes[temp][i][2]):
                    v_nodes[nodes[temp][i][1]] = nodes[temp][i][2]
                    # queue.append(nodes[temp][i][1])

bfs()
for i in range(N):
    print(lands[i])
print(v_nodes)
min_distance = 0
for i in range(2, len(v_nodes)):
    if v_nodes[i]:
        min_distance += v_nodes[i]

if not min_distance:
    print(-1)
else:
    print(min_distance)


def backtrack(start, v_nodes, distanz, depth):
    global min_distance
    if depth > island_num-2:
        print('들어옴?', distanz)
        print(v_nodes)
        if min_distance > distanz:
            min_distance = distanz
    else:

        for i in range(len(nodes[start])):
            if not v_nodes[nodes[start][i][1]] or v_nodes[nodes[start][i][1]] > nodes[start][i][2]:
                ori = v_nodes[nodes[start][i][1]]
                v_nodes[nodes[start][i][1]] = nodes[start][i][2]
                print(nodes[start], ':', nodes[start][i])
            # 해당 노드 방문 처리
                if distanz + nodes[start][i][2] < min_distance:
                    backtrack(nodes[start][i][1], v_nodes, distanz+nodes[start][i][2])
                v_nodes[nodes[start][i][1]] = ori

#backtrack(start, v_nodes, 0, 0)

queue = list(range(1, island_num+1))

def bfs():

    while queue:
        for _ in range(len(queue)):
            temp = queue.pop(0)
            for i in range(len(nodes[temp])):
                if temp < nodes[temp][i][1] and (not v_nodes[nodes[temp][i][1]] or v_nodes[nodes[temp][i][1]] > nodes[temp][i][2]):
                    v_nodes[nodes[temp][i][1]] = nodes[temp][i][2]
                    # queue.append(nodes[temp][i][1])


# 다리 조합을 하고, 백트래킹을 해주면서, 섬이 연결되어 있는지 dfs를 돌린다.
bfs()
for i in range(N):
    print(lands[i])
print(v_nodes)
min_distance = 0
for i in range(2, len(v_nodes)):
    if v_nodes[i]:
        min_distance += v_nodes[i]

if not min_distance:
    print(-1)
else:
    print(min_distance)
