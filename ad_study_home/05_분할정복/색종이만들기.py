def search(a, b, c, d, M):
    global white, blue

    result = 0
    if M == 1:
        if not arr[a][c]:
            white += 1
        else:
            blue += 1
    else:
        for i in range(a, b):
            for j in range(c, d):
                result += arr[i][j]

        if not result:
            white += 1
        elif result == M**2:
            blue += 1
        else:
            search(a, (a+b)//2, c, (c+d)//2, M//2)
            search(a, (a+b)//2, (c+d)//2, d, M//2)
            search((a+b)//2, b, c, (c+d)//2, M//2)
            search((a+b)//2, b, (c+d)//2, d, M//2)


N = int(input())

arr = [0]*N

for i in range(N):
    arr[i] = list(map(int, input().split()))

white = blue = 0
search(0, N, 0, N, N)
print(white)
print(blue)