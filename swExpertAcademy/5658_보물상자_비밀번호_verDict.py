T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = input()
    result = [0]*N
    q = N//4
    res = {}
    for i in range(q-1, -1, -1):
        res.setdefault(nums[q*0+i:q*1+i], 0)
        res.setdefault(nums[q*1+i:q*2+i], 0)
        res.setdefault(nums[q*2+i:q*3+i], 0)

        if q != 0:
            res.setdefault(nums[q*3+i:]+nums[:q*0+i], 0)
        else:
            res.setdefault(nums[q*3:], 0)

    result = [k for k in res.keys()]
    final = [0]*len(result)
    calcul = [0]*q
    for c in range(q):
        calcul[c] = 16**c
    for x in range(len(result)):

        for i in range(q):
            if result[x][i] == 'A':
                temp = 10
            elif result[x][i] == 'B':
                temp = 11
            elif result[x][i] == "C":
                temp = 12
            elif result[x][i] =='D':
                temp = 13
            elif result[x][i] =='E':
                temp = 14
            elif result[x][i] == 'F':
                temp = 15
            else:
                temp = int(result[x][i])
            final[x] += calcul[q-1-i]*temp
    final.sort(reverse=True)
    print('#{} {}'.format(t, final[K-1]))