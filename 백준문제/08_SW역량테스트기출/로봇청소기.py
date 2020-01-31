# N, M
# 동서남북
#  dx = [0, 0, 1, -1]
#  dy = [1, -1, 0, 0]
#  방향x (-1, 1,0, 0)
#  방향y (0, 0, -1, 1)

N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#   x(0, -1, 0, 1,
#   y(-1,  0,  1, 0)

r, c, d = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
robot = [r, c]
direct = [dx[d], dy[d]]
visited[robot[0]][robot[1]] = 1

def direction(direct):

    if direct[0]:
        direct[0], direct[1] = direct[1], direct[0]
    else:
        direct[0], direct[1] = -direct[1], direct[0]

    return direct

def working(direct):
    global robot
    count = 0
    result=1
    while True:
        # 왼쪽으로 돌아

        direct = direction(direct)
        # print(direct)
        new = [robot[0]+ direct[0], robot[1]+direct[1]]

        if new[0] < 0 or new[1] < 0 or new[0] > N-1 or new[1] > M-1 or visited[new[0]][new[1]] or area[new[0]][new[1]]:
            count += 1
        if not visited[new[0]][new[1]] and not area[new[0]][new[1]]:
            visited[new[0]][new[1]] = 1
            robot = new[:]
            count = 0
            result += 1

        if count == 4:
            # 후진
            if direct[0]:
                direct[0] = -direct[0]
            else:
                direct[1] = -direct[1]
            temp = [robot[0]+direct[0], robot[1]+direct[1]]

            if temp[0] < 0 or temp[1] < 0 or temp[0] > N-1 or temp[1] > M-1 or area[temp[0]][temp[1]]:
                return result
            if not visited[temp[0]][temp[1]] and not area[temp[0]][temp[1]]:
                count = 0
                visited[temp[0]][temp[1]] = 1
                robot = temp[:]
                result += 1
                if direct[0]:
                    direct[0] = -direct[0]
                else:
                    direct[1] = -direct[1]
            if visited[temp[0]][temp[1]]:
                robot = temp[:]
                count = 0
                if direct[0]:
                    direct[0] = -direct[0]
                else:
                    direct[1] = -direct[1]




print(working(direct))












