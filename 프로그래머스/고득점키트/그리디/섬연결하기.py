
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    parents = [0]*n
    visited = [0]*n
    for i in range(n): parents[i] = i
    for cost in enumerate(costs):


    return answer

def find(x, parent):

    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y, parent, visited):

    x = find(x)

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))