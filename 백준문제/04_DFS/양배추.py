T = int(input())

for tc in range(T):
    width, height, K = map(int, input().split())
    land = [[0]*width for _ in range(height)]
    visited = []
    for _ in range(K):
        a, b = map(int, input().split())
        land[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    for i in range(height):
        for j in range(width):
            if land[i][j] and ([i, j] not in visited):
                stack = [[i, j]]
                visited += [[i, j]]
                count += 1
                while stack:
                    temp = stack.pop()
                    for r in range(4):
                        x = temp[0]
                        y = temp[1]
                        x += dx[r]
                        y += dy[r]
                        if x < 0 or y < 0 or x > height-1 or y > width-1:
                            continue
                        elif land[x][y] and [x, y] not in visited:
                            stack += [[x, y]]
                            visited += [[x, y]]
    print(count)