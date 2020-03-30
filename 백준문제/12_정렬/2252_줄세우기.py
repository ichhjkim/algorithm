import collections
N, M = map(int, input().split())
arr = []
degree = [0]*N
graph = [[] for _ in range(N)]
queue = collections.deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    degree[b-1] += 1

for i in range(N):
    # 뒷 순서로 호출된적이 없는 애들
    if not degree[i]:
        queue.append(i)

while queue:
    stu = queue.popleft()
    # 앞순서인 애들이 queue
    # 뒷 순서끼리 순서를 정해보기
    for j in graph[stu]:
        # 뒷순서로 호명될때마다 기존에 더해졌떤 수 감소
        degree[j] -= 1
        if not degree[j]:
            # 그런 순서가 0이 되었을 때
            queue.append(j)


    print(stu+1, end=" ")







