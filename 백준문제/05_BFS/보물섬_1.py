from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_result = deque([])
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visited= [[0]*M for _ in range(N)]
            queue = deque([])
            queue.append([i, j])
            depth = -1
            visited[i][j] = 1
            while queue:
                depth += 1
                length = len(queue)
                for _ in range(length):
                    q = queue.popleft()
                    for r in range(4):
                        x = q[0]
                        y = q[1]
                        x += dx[r]
                        y += dy[r]

                        if x < 0 or y < 0 or x > N-1 or y > M-1:
                            continue
                        if not visited[x][y] and board[x][y] == 'L':
                            visited[x][y] = 1
                            queue.append([x, y])

            min_result.append(depth)

print(max(min_result))