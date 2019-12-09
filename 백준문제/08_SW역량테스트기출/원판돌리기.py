# 원판의 반지름이 i면, i번째 원판이라고 한다.

# i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다.

# 주의 (i, 1) -- (i,2)/(i, M)
# (i, M) -- (i, 1)/(i, M-1)
import collections
N, M, T = map(int, input().split())

nums =[collections.deque(map(int, input().split())) for _ in range(N)]
rotations = [list(map(int, input().split())) for _ in range(T)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x, d, k in rotations:
    for i in range(N):
        if not (i+1) % x:
            if d:# 반시계방향
             count = k
             while count:
                 temp = nums[i].popleft()
                 nums[i].append(temp)
                 count -= 1

            else:
                count = k
                while count:
                    temp = nums[i].pop()
                    nums[i].appendleft(temp)
                    count -= 1

    same = True
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        f = True
        for j in range(M):
            flag = True
            if nums[i][j]:
                for m in range(4):
                    idx = i + dx[m]
                    idy = j + dy[m]

                    if idx <= N-1 and idx >= 0:
                        if idy < 0: idy=M-1
                        if idy > M-1:idy=0
                        if nums[i][j] == nums[idx][idy]:
                            visited[idx][idy] = 1
                            visited[i][j] = 1
                            flag = False
                            same= False

            if not flag:
                nums[i][j] = 0
                f = False

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                nums[i][j] = 0

    if same:
        result = 0
        c = 0
        for i in range(N):
            for j in range(M):
                if nums[i][j]:
                    result += nums[i][j]
                    c += 1
        if c:
            avg = result/c
        else:
            avg = 0
        for i in range(N):
            for j in range(M):
                if nums[i][j]:
                    if avg < nums[i][j]:
                        nums[i][j] -= 1
                    elif avg > nums[i][j]:
                        nums[i][j] += 1

final = 0
for i in range(N):
    final += sum(nums[i])
print(final)


