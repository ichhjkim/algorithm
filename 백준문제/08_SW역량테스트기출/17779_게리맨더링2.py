# N*N
# (r, c)로 구역
# 선거구는 5개, 구역은 선거구에 포함
# 선거구는 구역 1개 이상, 한 선거구에 포함되어 있는 구역은 모두 연결되어야 함

# 기준은 위에  왼쪽으로 가는게 d1, 오른쪽으로 가는게 d2
# (x, y)

# d1+d2의 최대 길이는 N보다 작음
def is_wall(a, b):

    if a < 0 or b < 0 or a > N-1 or b> N-1:
        return False
    return True

def full(x, y):
    global visited
    x+=1
    for i in range(N):
        visited[i] = visited[i][:]
    while not visited[x][y]:
        visited[x][y] = 1
        x += 1


def oneelect(i, j, d1):
    global visited
    allsum = 0
    for r in range(i+d1):
        for c in range(j+1):
            if not visited[r][c]:
                allsum += area[r][c]
                # visited[r][c] = 2
    # for q in range(N):
    #     print(visited[q])
    # print('=======2============')
    return allsum

def twoelect(i, j, d2):
    global visited
    allsum = 0
    for r in range(i+d2+1):
        for c in range(j+1, N):
            if not visited[r][c]:
                allsum += area[r][c]
                # visited[r][c] = 3
    # for q in range(N):
    #     print(visited[q])
    # print()
    return allsum


def threeelect(i, j, d1, d2):
    global visited
    allsum = 0
    for r in range(i+d1, N):
        for c in range(j-d1+d2):
            if not visited[r][c]:
                allsum += area[r][c]
                # visited[r][c] = 4
    # for q in range(N):
    #     print(visited[q])
    # print('----------3-----------')
    return allsum

def fourelect(i, j, d1, d2):
    global visited
    allsum = 0
    for q in range(N):
        visited[q] = visited[q][:]

    for r in range(i+d2+1, N):
        for c in range(j-d1+d2, N):
            if not visited[r][c]:
                allsum += area[r][c]
                # visited[r][c] = 5
    # for q in range(N):
    #     print(visited[q])
    # print('---------------')
    return allsum



N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
min_result = 999999
for i in range(N):
    for j in range(N):

        for x in range(1, N):
            d1 = x
            for temp in range(1, N-x):
                visited = [[0] * N for _ in range(N)]
                elects = [0] * 5
                d2 = temp
                visited[i][j] = 1
                flag = True
                # 1번 경계선, 4번 경계썬
                for t in range(d1+1):
                    (one_x, one_y) = (i+t, j-t)
                    (four_x, four_y) = (i+d2+t, j+d2-t)
                    if (not is_wall(one_x, one_y)) or not is_wall(four_x, four_y):
                        flag=False
                        break
                    visited[one_x][one_y] = 1
                    visited[four_x][four_y] = 1

                if not flag:
                    continue

                # 2번 경계선, 3번 경계선
                for t in range(d2+1):
                    (two_x, two_y) = (i+t, j+t)
                    (three_x, three_y) = (i+d1+t, j-d1+t)
                    if not is_wall(two_x, two_y) or not is_wall(three_x, three_y):
                        flag = False
                        break
                    visited[two_x][two_y] = 1
                    visited[three_x][three_y] = 1

                if not flag: continue
                # j를 빼고 더함

                for f in range(d1):
                    [one_x, one_y] = [i+f, j-f]
                    full(one_x, one_y)
                for f in range(d2):
                    [two_x, two_y] = [i+f, j+f]
                    full(two_x, two_y)

                for n in range(N):
                    for m in range(N):
                        if visited[n][m]:
                            elects[4] += area[n][m]

                elects[0] = oneelect(i, j, d1)
                elects[1] = twoelect(i, j, d2)
                elects[2]= threeelect(i, j, d1, d2)
                elects[3] = fourelect(i, j, d1, d2)


                if min(elects):

                    result = max(elects) - min(elects)

                    if min_result > result:
                        # print(result, '----------')
                        min_result = result




print(min_result)









