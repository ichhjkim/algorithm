# 1
# 0
# 2
# 0 0 1
# 3
# 0 0 1 0 0 1 1
# 4
# 0 0 1 0 0 1 1 0 0 0 1 1 0 1 1
# 5
# 0 0 1 0 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 0 1 1 0 1 1

def solution(n):
    if n > 1:
        answer = [0]*(2**n-1)
        flag = 0
        b = solution(n-1)
        cnt = 0
        for i in range(len(answer)):
            if not i % 2:
                if not flag:
                    answer[i]= flag
                    flag = 1
                else:
                    answer[i] = flag
                    flag = 0
            else:
                answer[i] = b[cnt]
                cnt += 1

        return answer

    else:
        return [0]

print(solution(3))