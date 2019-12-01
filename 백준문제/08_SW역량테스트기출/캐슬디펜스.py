def backtrack(map, visited, arrow, m):
    choice = [0, 1]
    # # 백트래킹 할 때마다 다시 원상복귀 시켜줄...
    # copy_map = map[:]
    if arrow == 3:
        loca_arrow = []
        for i in range(M):
            if visited[i]:
                loca_arrow.append([N, i])
        distance(loca_arrow)

    ori_m = m
    ori_arrow = arrow
    for i in range(m, M):
        for c in range(2):
            visited[i] = choice[c]
            if visited[i]:
                arrow += 1
                m = i+1
                backtrack(map, visited, arrow, m)
                m = ori_m
                # 다시 원상복귀
                # 궁수의 수를 원래 참트로 만들기 전의 궁수의 수로
                arrow = ori_arrow
                # map에도 표시해주기 전으로
                visited[i] = 0


# 적의 위치를 찾아줌.
def enemylocation():
    global map
    global locations
    for s in range(N):
        for g in range(M):
            if map[s][g] == 1:
                locations.append([s, g])

    return locations
# 적 1씩 증가


def enemy_move(enemy_loca):
    temper = []
    for e in enemy_loca:
        if e[0]+1 < N:
            e[0] += 1
        elif e[0]+1 == N:
            temper.append(e)

    for t in temper:
        enemy_loca.remove(t)


#거리구하고 적 지우기 작업
def distance(loca_arrow):
    global results
    result = 0
    enemy_loca = enemylocation()
    while enemy_loca:
        temper = []
        for arrow in loca_arrow:
            min_enemy = 50
            mindistance = D+6
            remove_e = 0
            for e in enemy_loca:
                if D >= abs(arrow[0]-e[0]) + abs(arrow[1]-e[1]):
                    if mindistance > abs(arrow[0]-e[0]) + abs(arrow[1]-e[1]):
                        mindistance = abs(arrow[0]-e[0]) + abs(arrow[1]-e[1])
                        remove_e = e
                        min_enemy = e[1]
                    elif mindistance == abs(arrow[0]-e[0]) + abs(arrow[1]-e[1]):
                        if min_enemy > e[1]:
                            min_enemy = e[1]
                            remove_e = e

            # min_enemy의 값이 바뀌었다는 건 한명이라도 제한 거리 내 적이 있었다는 의미
            if remove_e:
                if remove_e not in temper:
                    result += 1
                    temper.append(remove_e)
                # 해당 백트래킹 내에 있는 result 값을 올려줌
        else:
            for t in temper:
                enemy_loca.remove(t)

            enemy_move(enemy_loca)

    return results.append(result)


N, M, D = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
# 궁수와 성을 놓을 N번째 인덱스 추가
map += [[0]*M]
# 궁수가 있을 위치를 결정해줄...
visited = [0] * M
# 궁수가 죽인 적의 수들의 모음
results = []
m = 0
# 적의 위치를 찾아줌.
locations = []
arrow = 0
### 실행 시작
# 적의 위치를 찾는 것으로 시작

backtrack(map, visited, arrow, m)

print(max(results))