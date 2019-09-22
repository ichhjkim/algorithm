def permufunc(depth):
    global count
    if depth == 3:
        count += 1
        if count == num:
            for r in result:
                print(r, end='')
            print()
    else:
        for i in range(len(permu)):
            if not visited[i]:
                visited[i] = 1
                result[depth] = permu[i]
                permufunc(depth + 1)
                visited[i] = 0
                result[depth] = 0



permu = list(map(int, input().split()))
num = int(input())
visited = [0] * len(permu)
permu.sort()
result = [0] * len(permu)
depth = 0
count = 0
permufunc(0)