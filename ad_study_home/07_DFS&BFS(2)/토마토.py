import collections

M, N = map(int, input().split())

box = [0]*N

for i in range(N):
    box[i] = list(map(int, input().split()))

queue = collections.deque([])

for i in range(N):
    for j in range(M):
        # -1은 not box[i][j] 하면 True로 나옴
        if box[i][j] == 1:
            queue.append([i, j])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
count = 0

while queue:
    count += 1
    for _ in range(len(queue)):
        temp = queue.popleft()

        for i in range(4):
            idx = temp[0]+dx[i]
            idy = temp[1]+dy[i]

            if idx < 0 or idy < 0 or idx > N-1 or idy > M-1:
                continue
            elif not box[idx][idy] and not visited[idx][idy]:
                visited[idx][idy] = 1
                queue.append([idx, idy])

def confirm():

    for i in range(N):
        for j in range(M):
            if not box[i][j] and not visited[i][j]:
                return -1

    return count-1

print(confirm())