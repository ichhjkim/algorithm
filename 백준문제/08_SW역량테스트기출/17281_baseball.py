N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]

# 타자가 서는 순서를 정해야 하고, 경기중에는 변경 안됨
players = list(range(0, 8))
temp_c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
max_result = -1
# s는 4부터 시작, depth 3부터 시작, candi = [0, 1, 2, 3, 0]
p_visited = [1, 0, 0, 0, 0, 0, 0, 0, 0]
def combi(depth, candi):
    global max_result

    if depth == 9:
        candi = candi[:]
        res = play(candi)
        if max_result < res:
            max_result = res
    elif depth == 3:
        combi(depth+1, candi)
    else:
        # 4, 5,6, 7, 8까지만 결정하면 됨
        for i in range(1, 9):
            if not p_visited[i] :
                candi[depth] = i
                p_visited[i] = 1
                combi(depth+1, candi)
                p_visited[i] = 0


def play(candi):
    global N
    # 9명 // 수비 공격 번갈아
    # N 이닝동안 게임 진행,
    stage = -1
    result = 0

    while stage < N-1:
        stage += 1
        visited = [0, 0, 0]
        out = 0
        while out < 3:
            temp = candi.pop(0)
            # 아웃인 경우
            if scores[stage][temp] == 0:
                out += 1

            elif scores[stage][temp] == 1:
                result += visited[2]
                visited[2] = visited[1]
                visited[1] = visited[0]
                visited[0] = 0
                visited[0] += 1

            elif scores[stage][temp] == 2:
                result += visited[2]
                result += visited[1]
                visited[2] = 0
                visited[1] = 0
                visited[2] = visited[0]
                visited[0] = 0
                visited[1] += 1

            elif scores[stage][temp] == 3:
                for i in range(2, -1, -1):
                    result += visited[i]
                    visited[i] = 0
                visited[2] += 1
            else:
                for i in range(2, -1, -1):
                    result += visited[i]
                    visited[i] = 0
                result += 1
            candi.append(temp)


    return result

combi(0, temp_c)
print(max_result)