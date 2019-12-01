def zipping(a, b, c, d, M):
    global result

    cnt = 0
    if M == 1:
        result.append(str(video[a][c]))
    else:
        for i in range(a, b):
            for j in range(c, d):
                cnt += video[i][j]

        if not cnt:
            result.append('0')
        elif cnt == M**2:
            result.append('1')
        else:
            result.append('(')
            zipping(a, (a+b)//2, c, (c+d)//2, M//2)
            zipping(a, (a + b) // 2, (c + d) // 2, d, M // 2)
            zipping((a+b)//2, b, c, (c+d)//2, M//2)
            zipping((a+b)//2, b, (c+d)//2, d, M//2)
            result.append(')')

N = int(input())
video = []
result = []
for _ in range(N):
    video.append(list(map(int, input())))

zipping(0, N, 0, N, N)
print(''.join(result))