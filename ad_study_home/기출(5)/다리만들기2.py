N, M = map(int, input().split())

lands = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
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


nodes = [[0]*(island_num+1) for _ in range(island_num+1)]
def distance(x, y, num):
    global nodes
    # 섬 번호는 1부터 시작하니까
    # candidates = [False]*(len(islands)+1)
    for d in range(2):
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
            if not nodes[num][lands[idx][idy]]:
                nodes[num][lands[idx][idy]] = count
            elif nodes[num][lands[idx][idy]] > count: # 만약 해당 다리와 이미 연결되어 있다면, 다리 길이를 비교
                nodes[num][lands[idx][idy]] = count


for n in range(len(islands)):
    for m in range(len(islands[n])):
        x, y, num = islands[n][m]
        distance(x, y, num)
        # islands 내 island 하나씩 꺼내고 좌표 꺼내고 함수 돌리기

min_distance = 10000000000000000
start = 1
list_nodes = []
for i in range(1, island_num+1):
    for j in range(1, island_num+1):
        if nodes[i][j]:
            list_nodes.append([i, j, nodes[i][j]])
v_nodes = [0]*(len(list_nodes))
min_distance = 10000000000000000
#print(list_nodes)
def connected(candidate):

    queue = [candidate[0]]
    visited_sum = [[0] * (island_num+1) for _ in range(island_num+1)]
    distanz = candidate[0][2]
    visited_sum[candidate[0][0]][candidate[0][1]] = 1
    visited_sum[candidate[0][1]][candidate[0][0]] = 1
    confirm = [0]*(island_num+1)
    confirm[candidate[0][0]] = 1
    confirm[candidate[0][1]] = 1
    while queue:
        for _ in range(len(queue)):
            temp = queue.pop(0)
            for c in range(len(candidate)):
                if candidate[c][0] == temp[1] and not visited_sum[candidate[c][1]][temp[1]] and not visited_sum[temp[1]][candidate[c][1]]:
                    distanz += candidate[c][2]
                    visited_sum[candidate[c][1]][temp[1]] = 1
                    visited_sum[temp[1]][candidate[c][1]] = 1
                    confirm[candidate[c][1]] = 1
                    confirm[temp[1]] = 1
                    queue.append(candidate[c])
                if candidate[c][1] == temp[0] and not visited_sum[candidate[c][0]][temp[0]] and not visited_sum[temp[0]][candidate[c][0]]:
                    distanz += candidate[c][2]
                    visited_sum[candidate[c][0]][temp[0]] = 1
                    visited_sum[temp[0]][candidate[c][0]] = 1
                    confirm[temp[0]] = 1
                    confirm[candidate[c][0]] = 1
                    queue.append(candidate[c])
    for i in range(1, island_num+1):
        if not confirm[i]:
            return False
    return distanz

def combination(depth, st, candi):
    global min_distance
    ori = candi[:]
    if depth == island_num-1:
        # 섬연결되었는지 확인 [0]*(island_num-1)
        d = connected(candi)
        if d:
            if min_distance > d:
                min_distance = d

    else:
        for i in range(st, len(list_nodes)):
            if not v_nodes[i]:
                v_nodes[i] = 1
                candi.append(list_nodes[i])
                candi.append([list_nodes[i][1], list_nodes[i][0], list_nodes[i][2]])
                combination(depth+1, i+1, candi)
                v_nodes[i] = 0
                candi = ori[:]
combination(0, 0, [])
if min_distance == 10000000000000000:
    print(-1)
else:
    print(min_distance)










