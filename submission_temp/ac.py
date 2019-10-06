from collections import deque

T = int(input())
for tc in range(1, T+1):

    p = input()
    N = int(input())
    temp = input()
    temp = temp[1:-1]

    if N:
        nums = deque(list(map(int, temp.split(','))))
    else:
        nums = deque(temp)
    print(nums, tc, '====')
    flag = 1
    for x in p:
        if x == 'R':
            if flag:
                flag = 0
            else:
                flag = 1
        else:
            try:
                if flag:
                    nums.popleft()
                else:
                    nums.pop()
            except IndexError:
                flag = 3
                break

    if flag == 1:
        print(list(nums), '답')
    elif flag == 3:
        print('error', '답')
    else:
        nums.reverse()
        print(list(nums), '답')