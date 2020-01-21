T = int(input())

for tc in range(1, T+1):

    N, C, P = map(int, input().split())
    people = [0]*N
    problem = [0]*C
    p_score = 0
    for i in range(N):

        people[i] = list(map(int, input().split()))
        for c in range(C):
            if not people[i][c]: problem[c] += 1
    result = 1
    for c in range(C):
        p_score+= people[P-1]*problem[c]
    for j in range(N):
        if P-1 != j:
            temp = 0
            for c in range(C):
                temp += people[j]*problem[c]

            if temp > p_score:
                result += 1
            elif temp == p_score and sum(people[P-1]) < sum(people[j]):
                result += 1
            elif  temp == p_score and sum(people[P-1]) == sum(people[j]) and j < P-1:
                result += 1

    print('#{} {} {}'.format(tc, p_score, result))







