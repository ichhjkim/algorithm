

# 배열 A[r-1][c-1] === k인 최소 값
#
r, c, k = map(int, input().split())
# r-1, c-1
r -= 1
c -= 1
# 크기 3*3
board = [list(map(int, input().split())) for _ in range(3)]

def solution(board):

    time = 0
    # 100을 넘어가는 경우
    while time <= 100:

        for x in range(len(board)):
            for y in range(len(board[0])):
                if x == r and y==c and board[r][c]==k :
                    return time
        #for q in range(len(board)):
        #    print(board[q])
        #print('----------------------')
        # 행과 열의 크기 비교
        # R 연산 : 배열 A의 모든 행에 대해 정렬 수행 // 행의 개수 >= 열의 갯수
        # C 연산 : 모든 열에 대해 정렬 수행 // 행의 갯수 < 열의 개수
        if len(board) >= len(board[0]):
           temp_board =  R(board)
           for i in range(len(temp_board)):
                board[i] = temp_board[i][:]
           #for q in range(len(board)):
           #    print(board[q])
           #print('-------R연산 후---------------',time)
        else:
            temp = C(board)
            board = temp

            #for q in range(len(board)):
            #    print(board[q])
            #print('-------C연산후 후---------------', time)



        # 1초가 지날때 마다 배열에 연산 적용
        time += 1

    return -1





def R(board):
    # 행
    width = len(board[0])
    # 열
    height = len(board)
    temp = [[] for _  in range(height)]
    maxlen = 0

    for i in range(height):
        new = [0]*10001
        for j in range(width):
            # 수 정렬시 0은 무시
            if board[i][j]:
                ## 각각 수가 몇번 나왔는지 알아야 함.
               # print(board[i][j])
                new[board[i][j]] += 1

                # 수의 등장 횟수가 큰 순으로 오름차순순
                # 등장 횟수가 동일하면 수 자체가 큰 수로 오름차순

        t = []
        for num in range(1, 10001):
            if new[num]:
                t.append([new[num], num])

        t.sort()
        #행 또는 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지는 버린다
        maxrange = 0
        if maxlen < len(t)*2 :
            if len(t)*2 < 101:
                maxlen = len(t)*2
            else:
                maxlen = 100
        if len(t)*2 < 101:
            maxrange = len(t)*2
        else:
            maxrange = 100
        # 순서는 [수, 횟수] 순으로 넣기
        for lent in range(maxrange//2):
            temp[i].append(t[lent][1])
            temp[i].append(t[lent][0])

    for i in range(height):
        if len(temp[i]) < maxlen:
            temp[i] += [0]*(maxlen - len(temp[i]))

    # 정렬된 배열을 다시 넣으면 행/ 열이 커짐
    # 가장 큰 배열의 크기 기준
    return temp


# 순서는 [수, 횟수] 순으로 넣기
# 정렬된 배열을 다시 넣으면 행/ 열이 커짐
# 가장 큰 배열의 크기 기준
# 수 정렬시 0은 무시
# 행 또는 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지는 버린다


def C(board):
    # 행
    width = len(board[0])
    # 열
    height = len(board)
    temp = [[] for _ in range(width)]
    maxlen = 0
    for i in range(width):
        new = [0]*10001
        for j in range(height):
            # 수 정렬시 0은 무시
            if board[j][i]:
                ## 각각 수가 몇번 나왔는지 알아야 함.
                new[board[j][i]] += 1

        t = []
        for num in range(1, 10001):
            if new[num]:
                t.append([new[num], num])
        # 수의 등장 횟수가 큰 순으로 오름차순순
        # 등장 횟수가 동일하면 수 자체가 큰 수로 오름차순
        t.sort()

        maxrange = 0
        # 행 또는 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지는 버린다
        maxrange = 0
        if maxlen < len(t) * 2:
            if len(t) * 2 < 101:
                maxlen = len(t) * 2
            else:
                maxlen = 100
        if len(t) * 2 < 101:
            maxrange = len(t) * 2
        else:
            maxrange = 100
        for lent in range(maxrange//2):
            temp[i].append(t[lent][1])
            temp[i].append(t[lent][0])

    for i in range(len(temp)):
        if len(temp[i]) < maxlen:
            temp[i] += [0]*(maxlen-len(temp[i]))

    final = [[0]*len(temp) for _ in range(maxlen)]
    for fi in range(maxlen):
        for fj in range(len(temp)):
            final[fi][fj] = temp[fj][fi]

    return final


print(solution(board))
