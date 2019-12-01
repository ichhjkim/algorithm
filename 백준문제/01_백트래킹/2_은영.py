def backtrack(k, s):
    if k == M:
        for i in range(k):
            print(t[i], end=" ")
        print()
    else:
        for i in range(s, N):
            t[k] = li[i]
            backtrack(k + 1, i + 1)


N, M = map(int, '4 2'.split())
li = [i for i in range(1, 1+N)]
t = [0]*N
backtrack(0, 0)