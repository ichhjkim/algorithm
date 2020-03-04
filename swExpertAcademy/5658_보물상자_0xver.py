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

    final = [int('0x'+x, 16) for x in set(result)]
    final.sort(reverse=True)
    print('#{} {}'.format(t, final[K-1]))