N = int(input())

idx_one = []
for i in range(N):
    idx_one.append([i]+list(map(int, input().split()))+[0])

for i in range(N):
    bigger = 1
    for j in range(N):
        if idx_one[i][1] < idx_one[j][1] and idx_one[i][2] < idx_one[j][2]:
            bigger += 1

    idx_one[i][3] = bigger

idx_one.sort()
for f in range(N):
    print(idx_one[f][3], end=' ')






