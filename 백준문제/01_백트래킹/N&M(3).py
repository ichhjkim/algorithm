def permu_repet(arr, depth, m):
    global count
    if depth == M:
        count += 1
        for a in arr:
            print(a, end=' ')
        print()
    else:
        for i in range(m, N+1):
            ar = arr[:]
            ar.append(i)
            permu_repet(ar, depth + 1, i)

N, M = map(int, input().split())
count = 0
visited = [0] * N

permu_repet([], 0, 1)



