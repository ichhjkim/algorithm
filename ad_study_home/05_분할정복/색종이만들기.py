def search(a, b, c, d, N):
    global count
    result = 0
    for i in range(a, b):
        for j in range(c, d):
            result += arr[i][j]

    if not result or result == N*N:
        count += 1
    else:
        search(a, b//2, a, b//2, N//2)
        search(a, b//2, b//2, b, N//2)
        search(b//2, b, a, b//2, N//2)
        search(b//2, b, b//2, b, N//2)


N = int(input())

arr = [0]*N

for i in range(N):
    arr[i] = list(map(int, input().split()))

count = 0
search(0, N, 0, N, N)
print(count)