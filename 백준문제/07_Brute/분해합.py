def finding(num):
    global min_result, min_x
    result = num

    while num:
        result += num % 10
        num = num // 10
    if result == ori_N:
        return True
    return False

N = input()
count = len(N)
ori_N = int(N)
candidates = ori_N-(9*(count-1))
min_x = 0
for i in range(candidates, ori_N-3):
    if finding(i):
        min_x = i 
        break

print(min_x)


