N, M = map(int, input().split())

lands = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
islands = []
# 범위 확인
def is_wall(i, j):
    if 0 <= i < N and 0<= j < M:
        return True
    else:
        return False

def distance(i, j):
    candidates = []
    for d in range(4):
        idx = i + dx[d]
        idy = j + dy[d]
        count = 0
        while islands(idx, idy) and not lands[idx][idy]:

            idx += dx[d]
            idy += dy[d]

            count += 1

        if count >= 2:
            candidates.append(count)


for i in range(N):
    for j in range(M):
        if lands[i][j]:

