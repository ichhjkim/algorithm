def choice(num, count, visited):
    # count 값도 백트래킹 하기 전 값으로 해줘야함.
    ori_count = count

    if count == M:
        # mis 인덱스에 넣기 위한 것. mins 인덱스 한칸씩 증가시키기 위함. append를 최대한 안쓰기 위한 나의노력...
        calculated(visited)

    else:
        for l in range(num, len(chicken)):
                visited[l] = 1
                choice(l+1, count+1, visited)
                visited[l] = 0

def calculated(visited):
    global results
    result = 0
    for h in range(len(houses)):
        semi_result = 1000
        for c in range(len(chicken)):
            if visited[c] == 1:
                d = abs(chicken[c][0]-houses[h][0]) + abs(chicken[c][1]-houses[h][1])
                if semi_result > d:
                    semi_result = d

        result += semi_result

    if results > result:
        results = result

    return
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
houses = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i+1, j+1])

        elif city[i][j] == 2:
            chicken.append([i+1, j+1])


visited = [0] * len(chicken)
count = 0
num = 0
results = 10000000
choice(num, count, visited)
print(results)






