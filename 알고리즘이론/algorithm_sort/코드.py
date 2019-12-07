import sys
import copy
​
sys.stdin = open('최대상금.txt', 'r')
​
def backtrack(s, nums, increase):
    global max_result
​
    if increase == count:
        a = ''.join(nums)
        if int(a) > max_result:
            max_result = int(a)
​
    else:
        for i in range(len(nums)):
            for j in range(len(nums)):
                # 조합으로 돌리려고 중복되는 경우의 수를 없애고자 i > j 를 했어용
                if i > j:
                    nums[i], nums[j] = nums[j], nums[i]
                    a = int(''.join(nums))
                    # 나름 가지치기를 시도해보았어요, 근데... 이 가지치기는 아닌 것 같아여
                    if a > max_result:
                        # 비지티드 해줘도 음... 답이 나오는 건 아니더라구욥 대체 뭐가 문제인지..
                        visited[a] = 1
                        backtrack(s, nums, increase+1)
                        nums[j], nums[i] = nums[i], nums[j]
                        visited[a] = 0
​
​
T= int(input())
​
for tc in range(1, T+1):
​
    nums = input().split()
    count = int(nums[-1])
    nums = list(''.join(nums[0]))
    max_result = 0
​
    visited = [0] * (10**len(nums))
    backtrack(0, nums, 0)
​
    print('#{} {}'.format(tc, max_result))


          11              -1, +1, *2, -10
10     12     22     1                   배열[10]=1  배열[12]=1 ...

777770

1번쨰 시도 : 777770     777770
           15개 경우    15개 경우
           15
           15
           10억             10억
           10초            10ㅊ
