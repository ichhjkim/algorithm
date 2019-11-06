# 처음에 for 돌리면서 0갯수 세고 
# #가 될떄마다 갯수에서 하나씩 빼줌

# 1번 CCTV는 한쪽 방향만 감시할 수 있따
# 2번은 두 방향
# 3번은 직각 두방향
# 4번은 세방향
# 5번은 모든 방향

## 6은 벽
# 0은 빈칸
# 1--5는 CCTV의 번호
# 1번 CCTV
N, M = map(int, input().split())

raum = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
count = 0
for i in range(N):
    for j in range(M):
        if 1 <= raum[i][j] <= 5:
            cctvs.append([raum[i][j], i, j])
        elif not raum[i][j]:
            count += 1
result = count

cctvs.sort(reverse=True)
visited = [[0]*M for _ in range(N)]



def cctv_one(visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = max_count = 0
    max_candidate = []
    for x in range(4):
        idx = cctv[1] + dx[x]
        idy = cctv[2] + dy[x]
        candidate = []
        while 0 <= idx < N and 0 <= idy < M :
            if not visited[idx][idy] and raum[idx][idy] == 0:
                count += 1
                candidate.append([idx, idy])
                idx += idx
                idy += idy
            elif visited[idx][idy] or raum[idx][idy]:
                break
        if count > max_count:
            max_count = count
            max_candidate = candidate[:]

    for m in max_candidate:
        visited[m[0]][m[1]] = 1

def zwei():
    dx = [1, 0]
    dy = [0, 1]
    max_candidate = []
    for x in range(2):
        idx = cctv[1] + dx[x]
        idy = cctv[2] + dy[x]
        candidate = []
        while 0 <= idx < N and 0 <= idy < M:
            if not visited[idx][]

def funf():
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(4):
        idx = cctv[1] + dx[x]
        idy = cctv[2] + dy[x]

        while idx > N-1 or idy > M-1:
            if not visited[idx][idy] and raum[idx][idy] == 0:
                visited[idx][idy] = 1
                count -= 1
                idx += idx
                idy += idy
            elif visited[idx][idy] or raum[idx][idy]:
                return

def zwei():
    # visited copy
    # idx -idx로 반전해줌
    for x in range(2):


for cctv in cctvs:
    if cctv[2] == 1:
        one_count = 0
    elif cctv[2] == 2:
        two_count = 0
    elif cctv[2] == 3:
        three_count = 0
    elif cctv[2] == 4:
        four_count = 0
    elif cctv[2] == 5:
        funf()

