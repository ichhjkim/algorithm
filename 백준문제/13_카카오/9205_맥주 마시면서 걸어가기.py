# 현재 위치 각 1000 이하 선택
# 거기에서 1000이하 또 선택
T = int(input())

for _ in range(T):

    N = int(input())

    nodes = [0]*(N+2)
    for _ in range(N+2):
        nodes[_] = list(map(int, input().split()))

    road = [[0]*(N+2) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+2):
            if i != j:
                d = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
                if d <= 1000:
                    road[i][j] = 1

    queue = []
    visited = [0] * (N + 2)
    for i in range(N+2):
        if road[0][i]:
            queue.append(i)
            visited[i] = 1

    flag = False
    while queue:

        for _ in range(len(queue)):
            t = queue.pop(0)

            if t < N+1:
                for i in range(N+2):
                    if road[t][i] and not visited[i]:
                            queue.append(i)
                            visited[i] = 1
            else:
                flag = True
                break

    if flag:
        print('happy')
    else:
        print('sad')

#117744	248