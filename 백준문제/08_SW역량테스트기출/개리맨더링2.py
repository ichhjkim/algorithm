# N*N 5개로 나눠야 함. 반드시 5개중 한개에 포함되어야 함.
# 한 선거구에 포함되어 잇는 구역은 모두 연결되어야 함.
# 경계의 길이
N = input()

area = [ list(map(int, input())) for _ in range(N) ]

for x in range(N):
    for y in range(N):

        for d1 in range(1, N):

            for d2 in range(1, N):
                elections = [0] * 5
                if (x+d1+d2 < N) and (y-d1 >= 0) and (y+d2 < N):
                    # 선거구 1
                    for width in range(d1):
                        ty = y-width-1
                        tx = 0
                        while ty >= 0 and tx <= d2:
                            elections[0] += area[tx][ty]
                            ty -= 1
                            tx += 1

                    for i in range(x):
                        for j in range(y+1):
                            elections[0] += area[i][j]

                    # 선거구 2
                    for width in range(d1):
                        ty = y+width+1
                        tx = 0
                        while ty < N and tx <= d2:
                            elections[1] += area[tx][ty]
                            ty += 1
                            tx += 1

                    for i in range(x):
                        for j in range(y+1, N):
                            elections[1] += area[i][j]

                    # 선거구 3
                    for


