# N*N 크기 땅 구매
# # r-1, c-1
# # 모든 칸에 처음은 양분이 5
# # 나무의 갯수 M
# # 같은 칸에 여러개 나무 가능




#K년이 지난후 상도의 땅에 살아있는 나무의 개수///!

N, M, K = map(int, input().split())

plusfeed = [list(map(int, input().split())) for _ in range(N)]
trees = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        trees[i][j] = []

for i in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

feed = [[5]*N for _ in range(N)]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

# # 봄
# # 나무가 자신의 나이 만큼 양분을 먹고. 나이가 1증가
# 하나의 칸에 여러개의 나무가 있으면 나이가 어린 나무부터 양분을 먹음
# 양분이 없어서 자신의 나이만큼 양분 못먹으면 바로 죽음


# 가을 --> 나무 번식
# 번식할 수 있는 나무는 나이가 5의 배수
# 8칸에 나이가 1인 나무가 생긴다.
# 땅을 벗어나는 칸에는 나무가 생기지 않는다.




# 겨울 양분이 추가 /// 각칸에 추가되는 양분의 양은 A[r][c] 이고, 입력으로 주어짐



def time(K):
    global trees

    while K:
        for x in range(N):
            for y in range(N):
                if trees[x][y]:
                    trees[x][y].sort()
                    discard = 0
                    new = []

                    for f in range(len(trees[x][y])):
                        if (feed[x][y] - trees[x][y][f]) >= 0:
                            feed[x][y] -= trees[x][y][f]
                            trees[x][y][f] += 1
                            new.append(trees[x][y][f])
                        else:
                            discard += trees[x][y][f] // 2

                    # 여름 : 죽은 나무의 나이가 양분, 나이의 //2
                    feed[x][y] += discard
                    trees[x][y] = new[:]

        for x in range(N):
            for y in range(N):
                feed[x][y] += plusfeed[x][y]
                if trees[x][y]:

                    for f in range(len(trees[x][y])):
                        if not trees[x][y][f] % 5:

                            for i in range(8):
                                idx = x + dx[i]
                                idy = y + dy[i]
                                if idx >= 0 and idx <= N - 1 and idy >= 0 and idy <= N - 1:
                                    trees[idx][idy].append(1)

        K-= 1

    result = 0
    for x in range(N):
        for y in range(N):

            if trees[x][y]:
                result += len(trees[x][y])

    return result

print(time(K))


