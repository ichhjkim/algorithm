N = int(input())
K = int(input()) # 사과 갯수

board = [[0]*N for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 3

L = int(input())
rotate = [0]*L #

for i in range(L):
    X, C = input().split()
    rotate[i] = [int(X), C]

snake = [[0, 0]]


# 벽을 만나거나 자신을 만나면 안댐
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1

def move(result):

    direction = [0, 1]
    result = 0
    i = 0
    while True:
        result += 1
        temp = [snake[0][0]+direction[0], snake[0][1]+direction[1]]

        if temp[0] < 0 or temp[0] > N-1 or temp[1] <0 or temp[1] > N-1:
            return result
        if visited[temp[0]][temp[1]]:
            return result

        snake.insert(0, temp)

        if board[temp[0]][temp[1]] == 3 and not visited[temp[0]][temp[1]]:
            board[temp[0]][temp[1]] = 0
            visited[temp[0]][temp[1]] = 1

        if not board[temp[0]][temp[1]] and not visited[temp[0]][temp[1]]:
            visited[temp[0]][temp[1]] = 1
            x, y = snake.pop()
            visited[x][y] = 0

        if rotate and (rotate[i][0]==result):
            if rotate[i][1] == "L":
                if not direction[0]:
                    direction[0], direction[1] = -direction[1], direction[0]
                else:
                    direction[0], direction[1] = direction[1], direction[0]

            elif rotate[i][1] == 'D':
                if not direction[0]:
                    direction[0], direction[1] = direction[1], direction[0]
                else:
                    direction[0], direction[1] = direction[1], -direction[0]
            rotate.pop(0)

print(move(0))







