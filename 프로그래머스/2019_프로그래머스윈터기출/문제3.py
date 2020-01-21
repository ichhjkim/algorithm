from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(land, height):
    answer = 0
    visited = [[0]*len(land[0]) for _ in range(len(land[0]))]
    queue = deque([[0, 0]])
    visited[0][0] = 1
    while queue:
        over = []
        flag = True
        for _ in range(len(queue)):
            temp = queue.popleft()

            for x in range(4):
                idx = temp[0] + dx[x]
                idy = temp[1] + dy[x]

                if idx < 0 or idy < 0 or idx > len(land[0])-1 or idy > len(land[0])-1:
                    continue
                elif abs(land[temp[0]][temp[1]]-land[idx][idy]) <= height and not visited[idx][idy]:
                    queue.append([idx, idy])
                    visited[idx][idy] = 1
                    flag = False
                elif abs(land[temp[0]][temp[1]]-land[idx][idy]) > height and not visited[idx][idy]:

                    for xx in range(4):
                        cx = idx + dx[xx]
                        cy = idy + dy[xx]

                        if cx < 0 or cy < 0 or cx > len(land[0])-1 or cy > len(land[0])-1:
                            continue
                        elif abs(land[idx][idy]-land[idx][idy]) <= height:
                            break

                    else:
                        over.append([abs(land[temp[0]][temp[1]]-land[idx][idy]), idx, idy])

        if not queue and over:
            over.sort()
            print(over)
            answer += over[0][0]
            queue.append([over[0][1], over[0][2]])


    return answer
print(solution([[1, 4, 8, 10],
                [5, 5, 5, 5],
                [10, 10, 10, 10],
                [10, 10, 10, 20]], 3))