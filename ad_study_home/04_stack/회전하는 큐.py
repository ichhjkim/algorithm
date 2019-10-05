from collections import deque

N, M = map(int, input().split())

nums = deque(list(range(1, N+1)))

choose = deque(list(map(int, input().split())))
count = 0
while choose:
    idx = nums.index(choose[0])
    if not idx:
        nums.popleft()
        choose.popleft()
    elif abs(idx-len(nums)) >= idx:
        temp = nums.popleft()
        nums.append(temp)
        count += 1
    else:
        temp = nums.pop()
        nums.appendleft(temp)
        count += 1

print(count)