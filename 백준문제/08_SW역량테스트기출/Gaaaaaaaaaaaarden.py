# 초록, 빨강
# 하얀: 뿌릴 수 없는 땅 1
# 황토 : 뿌릴 수 있는 땅 2
# 하늘 호수 0
# 동일한 시간에 하면 꽃이 핌
import itertools, collections

def spread(temp):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    s_visited = [0] * N
    for x in range(N):
        s_visited[x] = [[0, 0, 0] for _ in range(M)]

    queue = collections.deque(temp)

    for a in queue:
        if a[0] == "R":
            s_visited[a[1]][a[2]][0] = 1
        else:
            s_visited[a[1]][a[2]][1] = 1
    time = 1 # 동시간대인것을 체크해주어야 함
    while queue:
        time += 1
        for _ in range(len(queue)):
            t = queue.popleft()
            if s_visited[t[1]][t[2]][0] and s_visited[t[1]][t[2]][1]: # 한 타임에 다 이루어버릴 수 있으니까!
                continue
            for d in range(4):
                idx = t[1] + dx[d]
                idy = t[2] + dy[d]
                if idx < 0 or idy < 0 or idx > N-1 or idy > M-1:
                    continue
                elif land[idx][idy]:
                    if (not s_visited[idx][idy][0] and not s_visited[idx][idy][1]):
                        if t[0] == 'R':
                            s_visited[idx][idy][0] = 1
                            s_visited[idx][idy][2] = time
                        elif t[0] == 'G':
                            s_visited[idx][idy][1] = 1
                            s_visited[idx][idy][2] = time
                        queue.append([t[0], idx, idy])
                    elif not s_visited[idx][idy][0]:
                        if t[0] == 'R' and (time == s_visited[idx][idy][2]):
                            result += 1
                            s_visited[idx][idy][0] = 1
                            s_visited[idx][idy][2] = time
                    elif not s_visited[idx][idy][1]:
                        if t[0] == 'G' and (time == s_visited[idx][idy][2]):
                            result += 1
                            s_visited[idx][idy][1] = 1
                            s_visited[idx][idy][2] = time


    return result



N, M, G, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

brown = []
for x in range(N):
    for y in range(M):
        if land[x][y] == 2:
            brown.append([x, y])

max_result = 0
brown_visited = [0]*len(brown)
color = [R, G]

all_colors = list(itertools.combinations(brown, R+G))
for all_color in all_colors:
    color_rs = list(itertools.combinations(all_color, R))
    for color_r in color_rs:
        res = [0]*(R+G)
        for a in range(R+G):
            if all_color[a] in color_r:
                res[a] = ["R", all_color[a][0], all_color[a][1]]
            else:
                res[a] = ['G', all_color[a][0], all_color[a][1]]
        r = spread(res)
        max_result = max(max_result, r)


print(max_result)