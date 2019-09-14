def BFS(m, n):

    while

def islands(h, w):
    landers = []
    queue = [[h, w]]
    while queue:
        t = queue.pop(0)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for r in range(4):
            idx = t[0] + dx[r]
            idy = t[1] + dy[r]

            if idx < 0 or idy < 0 or idx > height-1 or idy > width-1:
                continue
            elif map[idx][idy] =='L' and not visited[idx][idy]:
                visited[idx][idy] = 1
                landers.append([idx, idy])
                queue.append([idx, idy])

    return landers

height, width= map(int, input().split())
map = [input() for _ in range(height)]
visited = [[0]*width for _ in range(width)]
result = []
for h in range(height):
    for w in range(width):
        if map[h][w] == 'L' and not visited[h][w]:
            temp_lander = islands(h, w)





