def backtrack(a):
    global midde_value, min_result

    if a >= b+1:
        if midde_value > min_result:
            midde_value = min_result


    else:
        for r in range(3):
            ori_result = min_result
            if r == 0:
                min_result += fee[r]*using[a]
                backtrack(a+1)
                min_result = ori_result
            elif r == 1:
                min_result += fee[r]
                backtrack(a+1)
                min_result = ori_result
            elif r == 2:
                min_result += fee[r]
                backtrack(a+3)
                min_result = ori_result


T = int(input())

for tc in range(1, T+1):

    fee = list(map(int, input().split()))
    using = list(map(int, input().split()))
    idx = []
    for u in range(12):
        if u == 0 and using[u]:
            idx.append(u)
        elif u+1 < 12 and not using[u+1] and using[u]:
            idx.append(u)
        elif u-1 >= 0 and not using[u-1] and using[u]:
            idx.append(u)
        elif u-1 == 10 and using[u-1] and using[u]:
            idx.append(u)

    result = 0
    visited = [0]*12

    for i in range(len(idx)):
        midde_value = 1000000000000000000000
        if i+1 < len(idx) and not visited[idx[i]]:
            min_result = 0
            visited[idx[i]] = 1
            visited[idx[i+1]] = 1
            M = idx[i+1]-idx[i]+1
            a = idx[i]
            b = idx[i+1]
            backtrack(a)
            result += midde_value


    if result > fee[3]:
        result = fee[3]

    print('#{} {}'.format(tc, result))