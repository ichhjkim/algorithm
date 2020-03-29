N, M, R, G = map(int, input().split())
garden = [list(map(int,input().split())) for _ in range(N)]



# 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅
lands = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(N):
        if garden[i][j] == 2:
            lands.append([i, j])

green_red = [G, R]
depth_sum = R+G
# 봄
def Combi(depth, s, result):

    if depth == depth_sum:

    else:
        for i in range(s, len(lands)):
            result[depth] = lands[i]













# 봄이 아닐때, time


# 꽃의 최대 값

