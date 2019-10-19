def confirm_odd(s, result):

    # 두개를 선택할 것인가
    if s > N-1:
        print(result)
    # 한개를 선택할 것인가

    # s == 0에서 시작
    else:
        for i in range(s, N, 2):
            print(i, 'iiiiii')
            result.append(temp[i: i+3])
            if i+3 < N:
                result.append(temp[i+3])
            confirm_odd(i+4, result)
            if i+3 < N:
                result.pop()
            result.pop()
            result.append(temp[i])
            if i+1 < N:
                result.append(temp[i+1])

        # i+4에서 시작

N = int(input())
nums = [0]*N
temp = input()
for i in range(N):
    if not i % 2:
        nums[i] = int(temp[i])
    else:
        nums[i] = temp[i]

result = []
confirm_odd(0, result)