def solution(n, lost, reserve):
    answer = 0
    stu = [1]*n
    for l in lost:stu[l-1] -= 1
    for r in reserve:stu[r-1] += 1
    for x in range(n):
        if not stu[x]:
            if x > 0 and stu[x-1] > 1:
                stu[x-1] -= 1
                answer += 1
            elif x+1 < n and stu[x+1] > 1:
                stu[x+1] -= 1
                answer += 1
        else:
            answer += 1
    return answer