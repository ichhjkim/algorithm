def combination(depth, area, start):
    global min_result

    if depth == election:
        visited = [0] * (N + 1)
        DFS(area[0], visited, area)
        selected = left(area)
        if confirm(area, visited):
            selected = left(area)
            visited = [0]*(N+1)
            DFS(selected[0], visited, selected)
            if confirm(selected, visited):
                one_e = 0
                for a in area:
                    one_e += population[a]
                two_e = 0
                for s in selected:
                    two_e += population[s]

                if abs(one_e - two_e) < min_result:
                    min_result = abs(one_e-two_e)

    else:
        for i in range(start, N+1):
            combination(depth+1, area+[i], i+1)

def DFS(v, visited, area):

    visited[v] = 1
    for j in city[v]:
        if j in area and not visited[j]:
            DFS(j, visited, area)

def confirm(list_a, visited):

    for a in list_a:
        if not visited[a]:
            return False

    return True

def left(area):

    selected = []
    for i in range(1, N+1):
        if i in area:
            continue
        else:
            selected.append(i)

    return selected


N = int(input())

population = [0] + list(map(int, input().split()))
city = [0]*(N+1)
min_result = 10000000000000000000000
for i in range(1, N+1):
    city[i] = list(map(int, input().split()))[1:]

# 부분집합 컷해주면 되겠네
for election in range(1, N//2+1):
    combination(0, [], 1)


if min_result == 10000000000000000000000:
    print(-1)
else:
    print(min_result)