max_result = 0
def solution(road, n):
    answer = -1
    not_paved = []
    road = list(map(int, road))

    for i in range(len(road)):
        if not road[i]:
            not_paved += [i]

    visited = [0]*len(not_paved)
    temp = road[:]
    n = min(n, len(not_paved))
    def comb(depth, n, visited, not_paved, road):
        global max_result
        if depth == n:
            ori = road[:]
            for i in range(len(visited)):
                if visited[i]:
                    ori[not_paved[i]] = 1

            result = 0
            mid_result = 0
            for r in ori:
                if r:
                    result += 1
                else:
                    mid_result = max(mid_result, result)
                    result = 0

            mid_result = max(mid_result, result)
            max_result = max(max_result, mid_result)

            road = ori[:]
            return mid_result
        else:
            for x in range(len(not_paved)):
                if not visited[x]:
                    visited[x] = 1
                    comb(depth + 1, n, visited, not_paved, road)
                    visited[x] = 0

    comb(0, n, visited, not_paved, temp)


    return max_result




print(solution("111011110011111011111100011111"	, 3))