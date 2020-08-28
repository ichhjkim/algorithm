A, B = map(int, input().split())
result = 0
for x in range(A, B+1):
    #result += bin(x).count('1')
    cnt = 0
    while x:
        x = x & (x-1)
        cnt += 1
    result += cnt


print(result)