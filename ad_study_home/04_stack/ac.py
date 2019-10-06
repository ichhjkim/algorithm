from collections import deque

T = int(input())
for tc in range(1, T+1):

    p = input()
    N = int(input())
    temp = input()
    temp = temp[1:-1]

    if N:
        nums = deque(temp.split(','))
    else:
        nums = deque(temp)
    flag = 1
    for x in range(len(p)):
        if p[x] == 'R':
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
        print('[', end='')
        print(','.join(nums), end='')
        print(']')
    elif flag == 3:
        print('error')
    else:
        nums.reverse()
        print('[', end='')
        print(','.join(nums), end='')
        print(']')