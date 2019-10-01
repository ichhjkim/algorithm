N = int(input())

nums = list(map(int, input().split()))

nums.sort()
temp = 0
result = 0
for i in nums:
    temp += i
    result += temp

print(result)