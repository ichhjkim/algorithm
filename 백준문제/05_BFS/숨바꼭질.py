import collections

def BFS():
    count = 0
    while queue:
        count += 1
        for _ in range(len(queue)):
            temp = queue.popleft()

            for i in range(3):
                if i == 0:
                    result = temp-1
                elif i==1:
                    result = temp+1
                else:
                    result = temp*2

                if result > -1 and result < 100001 and result != K and not visited[result]:
                    visited[result] = 1
                    queue.append(result)
                elif result == K:
                    return count

N, K = map(int, input().split())
visited = [0]*100001
queue = collections.deque([N])
if N != K:
    print(BFS())
else:
    print(0)
