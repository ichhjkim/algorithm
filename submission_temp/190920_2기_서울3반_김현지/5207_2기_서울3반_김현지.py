T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    AB = [0, 0]
    for _ in range(2):
        AB[_] = list(map(int, input().split()))

    A = AB[0]
    B = AB[1]
    A.sort()

    middle = (0+len(A)-1)//2
    l = 0
    r = len(A)-1
    count = 0
    # print(tc)
    for b in range(M):
        if B[b] not in A:
            continue

        if B[b] < A[middle]:
            if B[b] >= A[(l+middle-1)//2]:

                count += 1
                # print(B[b], A[(l + middle - 1) // 2], count, 'left')

        elif B[b] > A[middle]:
            if B[b] <= A[(middle + 1 + r)//2]:
                # print((middle + 1 + r)//2)
                count +=1

        elif B[b] == A[middle]:
            # print(b, B[b], '중간')
            count += 1

    print('#{} {}'.format(tc, count))