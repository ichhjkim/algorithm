ary = [ [ 9, 20, 2, 18, 11 ],
	[ 19, 1, 25, 3, 21 ],
	[ 8, 24, 10, 17, 7 ],
	[ 15, 4, 16, 5, 6 ],
	[ 12, 13, 22, 23, 14 ] ]

sorted_ary = [[0]*5 for _ in range(5)]


def sel_mic(ary):
    minX, minY = 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j
                print(minX, minY)

    min = ary[minX][minY]
    print(min)
    ary[minX][minY] = 99
    for _ in range(5):
        print(ary[_], '원본의 정렬')

    return min


def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    if sorted_ary[x][y] != 0:
        return True
    return False

X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
#   오른쪽 아래 왼쪽 위
dir_stat = 0


for i in range(25):
    cur_min = sel_mic(ary)
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if isWall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]

for i in range(5):
    print(sorted_ary[i])
