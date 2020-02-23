# R*C 격자판 헹/열
R, C, M = map(int, input().split())

# 상어의 정보
shark = [0]*M
see = [[0]*C for _ in range(R)]


for i in range(M):
    x, y, s, d, z = map(int, input().split())
    shark[i] = [x-1, y-1, s, d, z]


# 한칸에는 상어가 최대 한마리
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def work():
    which = -1
    # 낚시왕은 -1 열부터 시작해서 len(열)이 인덱스가 되면 멈춤
    while which < C:
        # 낚시왕이 오른쪽으로 한칸 감
        which += 1
        ## 1초 동안 일어나는일
        # 해당 열에 있는 상어중 땅과 제일 가까운 상어를 잡음
        min_shark = 999999
        the_index = 999999
        for x in range(M):
            if shark[x][1] == which:
                if min_shark > shark[x][0]:
                    min_shark = shark[x][0]
                    the_index = x
        # 잡으면 상어 사라짐
        if the_index < 999999:
            shark.pop(the_index)

        # 상어 이동
        # 상어의 속도는 칸/초 1초 상어가 이동하려고 하는 칸이
        # 격자판의 경계인ㅇ 경우.. 이동 방향 반대로 바뀜
        for x in range(M):
            # 위/이래/오른/왼
            if shark[x][3]==0:
                idx = shark[x][0] + dx[0]
                idy = shark[x][1] + dy[0]

                if idx < 0 or idy < 0 or idx > R-1 or idx > C-1:
                    shark[x][3] = 1

        # 상어가 이동을 마친 후에 상어가 두마리 이상 가능 이따 크기가 큰 상어가 나머지 상
        #sort 쓰먄 됨






