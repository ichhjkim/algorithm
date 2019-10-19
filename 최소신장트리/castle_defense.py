from collections import deque
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t = [0]*3
v = [0]*M
l = [num for num in range(M)]
max_cnt = 0
dx, dy = [ 0, -1, 0], [-1, 0, 1]

# vv에 bfs 깊이가 저장되며 가므로 D보다 커질 때 끝남
def isEnd(li):
    global D
    for iss in range(len(li)):
        for end in range(len(li[0])):
            if li[iss][end] > D:
                return False
    return True

# 가장 가까운 적 찾기
def bfs(queue, visited, arr):
    vv = [[0] * (M+1) for _ in range(N+1)]
    while queue and isEnd(vv):
        x, y = queue.popleft()
        for idx in range(3):
            a = x + dx[idx]
            b = y + dy[idx]
            if 0 <= a < N and 0 <= b < M:
                if arr[a][b] == 0 and not vv[a][b]:
                    vv[a][b] = vv[x][y] + 1
                    queue.append((a, b))
                elif arr[a][b] == 1 and not vv[a][b] and vv[x][y]+1 <= D and not visited[a][b]:
                    return (a, b)
    return False

# 조합 후 해당 자리에 궁수가 있다고 가정하여 함수에 넣음
def perm(k):
    global max_cnt
    if k == 3:
        arrrrrr = [[0] *M for _ in range(N)]
        for xxxx in range(N):
            for yyyy in range(M):
                arrrrrr[xxxx][yyyy]= arr[xxxx][yyyy]
        visited = [[0]*M for _ in range(N)]
        cnt = 0
        for n in range(N, -1, -1):
            re = []
            for tt in range(3):
                queue = deque([])
                queue.append((n, t[tt]))
                re.append(bfs(queue, visited, arrrrrr))
            # 조합된 값 3개를 함수 통과시켜 re에 담고 거리가 2라면
            for r in range(len(re)):
                if re[r]:
                    h1, h2 = re[r]
                    if not visited[h1][h2]:
                        if abs(n - h1) + abs(t[r] - h2) <= D:
                            visited[h1][h2] = 1
                            cnt += 1
            for rm in range(M):
                arrrrrr[n-1][rm] = 0

        if cnt > max_cnt:
            max_cnt = cnt

    else:
        for i in range(M):
            if v[i]:
                continue
            if k == 0 or t[k-1] < l[i]:
                t[k] = l[i]
                v[i] = 1
                perm(k + 1)
                v[i] = 0
perm(0)
print(max_cnt)