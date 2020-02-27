# N개의 수가 주어짐
# 수와 수 사이에 연산자를 하나씩 넣음
# 식 계산은 우선순위를 무시하고 앞에서 진행
# 나눗셈은 몫
# 음수를 양수로 나누면
# 음수 -> 양수로 바꾸고 몫을 취하고, 그 몫을 음수로 바꿈
# 결과가 최대 인것 과 최소인 것을 구함
N = int(input())
nums = list(map(int, input().split()))
tools = list(map(int, input().split()))
min_result = 19999999999
max_result = -19999999999
visited = tools[:]
result = nums[0]

def dfs(depth, result):
    global max_result, min_result, visited
    ori_result = result
    if depth == N:
        if result < min_result:
            min_result = result

        if result > max_result:
            max_result = result

    else:
        for i in range(4):
            if visited[i]:
                visited[i] -= 1
                if i == 0:
                    result += nums[depth]
                elif i == 1:
                    result -= nums[depth]
                elif i == 2:
                    result *= nums[depth]
                else:
                    if result < 0:
                        temp = -result
                        result = -(temp//nums[depth])
                    else:
                        result //= nums[depth]

                dfs(depth+1, result)

                result = ori_result
                visited[i] += 1

dfs(1, nums[0])
print(max_result)
print(min_result)




