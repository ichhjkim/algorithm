N = int(input())

see = [list(map(int, input().split())) for _ in range(N)]

shark = 0
fish = []
for i in range(N):
    for j in range(N):
        if see[i][j] == 9:
            shark = [i, j, 2]
        elif see[i][j]:
            fish.append([i, j, see[i][j]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = 0

