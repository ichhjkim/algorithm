# 16진수 숫자(0-10A, 11B, 12C, 13D 14E 15F

# 보물상자의 뚜껑은 시계방향으로 돌릴 수 있고,
# 한번 돌리때마다 숫자가 시계 방향으로 한칸씩 회전

# 각 변에는 동일한 갯수의 숫자
# 시계방향 순으로 높은 자리 숫자에 하나의 수를 나타낸다.

# 보물상자의 비밀번호는 보물상자에 적힌 숫자로 만들 수 있는 모든 수중
# K번째로 큰 수를 10진수로 만든 수
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = input()
    result = [0]*N
    # 4의 배수로 어찌어찌하면..
    # 3회전 == 0 회전 => N//4 마다 동일
    q = N//4
    # 나머지 q-1
    count = 0
    for i in range(q-1, -1, -1):
        result[count*4] = nums[q*0+i:q*1+i]
        result[count*4+1] = nums[q*1+i:q*2+i]
        result[count*4+2] = nums[q*2+i:q*3+i]
        if q != 0:
            result[count*4+3] = nums[q*3+i:]+nums[:q*0+i]
        else:
            result[count*4+3] = nums[q*3:]
        count += 1

    result = list(set(result))
    final = [0]*len(result)
    calcul = [0]*q
    for c in range(q):
        calcul[c] = 16**c
    # print(result)
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
    # print(final)
    print('#{} {}'.format(t, final[K-1]))






