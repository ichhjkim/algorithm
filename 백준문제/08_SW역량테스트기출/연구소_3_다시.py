import collections

def BFS(selected):
    global min_count, flag

    selected = collections.deque(selected)
    visited = [[0] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(M):
        visited[selected[i][0]][selected[i][1]]=1
    count = 0
    flag_count = False
    while selected:


def combination(st, depth, selected):
    if depth == M:
        BFS(selected)

    else:
        for i in range(st, len(virus)):
            selected[depth] = virus[i]
            combination(i+1, depth+1, selected)

N, M = map(int, input().split())

research = [0]*N

for i in range(N):
    research[i] = list(map(int, input().split()))

virus = []
min_count = 10000000000000000
for i in range(N):
    for j in range(N):
        if research[i][j] == 2:
            virus.append([i, j])

flag = False
combination(0, 0, [0]*M)
