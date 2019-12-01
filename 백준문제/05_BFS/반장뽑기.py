from collections import deque
N = int(input())
candidates = [[] for _ in range(N+1)]
# DEPTH 몇에 모든 visited가 1이 되느냐
# reuslt에 후보들을 어펜드하고, sort 써야겠네
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    candidates[a] += [b]
    candidates[b] += [a]

min_depth = 100000000000000

result = deque([min_depth])
for i in range(1, N+1):
    depth = 0
    queue = deque([])
    visited = [0]*(N+1)
    queue.append(i)
    while queue:
        depth += 1
        length = len(queue)
        for _ in range(length):
            q = queue.popleft()
            if not visited[q]:
                visited[q] = 1
                queue.extend(candidates[q])

        for r in range(1, N+1):
            if not visited[r]:
                break

        else:
            if min_depth > depth:
                min_depth = depth
                for _ in range(len(result)):
                    result.popleft()
                result.append(i)
            elif min_depth == depth:
                result.append(i)

        if min_depth < depth:
            break

print(min_depth-1, len(result))
for _ in range(len(result)):
    print(result[_], end=' ')


