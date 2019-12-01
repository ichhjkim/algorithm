import collections

def BFS(count):
    while queue:
        count += 1
        for _ in range(len(queue)):
            temp = queue.popleft()

            for x in range(4):
                idx = temp[0] + dx[x]
                idy = temp[1] + dy[x]

                if idx < 0 or idy < 0 or idx > N - 1 or idy > M - 1:
                    continue
                elif maze[idx][idy] == '1' and not visited[idx][idy]:
                    if idx == N-1 and idy == M-1:
                        return count
                    visited[idx][idy] = 1
                    queue.append([idx, idy])

N, M = map(int, input().split())
maze = [0]*N
for i in range(N):
    maze[i] = input()
visited = [[0]*M for _ in range(N)]

# (0, 0)에서 시작해서 (N-1, M-1)칸에 도착해야함

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = collections.deque([[0, 0]])
visited[0][0] = 1

print(BFS(1))






